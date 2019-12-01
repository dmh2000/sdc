#!/usr/bin/env python3

"""
2D Controller Class to be used for the CARLA waypoint follower demo.
"""

import cutils
import numpy as np


class Controller2D(object):
    def __init__(self, waypoints):
        self.vars = cutils.CUtils()
        self._current_x = 0
        self._current_y = 0
        self._current_yaw = 0
        self._current_speed = 0
        self._desired_speed = 0
        self._current_frame = 0
        self._current_timestamp = 0
        self._start_control_loop = False
        self._set_throttle = 0
        self._set_brake = 0
        self._set_steer = 0
        self._waypoints = waypoints
        self._conv_rad_to_steer = 180.0 / 70.0 / np.pi
        self._pi = np.pi
        self._2pi = 2.0 * np.pi

    def update_values(self, x, y, yaw, speed, timestamp, frame):
        self._current_x = x
        self._current_y = y
        self._current_yaw = yaw
        self._current_speed = speed
        self._current_timestamp = timestamp
        self._current_frame = frame
        if self._current_frame:
            self._start_control_loop = True

    def update_desired_speed(self):
        min_idx = 0
        min_dist = float("inf")
        desired_speed = 0
        for i in range(len(self._waypoints)):
            dist = np.linalg.norm(np.array([
                self._waypoints[i][0] - self._current_x,
                self._waypoints[i][1] - self._current_y]))
            if dist < min_dist:
                min_dist = dist
                min_idx = i
        if min_idx < len(self._waypoints)-1:
            desired_speed = self._waypoints[min_idx][2]
        else:
            desired_speed = self._waypoints[-1][2]
        self._desired_speed = desired_speed

    def update_waypoints(self, new_waypoints):
        self._waypoints = new_waypoints

    def get_commands(self):
        return self._set_throttle, self._set_steer, self._set_brake

    def set_throttle(self, input_throttle):
        # Clamp the throttle command to valid bounds
        throttle = np.fmax(np.fmin(input_throttle, 1.0), 0.0)
        self._set_throttle = throttle

    def set_steer(self, input_steer_in_rad):
        # Covnert radians to [-1, 1]
        input_steer = self._conv_rad_to_steer * input_steer_in_rad

        # Clamp the steering command to valid bounds
        steer = np.fmax(np.fmin(input_steer, 1.0), -1.0)
        self._set_steer = steer

    def set_brake(self, input_brake):
        # Clamp the steering command to valid bounds
        brake = np.fmax(np.fmin(input_brake, 1.0), 0.0)
        self._set_brake = brake

    def update_controls(self):
        ######################################################
        # RETRIEVE SIMULATOR FEEDBACK
        ######################################################
        x = self._current_x
        y = self._current_y
        yaw = self._current_yaw
        v = self._current_speed
        self.update_desired_speed()
        v_desired = self._desired_speed
        t = self._current_timestamp
        waypoints = self._waypoints
        throttle_output = 0
        steer_output = 0
        brake_output = 0

        ######################################################
        ######################################################
        # MODULE 7: DECLARE USAGE VARIABLES HERE
        ######################################################
        ######################################################
        """
            Use 'self.vars.create_var(<variable name>, <default value>)'
            to create a persistent variable (not destroyed at each iteration).
            This means that the value can be stored for use in the next
            iteration of the control loop.

            Example: Creation of 'v_previous', default value to be 0
            self.vars.create_var('v_previous', 0.0)

            Example: Setting 'v_previous' to be 1.0
            self.vars.v_previous = 1.0

            Example: Accessing the value from 'v_previous' to be used
            throttle_output = 0.5 * self.vars.v_previous
        """
        self.vars.create_var('n', 0)        # current iteration
        self.vars.create_var('t_1', 0.0)    # previous timestamp
        self.vars.create_var('v_1', 0.0)    # previous velocity
        self.vars.create_var('x_1', 0.0)    # previous x coordinate
        self.vars.create_var('y_1', 0.0)    # previous y coordinate
        self.vars.create_var('yaw_1', 0.0)  # previous yaw coordinate
        self.vars.create_var('Kp_v', 4.0)   # velocity proportional gain
        self.vars.create_var('Kd_v', 0.3)   # velocity derivative gain
        self.vars.create_var('Ki_v', 0.1)   # velocity integral gain
        self.vars.create_var('v_e_1', 0.0)  # previous velocity error
        self.vars.create_var('v_i', 0.0)    # velocity integral accumulator
        self.vars.create_var('v_i_limit', 0.2)  # integrator term limiter
        # scale factor acceleration to throttle command
        self.vars.create_var('K_throttle', 1.0)
        # filter value for desired velocity
        self.vars.create_var('alpha_v', 0.3)
        # accumulator for desired velocity filter
        self.vars.create_var('v_des_1', 0.0)

        # Skip the first frame to store previous values properly
        if self._start_control_loop:
            """
                Controller iteration code block.

                Controller Feedback Variables:
                    x               : Current X position (meters)
                    y               : Current Y position (meters)
                    yaw             : Current yaw pose (radians)
                    v               : Current forward speed (meters per second)
                    t               : Current time (seconds)
                    v_desired       : Current desired speed (meters per second)
                                      (Computed as the speed to track at the
                                      closest waypoint to the vehicle.)
                    waypoints       : Current waypoints to track
                                      (Includes speed to track at each x,y
                                      location.)
                                      Format: [[x0, y0, v0],
                                               [x1, y1, v1],
                                               ...
                                               [xn, yn, vn]]
                                      Example:
                                          waypoints[2][1]:
                                          Returns the 3rd waypoint's y position

                                          waypoints[5]:
                                          Returns [x5, y5, v5] (6th waypoint)

                Controller Output Variables:
                    throttle_output : Throttle output (0 to 1)
                    steer_output    : Steer output (-1.22 rad to 1.22 rad)
                    brake_output    : Brake output (0 to 1)
            """

            ######################################################
            ######################################################
            # MODULE 7: IMPLEMENTATION OF LONGITUDINAL CONTROLLER HERE
            ######################################################
            ######################################################
            """
                Implement a longitudinal controller here. Remember that you can
                access the persistent variables declared above here. For
                example, can treat self.vars.v_previous like a "global variable".
            """
            # compute sample time
            dt = t - self.vars.t_1

            # filter desired velocity to smooth out spikes when desired velocit changes
            if self.vars.n == 0:
                v_des = v_desired
            else:
                v_des = self.vars.v_des_1 + self.vars.alpha_v * \
                    (v_desired - self.vars.v_des_1)

            # velocity error
            v_e = v_des - v

            # integral term
            v_i = self.vars.v_i + v_e * dt
            i = self.vars.Ki_v * v_i
            # limit integrator term
            if (i > self.vars.v_i_limit):
                i = self.vars.v_i_limit
            elif (i < -self.vars.v_i_limit):
                i = -self.vars.v_i_limit

            # derivative term
            v_d = (v_e - self.vars.v_e_1) / dt

            # compute control command
            v_dot_cmd = \
                + self.vars.Kp_v * v_e \
                + i \
                + self.vars.Kd_v * v_d

            # save integrator
            self.vars.v_i = v_i
            # save previous error
            self.vars.v_e_1 = v_e
            # scale to throttle output
            throttle_output = v_dot_cmd * self.vars.K_throttle
            # no brake at this time
            brake_output = 0

            ######################################################
            ######################################################
            # MODULE 7: IMPLEMENTATION OF LATERAL CONTROLLER HERE
            ######################################################
            ######################################################
            """
                Implement a lateral controller here. Remember that you can
                access the persistent variables declared above here. For
                example, can treat self.vars.v_previous like a "global variable".
            """
            L = 1.5

            # find nearest waypoint on path
            min_dist = float("inf")
            idx = 0
            for i in range(len(waypoints)-2):
                dist = np.linalg.norm(np.array([
                    waypoints[i][0] - x,
                    waypoints[i][1] - y]))
                if dist < min_dist and i > 1:
                    min_dist = dist
                    idx = i

            # find direction of path
            # w0 = waypoints[idx-1]
            # w1 = waypoints[idx+0]
            # w2 = waypoints[idx+1]
            # theta_p = np.arctan2(w2[1]-w0[1], w2[0]-w0[0])

            w0 = waypoints[idx-1]
            w1 = waypoints[idx+0]
            w2 = waypoints[idx+1]
            theta_p = np.arctan2(w2[1]-w1[1], w2[0]-w1[0])

            # angle error
            theta_e = theta_p - yaw

            # cross track error
            # point to line solution
            # # numerator
            # a = np.abs(((w1[1]-w0[1]) * x) - ((w1[0]-w0[0]) * y) + (w1[0]*w0[1]) - (w1[1]*w0[0])            )
            # # denominator
            # b = np.sqrt((w1[1] - w0[1])**2 + (w1[0]-w0[0])**2)
            # e = a / b
            # simple point to waypoint solution
            e = np.sqrt((x - w1[0])**2 + (y - w1[1])**2)

            # cross track gain
            k = 0.038

            # cross track correction
            cta = np.arctan2(k * e, v)

            # steering angle with a little added gain
            delta = theta_e + cta

            # print(f"{idx:04}, {delta:8.4f}, {theta_e:8.4f}, {e:8.4f}, {cta:8.4f}")

           # Change the steer output with the lateral controller.
            steer_output = delta

            ######################################################
            # SET CONTROLS OUTPUT
            ######################################################
            self.set_throttle(throttle_output)  # in percent (0 to 1)
            self.set_steer(steer_output)        # in rad (-1.22 to 1.22)
            self.set_brake(brake_output)        # in percent (0 to 1)

        ######################################################
        ######################################################
        # MODULE 7: STORE OLD VALUES HERE (ADD MORE IF NECESSARY)
        ######################################################
        ######################################################
        """
            Use this block to store old values (for example, we can store the
            current x, y, and yaw values here using persistent variables for use
            in the next iteration)
        """
        self.vars.t_1 = t  # timestamp
        self.vars.v_1 = v  # Store forward speed to be used in next step
        self.vars.x_1 = x
        self.vars.y_1 = y
        self.vars.yaw_1 = yaw
        self.vars.v_i = v_i  # integrator
        self.vars.v_e_1 = v_e  # velocity error
        self.vars.v_des_1 = v_des  # filter accumulator
        self.vars.n = self.vars.n + 1  # iteration count
