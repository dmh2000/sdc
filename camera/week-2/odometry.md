# visual odometry

VO incrementally estimate pose of vehcile by examing tchanges that motion induces on camera images
PRO:

- not affected by wheel slip
- more accurate trajectorsy than wheel odometry

CON:

- need external sensor to estimate absolute scale
- camera is no robust to weather and illumination
- any form of odometry drifts

estimate transform matrix between Tk and Tk-1 between consecutive images Ik-1,Ik
Tk = [
Rk,k-1, tk,k-1,
0, 1
]

concatenate the single movements over time recovers full trajectors given frame C1..Cm

General process

- given two consecutive images
  - perform detection and description
  - match the features
  - use matched feeatures to estimate motion to get Tk

motion estimation

- 2d-2d -> image u,v coordinates
- 3d-3d -> world 3d coordinates (stereo cameras)
- 3D-2d
  - given world coordinates of frame k-1
  - thru matching, ahve 2d coordinates in frame k
  - use camera projects
  - K is known from calibration O = P@O = K[R|t] @ O
  - reduces to estimate [R|t]
  - uses perspective N point algorithm
    - use DLT for R|t, forms linear model using SVD
    - improve use LM Levenberg-Marquart
    - need at least 3 points to solve P3P, 4 to avoid ambiguity
    -
