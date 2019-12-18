import numpy as np

# https://www.youtube.com/watch?v=JaFrOn0zf50
# 2D KALMAN FILTER

# initial state
x_0 = np.array([
    4000.0,  # x = m
    280.0,  # vx = m/sec
    # 3000.0,  # y = m
    # 120.0,  # vy = m/sec
])

a_x = np.array([2.0])  # m/sec
dt = 1.0

# observations
Y_m = np.array([
    [4000.0, 280.0],
    [4260.0, 282.0],
    [4550.0, 285.0],
    [4860.0, 286.0],
    [5110.0, 290.0]
])

# process errors
dx = 20.0
dv = 5.0
P = np.array([
    [dx ** 2, 0],  # P_x
    [0, dv ** 2]  # P_v
])
print(P)

# observation errors
R = np.array([
    [25.0 ** 2, 0.0],  # m
    [0.0, 6.0 ** 2]  # m/sec
])
print('R', R)

A = np.array([
    [1.0, dt],
    [0.0, 1.0]
])
print('A', A)

B = np.array([
    0.5 * dt ** 2,
    dt
])
print('B', B)

# measurement model
C = np.identity(2)

W = 0
Q = 0

# motion model
H = np.identity(2)
print('H', H)

# initial condition
X_k = x_0
print('X_k', X_k)
print("RUN ==================================")
for k in range(1, 5):
    print('---k---', k)
    # PREDICT
    print("predict-----------")
    # predict future state
    X_k = A @ X_k + B * a_x + W
    print('X_k', X_k)

    # update process covariance
    P = A @ P @ A.T + Q
    P[0, 1] = 0
    P[1, 0] = 0
    print('P', P)

    # calculate Kalman gain
    K = (P @ H.T) * np.linalg.inv(H @ P @ H.T + R)
    print('K', K)

    # CORRECT
    print("correct-----------")
    # adjust observation
    Y_k = C @ Y_m[k] + 0
    print('Y_k', Y_k)

    # correct the state
    X_k = X_k + K @ (Y_k - H @ X_k)
    print('X_k', X_k)

    # update P
    P = (np.identity(2) - K @ H) @ P
    print('P', P)
    print("=================================")
