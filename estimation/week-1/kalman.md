## Kalman Filters

kalman filter is used to fuse measurements of several
sensors to real time estimate state of a robotic system
history of Kalman Filter

Linear formulation

BLUE : best linear unbiased estimator

nonlinear -> linearize

limitiation of linearization

unscented kalman filter

1. describe kalman filters as two stage filter : predict, corrrect
2. difference motion and measurement models
3. use KF in 1D localization example

Kalman, 1960 linear theory

Apollo guidance computer

similar to RLS but
RLS esimates a static parameter
KF estimates an evolving state

KF : make a probabilistic esimate of state by predict then correct

1D localization 1. use motion model to predict state using wheel odometry, IMU 2. use observation model (measurement), GPS, Lidar to correct prdiction

motion model
estimate at step k is a linear combination of the estimate at time step k_1
, a control input and some zero mean noise
x_k = F_1@x_1 + G_1@u_1 + w_q
F_1 is esimate at k-1
G_1@u_1 is a control input
w_1 is nonzero mean gaussian noise
input u is an external signal that modifies the state

    measurement model y_k = H@X + v
    measuremnt moise
    process (motion) noise

KF is an RLS that also includes a process (motion) model

    1a. predict the new state using process model
    1b. propagate the uncertainty
    2a. use measurement to compute optimal gain
    2b. correct prediction
    2c. probate probability

process model :

- 'open loop' model of how the process changes
- probably not accurate
- throttle setting results in expected acceleration
- odometer reading results in expected displacement

measurement model:

- statistical characteristics of sensor information

### predict

- output is a fuzzy estimate
- F = prediction matrix (map inputs to outputs)
- G = control input
- P = covariance matrix
- Q = process noise covariance matrix

- x_hat = F @ x + G @ u
- P_hat = F @ P @ F + Q

### correct

- use measurements to correct the fuzzy estimate
- H = sensor model
- R = sensor/measurement model = noise covariance matrix (constant)
- mu = expected mean = H@x_hat
- sigma = expected covariance = H @ P @ H.T

- K = P_hat @ H.T @ inv(H @ P_hat @ H.T + R)
- x_hat = x_hat + K @ (y - H @ x_hat)
- P_hat = (1- K @ H) @ P_hat
