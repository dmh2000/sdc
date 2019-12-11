import pickle
import numpy as np
import matplotlib.pyplot as plt

with open('data/data.pickle', 'rb') as f:
    data = pickle.load(f)

t = data['t']  # timestamps [s]

x_init = data['x_init']  # initial x position [m]
y_init = data['y_init']  # initial y position [m]
th_init = data['th_init']  # initial theta position [rad]

# input signal
v = data['v']  # translational velocity input [m/s]
om = data['om']  # rotational velocity input [rad/s]

# bearing and range measurements, LIDAR constants
# bearing to each landmarks center in the frame attached to the laser [rad]
b = data['b']
r = data['r']  # range measurements [m]
l = data['l']  # x,y positions of landmarks [m]
d = data['d']  # distance between robot center and laser rangefinder [m]

v_var = 0.01  # translation velocity variance
om_var = 0.01  # 0.01  # rotational velocity variance
r_var = 0.01  # range measurements variance
b_var = 0.01  # bearing measurement variance

Q_km = np.diag([v_var, om_var])  # input noise covariance
cov_y = np.diag([r_var, b_var])  # measurement noise covariance

x_est = np.zeros([len(v), 3])  # estimated states, x, y, and theta
P_est = np.zeros([len(v), 3, 3])  # state covariance matrices

x_est[0] = np.array([x_init, y_init, th_init])  # initial state
P_est[0] = np.diag([1, 1, 0.1])  # initial state covariance

# initialize P_chk
P_check = P_est[0]


# Wraps angle to (-pi,pi] range
def wraptopi(x):
    if x > np.pi:
        x = x - (np.floor(x / (2 * np.pi)) + 1) * 2 * np.pi
    elif x < -np.pi:
        x = x + (np.floor(x / (-2 * np.pi)) + 1) * 2 * np.pi
    return x


# motion model
def f(x, v, omega):
    # noise term
    w = np.random.normal(loc=0, scale=Q_km)
    w_k = np.array([w[0, 0], w[1, 1]])

    # update term
    theta = x[2]
    a = np.array([
        [np.cos(theta), 0],  # * [v,omega] = cos(velocity),0
        [np.sin(theta), 0],  # * [v,omega] = np.sin(velocity),0
        [0, 1]  # * [v,omega] = 0,omega
    ])

    # input term
    b = np.array([
        v, omega
    ]) + w_k

    # scale with noise
    c = a @ b

    # add to previous pose
    return x + c


# measurement model
def h(xk, lk, n):
    # extract scalars
    x_k = xk[0]
    y_k = xk[1]
    theta = xk[2]

    d = 0

    x_l = lk[0]
    y_l = lk[1]

    # x, y terms
    a = (x_l - x_k - d * np.cos(theta))
    b = (y_l - y_k - d * np.sin(theta))

    # range
    r = np.sqrt(a ** 2 + b ** 2)

    # angle
    phi = wraptopi(np.arctan2(b, a) - theta)

    # add noise
    return np.array([r, phi]) + n


