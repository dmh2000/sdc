# DEPTH PERCEPTION - 1

2 cameras - multiview geometry

parallel optical axes : Right, Left
align cameras in 3D so the only difference is x offset

known:

- rotation/translation between cameras
- known projection O between camera frames
  assumptions
- cameras are identical
- optical axes are aligned

compute 3d location

f = flocal length
b = baseline x offset
rotation is identity
translation only has x offset

compute X,Z of point O
then compute Y from X,Z

Z/f = X / X_left
Z/f = (X - b)/ X_right

disparity = X_left - X_right
u0, v0 = 0 pixel
X_l = Ul - U0
X_r = Ur - U0
y_l = Vl - V0
y_r = Yr - Y0

Z = f \* b / d
X = (Z \* Xl) / f
Y - (Z \* Yl) / f

need f,b,u0,v0 : use stereo calibration

need X_r for each X_l : use disparity computation
