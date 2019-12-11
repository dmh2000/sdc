import numpy as np
import matplotlib.pyplot as plt
import sklearn

dt = 0.5
u = np.array([-2.0])
S = 20.0
y = np.pi / 6.0
D = 40.0
v = 0.01

# initial p_hat is from Lesson 1 Linear KF
P_hat = np.array([
    [v, 0],
    [0.0, 1.0]
])

# x_hat 0
x_hat = np.array([0, 5]) @ P_hat

# motion model
F = np.array([
    [1.0, dt],
    [0.0, 1.0]
])

L = np.identity(2)

Q = np.array([
    [0.1, 0.0],
    [0.0, 0.1]
])

M = np.identity(1)
R = np.array([0.01])


def f(x, u, dt):
    '''
    process model
    state update + acceleration term (u) + noise
    '''
    return F @ x + np.array([[0.0], [dt]]) @ u


def h(x, v):
    '''
    measurement model:
    angle between car and landmark using
    arctan of landmark height (S) over 
    distance to landmark (D-position)
    '''
    return np.array([np.arctan(S / (D-x)) + v])


# -------------------
# predict
# -------------------
x_hat = f(x_hat, u, dt)
P_chk = F @ P_hat @ F.T + L @ Q @ L.T
print('P_chk', P_chk)

# -------------------
# correct
# -------------------
# recompute H when x_hat changes
H = np.array([
    [S / ((D - x_hat[0])**2 + S**2), 0.0]
])
print('H', H)

# Kalman Gain
K = P_chk @ H.T @ np.linalg.inv(H @ P_chk @ H.T + M @ R @ M.T)
print('K', K)

# correct the prediction
x_hat = x_hat + K @ (y - h(x_hat[0], v))

print('x', x_hat)

i = np.identity(2)
P_hat = P_chk - K @ H @ P_chk
print('P_hat', P_hat)
P_hat = (i - K @ H) @ P_chk
print('P_hat', P_hat)
