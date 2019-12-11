import sympy as sp
from sympy import *

xl, yl, d, x, y, theta, T, v_k, om_k, w_k, Q = \
    symbols('xl yl d x y theta_k-1 T v_k om_k w_l Q')

sp.init_printing()

x_k = sp.Matrix([[x], [y], [theta]]) + \
      T * sp.Matrix([[cos(theta), 0], [sin(theta), 0], [0, 1]]) @ \
      (sp.Matrix([[v_k], [om_k]]))
state = sp.Matrix([x, y, theta])

print(x_k)

print(x_k.jacobian(state))


