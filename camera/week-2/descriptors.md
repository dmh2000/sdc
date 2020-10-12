# feature descriptors

use matched features from two images for localization, object detect, support depth estimation to points

best match between frames

assign descriptor to each feature

descriptor:

- point u,v
- n dimensional vector summary of information
- invariance to transforms: translation, rotation, scale and illumination
  - repeatable
  - distinctiveness
  - compact
  - efficient : real time computation

SIFT : scale invariant feature transform

- 16x16 window of pixels : local neighborhood
- separate into 4 cells 4x5 patch
- compute edge orientation of each pixel
- suppress weak edges
- contruct 32 dimension historgram of orientations then contactenate
- 128 dimensional descriptor
- computed over multiple scales and orientation
- combined with feature detector

others:

- surf
- gloh
- brief
- org
