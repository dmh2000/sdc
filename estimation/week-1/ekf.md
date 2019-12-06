## extended kalman filter

linear KF doesn't work if measurements or control inputs are nonlinear

example: orientation is nonlinear (spherical)

EKF : for nonlinear systems

EKF uses first-order linearization
role of Jacobians

linear systems don't exist in reality : curve or step

linearization : pick operating point then approximate with tangent

Taylor series expansion of function calculated by explansion of terms of derivative

operating point for taylor expansion : most recent esimate of state

motion model : lienarize about posterior estimate
predictor model : linearize about prediction of current state based on current model

state space jacobians: F, L ,H, M
matrix of all first-order partial derivatives of a vector values function
column of jacobians function outputs

3d vector -> 2d vecotrs = 2x3 vector

jacobian tells you how fast each output of the function is chaning along each input dimension
