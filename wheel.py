import functools
import logging
import RPi.GPIO

import log


class Wheel:
    def __init__(self, dir_pin, pwm_pin, encoder_pin):
        log.call(self, dir_pin, pwm_pin, encoder_pin)

        self.dir_pin = dir_pin
        self.pwm_pin = pwm_pin
        self.encoder_pin = encoder_pin

        self.rotations = 0
        self.direction = 0

        RPi.GPIO.setup(self.dir_pin, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.pwm_pin, RPi.GPIO.OUT)
        RPi.GPIO.setup(self.encoder_pin, RPi.GPIO.IN)

        RPi.GPIO.add_event_detect(self.encoder_pin, RPi.GPIO.RISING, callback=self.encoder_callback)

    def update(self):
        while True:
            yield {
                "rotations": self.rotations
            }

    def forward(self):
        log.call(self)

        self.direction = 1

        RPi.GPIO.output(self.dir_pin, RPi.GPIO.HIGH)
        RPi.GPIO.output(self.pwm_pin, RPi.GPIO.HIGH)

    def backward(self):
        log.call(self)

        self.direction = -1

        RPi.GPIO.output(self.dir_pin, RPi.GPIO.LOW)
        RPi.GPIO.output(self.pwm_pin, RPi.GPIO.HIGH)

    def stop(self):
        log.call(self)

        self.direction = 0

        RPi.GPIO.output(self.dir_pin, RPi.GPIO.LOW)
        RPi.GPIO.output(self.pwm_pin, RPi.GPIO.LOW)

    def encoder_callback(self, pin):
        # log.call(self, pin)

        self.rotations = self.rotations + self.direction
