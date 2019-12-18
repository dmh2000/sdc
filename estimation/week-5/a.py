import numpy as np

A = np.array([
    [90, 80, 40],
    [90, 60, 80],
    [60, 50, 70],
    [30, 40, 70],
    [30, 20, 90]
])
print(A)

N = A.shape[0]

I = np.ones(N)
print(I)
# a = A - (I @ A) / 5.0

# sums
B = (I @ A)
print(B)

# averages
C = B / 5.0
print(C)

# deviation matrix
a = A - C
print(a)

# deviation matrix computed
a = A - (I @ A) / 5.0
print(a)

# compute covariance
M = (a.T @ a) / (N - 1)
print(M)

# numpy covariance
D = np.cov(A.T)
print(D)
