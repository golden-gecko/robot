import datetime
import logging

import compass
import lidar
import log
import servo
import wheel


class Robot:
    def __init__(self):
        log.call(self)

        self.compass = compass.Compass(port=1, declination=(5, 17))
        self.lidar = lidar.Lidar(port="/dev/ttyS0", baud_rate=115200)
        self.servo = servo.Servo(pin=18, clock=192, range=2000, min=52, max=132)
        self.wheel_left = wheel.Wheel(dir_pin=5, pwm_pin=12, encoder_pin=16)
        self.wheel_right = wheel.Wheel(dir_pin=6, pwm_pin=13, encoder_pin=21)

    def update(self):
        log.call(self)

        compass_update = self.compass.update()
        lidar_update = self.lidar.update()
        servo_update = self.servo.update()
        wheel_left_update = self.wheel_left.update()
        wheel_right_update = self.wheel_right.update()

        while True:
            compass_values = next(compass_update)
            lidar_values = next(lidar_update)
            servo_values = next(servo_update)
            wheel_left_values = next(wheel_left_update)
            wheel_right_values = next(wheel_right_update)

            yield {
                "compass": compass_values,
                "lidar": lidar_values,
                "servo": servo_values,
                "timestamp": str(datetime.datetime.utcnow()),
                "wheels": {
                    "left": wheel_left_values,
                    "right": wheel_right_values
                }
            }

    def forward(self):
        log.call(self)

        self.wheel_left.forward()
        self.wheel_right.forward()

    def backward(self):
        log.call(self)

        self.wheel_left.backward()
        self.wheel_right.backward()

    def left(self):
        log.call(self)

        self.wheel_left.backward()
        self.wheel_right.forward()

    def right(self):
        log.call(self)

        self.wheel_left.forward()
        self.wheel_right.backward()

    def stop(self):
        log.call(self)

        self.wheel_left.stop()
        self.wheel_right.stop()
