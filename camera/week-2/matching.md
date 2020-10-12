# feature matching

how to match on predefined distance
brute force matching

- identify features
- associate descriptors
- use features to match across images
- state estimation, object detection

brute force:

- define a distance function d(image fi,image fj) for comparison
- for every feature fi in image 1
  - compute distance
  - find closest match
  - keep if within delta threshold
- nearest neighbor
- sum of squared differences (SSD)
  - diff the descriptor values, square them and sum
  - sensitive to large variations
  - insensitivte to smaller
- sum of aboslute diffs
- hamming distance : uses binary features

brute force will find a match even when no corresponding feature exists
set distance threshold
brute force is computationally inefficient
enhanced by k-d tree spatial organization
