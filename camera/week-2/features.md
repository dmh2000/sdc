# image features and detectors

## extraction

- find features
- identify
- correlate

features

- salient : important, distinctive points of interest in image
- repeatable : can be found in multiple images
- local - small subset of image
- numerous : enough points
- efficient : computable in reasonable time

repeatitive texture less patch are hard
patches with large contrast changes graident are easier to detect (edges)
gradients with two significantly different oreientations (corners)

harris corner detector

- uses image gradient (illumination changes)
- no scale invarient (distance from camera
  harris-laplace
- add scale detection
  Fast
  Laplacian of gaussian (LOG)
  different of gaussian (DOG)
