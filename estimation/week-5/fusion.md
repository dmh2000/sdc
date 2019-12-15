## sensor fusion

Error state EKF with IMU, GNSS and LIDAR
position, velocity, orientation

why different sensors?

- error dynamics are uncorrelated
- use complementary sensors
- GNS absolute positions to mitigate imu drift
- LIDAR provides accurate local positioning with local maps
- GNSS tells which map to use

tight vs loosely coupled

state vector - 10D position (3), velocity (3), orientation quternion (4)
motion model - 6D acceleration/force (3) and rotation rates (3) sensor frame
no bias tracking

linearized motion model
error state (3D rotation error) {dp,dv,dphi) 9D

mesurement model

LOOP

1. update state with imu inputs (gnss corrected or not)
2. propagate uncertainty
3. if GNSS or LIDAR available,
   1. compute Kalman gain
   2. compute error state
   3. correct predicted state
4. compute corrected covariance
