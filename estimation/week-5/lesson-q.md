- sensor fusion
- calibration
- failures
- final project

## practical considerations

- data from different sensors
- how to combine
- use EKF

## calibration

- car specific parameters (wheel radius...)
- relative poses between sensors
- combine to common reference frame
- time offsets between sensor update times, synchronization

## accuracy requirement

- 1 meter or less for lane keeping
- car 1.8 m wide
- lane 3 m wide
- gps 1-5 m

# speed

- update rate : 15-30 hz update rate
- computer power
- electrical power
- tradeoffs between algorithms and time required

# failures

- sensors fail (GPS in tunnel)
- estimation error (linearization error in EKF)
- state uncertainty (imu drift)

# dynamic world

- world is not static
- account for in models or ignore

summary

- sensor fusion for practical state estimation
- calibration for sensor model parameters
- speed and accuracy tradeoffs
- cope with failures
