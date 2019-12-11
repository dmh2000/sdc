import sympy as sp
from sympy import *

xl, yl, d, xk, yk, theta, T, v_k, om_k, w_k, Q = \
    symbols('xl yl d xk yk theta T v_k om_k w_l Q')

sp.init_printing()

# y_k = sp.Matrix([
#     sqrt((xl - xk - d * cos(theta)) ** 2 + (yl - yk - d * sin(theta)) ** 2),
#     atan2(yl - yk - d * sin(theta), xl - xk - d * cos(theta)) - theta
# ])

y_k = sp.Matrix([
    sqrt((xl - xk) ** 2 + (yl - yk) ** 2),
    atan2(yl - yk, xl - xk) - theta
])
state = sp.Matrix([xk, yk, theta])

print(y_k)

print(y_k.jacobian(state))

# np.array([
# [(d*cos(theta) + xk - xl)/sqrt((-d*sin(theta) - yk + yl)**2 + (-d*cos(theta) - xk + xl)**2),
#  (d*sin(theta) + yk - yl)/sqrt((-d*sin(theta) - yk + yl)**2 + (-d*cos(theta) - xk + xl)**2),
#  (-d*(-d*sin(theta) - yk + yl)*cos(theta) + d*(-d*cos(theta) - xk + xl)*sin(theta))/sqrt((-d*sin(theta) - yk + yl)**2 + (-d*cos(theta) - xk + xl)**2)
#  ],
# [-(d*sin(theta) + yk - yl)/((-d*sin(theta) - yk + yl)**2 + (-d*cos(theta) - xk + xl)**2),
#  -(-d*cos(theta) - xk + xl)/((-d*sin(theta) - yk + yl)**2 + (-d*cos(theta) - xk + xl)**2),
#  d*(d*sin(theta) + yk - yl)*sin(theta)/((-d*sin(theta) - yk + yl)**2 + (-d*cos(theta) - xk + xl)**2) - d*(-d*cos(theta) - xk + xl)*cos(theta)/((-d*sin(theta) - yk + yl)**2 + (-d*cos(theta) - xk + xl)**2) - 1
#  ]
# ])

np.array([
    [(xk - xl)/sqrt((-xk + xl)**2 + (-yk + yl)**2),
     (yk - yl)/sqrt((-xk + xl)**2 + (-yk + yl)**2),
     0],
    [-(yk - yl)/((-xk + xl)**2 + (-yk + yl)**2),
     -(-xk + xl)/((-xk + xl)**2 + (-yk + yl)**2),
     -1]
    ])