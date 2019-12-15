from numpy import *
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import


# [x,y,z] = h-1(r,a,c) = [
# rcos(a)cos(e),
# rsin(a)cos(e),
# rsin(e)
# ]

def p2c(e, a, r):
    e = np.radians(e)
    a = np.radians(a)
    x = r * np.cos(a) * np.cos(e)
    y = r * np.sin(a) * np.cos(e)
    z = r * np.sin(e)
    return x, y, z


def sph_to_cart(epsilon, alpha, r):
    """
    Transform sensor readings to Cartesian coordinates in the sensor
    frame. The values of epsilon and alpha are given in radians, while
    r is in metres. Epsilon is the elevation angle and alpha is the
    azimuth angle (i.e., in the x,y plane).
    """
    p = zeros(3)  # Position vector
    # Your code here
    p[0] = r * np.cos(alpha) * np.cos(epsilon)
    p[1] = r * np.sin(alpha) * np.cos(epsilon)
    p[2] = r * np.sin(epsilon)
    return p


def estimate_params(P):
    """
    Estimate parameters from sensor readings in the Cartesian frame.
    Each row in the P matrix contains a single 3D point measurement;
    the matrix P has size n x 3 (for n points). The format is:

    P = [[x1, y1, z1],
         [x2, x2, z2], ...]

    where all coordinate values are in metres. Three parameters are
    required to fit the plane, a, b, and c, according to the equation

    z = a + bx + cy

    The function should retrn the parameters as a NumPy array of size
    three, in the order [a, b, c].
    """
    param_est = zeros(3)

    rows, cols = P.shape
    A = np.ones((rows, 3))
    x = P[:, 0]
    y = P[:, 1]
    z = P[:, 2]
    A[:,1] = x
    A[:,2] = y
    b = z
    param_est = np.linalg.inv(A.T @ A) @ A.T @ b

    return param_est


print(p2c(5, 10, 4))

a = np.random.rand(10, 3)
r = estimate_params(a)
print(r)

# (3.92,0.69,0.35)
