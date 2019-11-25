import math
import  scipy.integrate 

# Ld = lookahead line = center of rear axie to target point
# alpha = angle between heading and Ld
# # R = radius of instantaneous center of control
# Kappa = curvature
# delta = steering angle

def R(Ld,alpha):
    # Ld / sin alpha = 2R
    # R = Ld / (sin(alpha) * 2)
    R = Ld / (2 * math.sin(alpha))
    return R

def Kappa(r):
    # Kappa = 1 / R = 2 sin alpha / Ld
    k = 1.0 / r
    return k

def delta(K,L):
    #delta = arctan (2L sin alpha / Ld) 
    d = math.atan(K * L)
    return d

# crosstrack error function
def cte(t,e):
    k = 1
    return -k * e

def crosstrack():
    result = scipy.integrate.solve_ivp(cte,(0.0,2.0),[4])
    return result


L = 4
Ld = 10
alpha = math.radians(30.0)
r = R(Ld,alpha)
print(r)

k = Kappa(r)
print(k)

Ld = 15
L = 5
alpha = math.radians(60.0)
# get radius of rotation center
r = R(Ld,alpha)
# inverse of arc radius
k = Kappa(r)
# steering angle
d = delta(k,L)
# radians
print(d)
# degrees
print(math.degrees(d))

ct = crosstrack()
print(ct)
