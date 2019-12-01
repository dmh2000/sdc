import sklearn
import numpy as np
import matplotlib.pyplot as plt

# V = IR
# 1D array == transpose of that array
I = np.array([0.2, 0.3, 0.4, 0.5, 0.6])
print(I)
I = I.T
print(I)
V = np.array([1.23, 1.38, 2.06, 2.47, 3.17])
print(V)
V = V.T
print(V)

# X COORDINATES GO IN H
H = np.array([
    [1, 0.2],
    [1, 0.3],
    [1, 0.4],
    [1, 0.5],
    [1, 0.6]])
print(H)
print(H.T)


# Now estimate the resistance parameter.
# R = ...
R = np.linalg.lstsq(H, V, rcond=1)

print(R)
# Y COORDINATES GO HERE
# (H.T @ H) @ (H.T @ Y)
# stepwise
a = H.T @ H
print(a)
b = np.linalg.inv(a)
print(b)
c = H.T @ V
print(c)
d = b @ c
print(d)

# Y COORDINATES GO IN MATRIX MULT
R = np.linalg.inv(H.T @ H) @ (H.T @ V)
print('r', R)
R = R[1]

# USING numpy
S = np.linalg.lstsq(H, V, rcond=None)
print('s', S[0])

i = np.arange(0, 1.1, 0.1)
v = R * i
plt.grid()
plt.plot(i, v)
plt.show()
