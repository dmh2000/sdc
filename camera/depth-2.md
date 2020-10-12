# estimating disparity

disparity : difference in image location of the same 3d point under perspective to two different cameras

find same point in left and right images

- brute force
- epipolar contraint

epipolar line : horizontal line on X axis between points on left and right
constrain search to epipolar line : 2 dimensions to 1
optical axes are parallel
if not, epipolar lines are skewed, use multiview geometry

given rectified images and stereo calibration
for each epipolar line:

- take each pixel on this line in left image
- compare left pixels to every right pixel on same epipolar line
- choose pixel that has minimum cost
  - pixel intensity, color
- compute disparity p
