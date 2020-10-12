# camera sensor weeks 1

## pinhold camera

object -> pinhole barrier -> imaging sensor
pinhole camera model

- focal length f : distance between pinhole and sensor plane
- camera center (Cu,Cv)

## Projective Geometry

O_world -> aperature -> camera image plane

simplified camera model
O_world = [x,y,z]
O_image = [u,v]

- select world frame
- camera corrdinate frame (center of aperature)
- translation vector and rotation matrix for world frame -> camera coordinate frame
- image coordinate frame
  - Uy,Vx pixel frame top left U right, V down
- focal length : pinhole to image sensor

O_World -> O_camera = [R|T]O_world (extrinsic)
Rigid body transform T

- R = rotation
- t = tranlation
  O_camera -> O_image coordinates (intrinsic)
  use homogeneous coordinates (4x1 instead of 3x1)

O_world -> O_image

- matrix multiply K[R|t]
-

O_image -> O_pixel
[x,y,z] -> [u,v,1] = 1/z[x,y,z]

- non square pixels
- axis skew
- distortion
- non-unit aspect ratio
