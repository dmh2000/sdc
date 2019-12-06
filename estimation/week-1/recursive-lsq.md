## Recursive Least Squares

recursive linear estimator
resistance is the unknown parameter

running estimate of optimal parameter
incremental updates

x_hat : best estimate
y_k : new measurement
H_k : jacobian at k
V_k : gaussian noise

Goal: compute x_hat_k as a function of Y_k and x_hat_k_1

# FIR for error with gain K

x_hat = x_hat_1 + K_k @ (y_k - Hk@x_hat_t)
innovation
need recursive lsq criterion  
Lrls = Expected(error^2) at time K
= sigma_k^2

minimize expected value of sum of squared errors at time k
Trace(P_k)

covariance as a function of K
P_k = (1-K_k @ H_k)@P_k_1

K = Pk_1 @ H.Tk @ inv(Hk@Pk_1@H.Tk - Rk)

init
x_hat_0 = E[x] (expected value of x)
P_0 = E{(x-x_hat_0)(x-x_hat_0).T}

measurement model  
 y_k = H_k @ X + V_k

### update

#Construct K_k

# K_k = ...

K_k = P_k @ H_k.T @ inv(H_k @ P_k @ H_k.T + Var)
  
#Update our estimate

# x_k = ...

x_k = x_k + K_k @ (V[k] - H_k @ x_k)

#Update our uncertainty

# P_k = ...

P_k = (1.0 - K_k @ H_k) @ P_k
