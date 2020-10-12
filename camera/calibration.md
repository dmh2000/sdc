# CALIBRATION

## Projection Equations

O_image = P@O = K[R|t]@O_World

P = camera projection matrix

- extrinsic
- intrinsic

### world to image

O_image = [x,y,z] = RK[R|t] @ [X,Y,Z,1]

### Image to Pixel

O_pixel = [x,y,z] => [u,v,1] = 1/z \* [x,y,z] = [su,sv,s]
divide image coordinates by Z (distance) component
s = scale

scale is important for stereo computation

## Calibration Problem

o = P@O = K[R|t] @ O
[su,sv,s] = [
?,?,?,?,
?,?,?,?,
?,?,?,?,
] @ [X,Y,Z,1]

3x4 @ 4x1

### Process

use image with known geometry (like a 3d checkerboard)
2D image to 3d World
find least squares solution for P
[su,sv,s] = [
P11,P12,P13,P14,
P21,P22,P23,P24,
P31,P32,P33,P34,
] @ [X,Y,Z,1]

solve system of linear equations

1. set up 3 equations
   su - P11X - P12Y - P13Z - P14 = 0
   sv - P21X - P22Y - P23Z - P24 = 0
   s - P31X - P32Y - P33Z - P34 = 0

2. substitute S into third equation to get 2 equations per point
   s = P31X + P32Y + P33Z + P34 = 0

2 equations per point
P31Xu + P32Yu + P33Zu + P34u - P11X - P12Y - P13Z - P14 = 0
P31Xv + P32Yv + P33Zv + P34v - P21X - P22Y - P23Z - P24 = 0

3.  solve with singular value decomposition or pseudo-inverse
    advantages

- easy to formulate
- closed for solution
  disadvantages
- doesn't provide camera parameters
- doesn't model complex phenomeman, distortions
- doesn't allow for constraints like focal length

## RQ factorization P

3d camera center = P @ C where C is point that projects to 0

P = K[R|t]
= K[R] | -RC]
= [KR | -KRC]

M = KR
P = [M | -MC]
M = R_ut @ Q
upper triangular R_ut
orthogonal 3x3 Q

intrinsic calibration matrix K + R_ut
rotation matrix R = Q

translation vector
t = -K_inv @ P[:,4] = -K_inv @ M @ C
