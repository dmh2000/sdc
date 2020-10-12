# IMAGE FILTERING

cross corelation and convolution

dealing with noise

salt and pepper noise

- results in outliers in neighborhood
- replace outlier with mean of surrounding pxiesl
- mean filterG[U,v] = (1 / (2K + 1)\*_2) _ row/column sum
- add H weight (kernel)
- mean filter, H = 1/9
- gaussian weight H = 1/16

convolution

- cross-correlation where filter is flipped both horizontally and vertically before applying
- unlike correlation, convolution is associative
- if H and F are filter kernels
  - H \* (F \* I) = (H \* F) \* I
  - apply any number of kernels to an image
  - precompute convolutions H \* F then apply once
  - reduces runtime to a single pass

template matching

- pxels with highest response from cross-corellation is location of template pixel
- image \* pixel = match

gradient computation

- sobel kernel
- edges and corners
