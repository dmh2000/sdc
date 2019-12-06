## BIAS

best linear unbiased estimator

biased :
average error does not approach zero

unbiased :
filter produces an average error of zero at a particular time step over many trials

error dynamics:

- predicted state error e_k = x_hat_k - x_k
- corrected estimate error e_k = x_hat_k - x_k

initial state estimate should be unbiased
noise is white and gaussian

kalman filters are consistent

- covariance at k matches expected error at k
-
