## Calibration

sensor fusion is impossible without calibration
3 main types

- intrinsic - sensor specific
- extrinsic - position and orientation
- temporal - time offsets

### intrinsic

wheel speed
v = omega \* R

- omega = rotation rate
- R = radius

lidar

- elevation

- manufacturers specs
- measure by hand
- estimate as part of state on the fly or with a calibration step

### extrinsic

- determine relative poses of all sensors
- {C,r}
- cad model
- measure
- estimate as part of state

### temporal

- relative time delays of sensors
- timestamp when received
- assume 0 delay
- hardware timing signal
- estimate as part of state (complicated)
