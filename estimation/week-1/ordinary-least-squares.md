## Least Squares

Localization - method to determine location and position in world (know where they are)

State Estimation - final optimal value from assumptions
about sensors and measurements

States

- location
- position

Parameter
resistance of component

Ordinary Least Squares

- ordinary
- weighted

Squared Error Criterion

Method of Least Squares

- Gauss - discovery of planet ceres
- least squares error
- normal equations for parameter estimation

Late 18th century

- Giuseppe Piazzi
  - 24 observations
  - 4 days
  - 900 Km diameter
- Gauss
  - used least squares to quanity ceres orbit

The most probable value of an unknown parameter is that which minimizes the sum of squared errors of the differences between what we observe and computed values (expected value)

Measuring a resistor

- cheap multimeter
- take 4 measurements
- expected value is 1 kohm with 5% variance
- y = x + v
  - x - measured resistance
  - v - measurement noise
  - y - actual value
  - x_hat = esimate
  - residual : difference between y (actual value) - estimated value(x_hat)
  -
- Squared Error
  - e = (y - x)\*\*2
- argmin of sum of errors - Loss Function

e = vector of measuremnts = h - Hx
H = jacobian MxN

- M = number of measurement
- N = number of unknown parameters
- rectangular
  x = scalar or vector

S(x) = eT * e = yT*y - xTHTy - yTHx + xTHTHx

to minimize this, compute partial derivative, set to 0, solve for extremum

dS/dX = -yTH - yTH + 2x_hatThTH = 0

x_hatLS = (hTh)-1 \* hTy
unique if x_hat has an inverse (hTH)-1 exists

m measurements, n unknowns

- H element R(mxn)
- HtH element R(nxm)
- (hTh)-1 exists only if there are many measurements as there are unknowns : m >= n

X_hat = (hTH)-1hTy = arithmetic mean of the measurements

- minimizes simple least squares criteral
- measurement model is linear
- measurements are equally weighted

Method of Least Squares

- Gauss,ceres
- LS minimizes least squares criterion
- Ordinary least squares assumes measurements are weighted equally
- measurement model is linear
