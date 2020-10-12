# outliers

localization:

- given any two images, find translation from image 1 to image 2
- also keep scale and skew

- T = [t_u,t_v]
  - find displacement in u axis t_u
  - find displacement in v axis t_v
- compute features in image 1 and 2
- match with brute force matcher

solution:
match : each feature in all matches pairs are identified by u,v
model:
t_u1 + t_u = u_i2
t_v1 + t_v = v_i2
find translation T = t_u,t_v solve with least squares all pixels

identify outliers using Random Sample Consensus (ransac)

- init
  - given amodel find smallest number of sames M from which the model can be computed
  - problem is localization
  - data it t_u,t_v
- loop
  - select M random samples
  - compute model paraetmers using M
  - inlier set: count how many data points agree with the model parameters C
  - if C > inlier threshold or max iteration reached, terminate
- final
  - recompute model parameters from entire inlier set
