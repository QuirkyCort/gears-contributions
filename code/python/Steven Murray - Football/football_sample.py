#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
radio = Radio()

gyro_sensor_in1 = GyroSensor(INPUT_1)
gps_sensor_in2 = GPSSensor(INPUT_2)

motorC = LargeMotor(OUTPUT_C) # Magnet
motorD = LargeMotor(OUTPUT_D) # Magnet

eye = ObjectTracker()

def chase(target):
    p = gps_sensor_in2.position
    theta2ball = math.degrees(math.atan2(target[1] - p[1], target[0] - p[0]))
    theta = -gyro_sensor_in1.angle
    theta_error = wrap(theta2ball -  theta)
    steering = -1 * theta_error
    wrapped_steering = max(min(100,steering),-100)
    steering_drive.on(wrapped_steering, 70)
    
def wrap(angle):
    while (angle > 180):
        angle -= 360
    while (angle < -180):
        angle += 360
    return angle
    
def turn_to(target):
    while (True):
        p = gps_sensor_in2.position
        theta = -gyro_sensor_in1.angle
        theta2target = math.degrees(math.atan2(target[1] - p[1], target[0] - p[0]))
        theta_error = wrap(theta2target -  theta)
        steering = -1 * theta_error
        wrapped_power = max(min(100,steering),-100)
        steering_drive.on(100, wrapped_power)
        if (abs(theta_error) < 2.0):
            steering_drive.off()
            break
    
while True:
    bp = eye.position('ball')
    p = gps_sensor_in2.position
    if math.sqrt((bp[0] - p[0])**2 + (bp[1] - p[1])**2) > 15:
        chase(bp)
    else:
        steering_drive.off()
        motorC.on(100)
        time.sleep(1.0)
        turn_to([235,0])
        time.sleep(0.5)
        motorC.on(-40)
        time.sleep(1.0)
        motorC.off()