def measurement_update(lk, rk, bk, P_check, x_check):
    # 1. Compute measurement Jacobian
    xl = lk[0]
    yl = lk[1]
    xk = x_check[0]
    yk = x_check[1]
    theta = wraptopi(x_check[2])
    d = 0

    M = np.identity(2)
    H = np.array([
        [(d * np.cos(theta) + xk - xl) / np.sqrt(
            (-d * np.sin(theta) - yk + yl) ** 2 + (-d * np.cos(theta) - xk + xl) ** 2),
         (d * np.sin(theta) + yk - yl) / np.sqrt(
             (-d * np.sin(theta) - yk + yl) ** 2 + (-d * np.cos(theta) - xk + xl) ** 2),
         (-d * (-d * np.sin(theta) - yk + yl) * np.cos(theta) + d * (-d * np.cos(theta) - xk + xl) * np.sin(
             theta)) / np.sqrt((-d * np.sin(theta) - yk + yl) ** 2 + (-d * np.cos(theta) - xk + xl) ** 2)
         ],
        [-(d * np.sin(theta) + yk - yl) / ((-d * np.sin(theta) - yk + yl) ** 2 + (-d * np.cos(theta) - xk + xl) ** 2),
         -(-d * np.cos(theta) - xk + xl) / ((-d * np.sin(theta) - yk + yl) ** 2 + (-d * np.cos(theta) - xk + xl) ** 2),
         d * (d * np.sin(theta) + yk - yl) * np.sin(theta) / (
                     (-d * np.sin(theta) - yk + yl) ** 2 + (-d * np.cos(theta) - xk + xl) ** 2) - d * (
                     -d * np.cos(theta) - xk + xl) * np.cos(theta) / (
                     (-d * np.sin(theta) - yk + yl) ** 2 + (-d * np.cos(theta) - xk + xl) ** 2) - 1
         ]
    ])

    np.array([
        [(xk - xl) / np.sqrt((-xk + xl) ** 2 + (-yk + yl) ** 2),
         (yk - yl) / np.sqrt((-xk + xl) ** 2 + (-yk + yl) ** 2),
         0],
        [-(yk - yl) / ((-xk + xl) ** 2 + (-yk + yl) ** 2),
         -(-xk + xl) / ((-xk + xl) ** 2 + (-yk + yl) ** 2),
         -1]
    ])

    H = H.reshape((2, 3))

    # 2. Compute Kalman Gain
    K = P_check @ H.T @ np.linalg.inv(H @ P_check @ H.T + M @ cov_y @ M.T)

    # 3. Correct predicted state (remember to wrap the angles to [-pi,pi])
    y_l = np.zeros(2)
    y_l[0] = rk
    y_l[1] = wraptopi(bk)

    y_check = h(x_check, lk, np.array([0, 0]))

    x_hat = x_check + K @ (y_l - y_check)

    # 4. Correct covariance
    P_check = (np.identity(3) - K @ H) @ P_check

    return x_check, P_check


# 5. Main Filter Loop #######################################################################

x_check = x_est[0]
for k in range(1, len(t)):  # start at 1 because we've set the initial prediciton

    delta_t = t[k] - t[k - 1]  # time step (difference between timestamps)

    # 1. Update state with odometry readings (remember to wrap the angles to [-pi,pi])
    x_check = f(x_check, v[k], om[k])

    # 2. Motion model jacobian with respect to last state
    theta_k = x_check[2]

    F_km = np.array([[1, 0, -delta_t * v[k] * np.sin(theta_k)],
                     [0, 1, delta_t * v[k] * np.cos(theta_k)],
                     [0, 0, 1]])

    # 3. Motion model jacobian with respect to noise
    L_km = np.zeros((3, 2))

    # 4. Propagate uncertainty
    P_check = F_km @ P_check @ F_km.T + L_km @ Q_km @ L_km.T

    # 5. Update state estimate using available landmark measurements
    for i in range(len(r[k])):
        x_check, P_check = measurement_update(l[i], r[k, i], b[k, i], P_check, x_check)

    # Set final state predictions for timestep
    x_est[k, 0] = x_check[0]
    x_est[k, 1] = x_check[1]
    x_est[k, 2] = x_check[2]
    P_est[k, :, :] = P_check

e_fig = plt.figure()
ax = e_fig.add_subplot(111)
ax.grid()
ax.plot(x_est[:, 0], x_est[:, 1])
ax.set_xlabel('x [m]')
ax.set_ylabel('y [m]')
ax.set_title('Estimated trajectory')
plt.show()

# e_fig = plt.figure()
# ax = e_fig.add_subplot(111)
# ax.grid()
# ax.plot(t[:], x_est[:, 2])
# ax.set_xlabel('Time [s]')
# ax.set_ylabel('theta [rad]')
# ax.set_title('Estimated trajectory')
# plt.show()
