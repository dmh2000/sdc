import numpy as np

# PROCESS COVARIANCE

# STATE VECTOR
# X = [x,x_dot]
x_0 = 50.0
v_0 = 5.0
a_0 = 2.0

# process sigma
sigma_x = 0.5
sigma_v = 0.2
'''
P = [
    sigma_x**2      sigma_x * sigma_v
    sigma_v*sigma_x sigma_v**2
'''
P = np.array([
    [sigma_x * sigma_x, sigma_x * sigma_v],
    [sigma_x * sigma_v, sigma_v * sigma_v]
])
print(P)

# if estimate error for x (position) is completely indepent
# of the other variable x_dot (velocity)
# then the covariances elements = 0
#
# no adjustments are made to the estimates of one variable due
# to the process error of the other variable
P = np.array([
    [sigma_x * sigma_x, 0],
    [0, sigma_v * sigma_v]
])
print(P)
