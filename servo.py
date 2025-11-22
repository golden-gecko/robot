import logging
import time
import wiringpi

import log


class Servo:
    def __init__(self, pin, clock, range, min, max):
        log.call(self, pin, clock, range, min, max)

        self.pin = pin
        self.min = min
        self.max = max

        self.step = 2
        self.interval = 0.1

        wiringpi.wiringPiSetupGpio()
        wiringpi.pinMode(self.pin, wiringpi.GPIO.PWM_OUTPUT)
        wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)
        wiringpi.pwmSetClock(clock)
        wiringpi.pwmSetRange(range)

    def update(self):
        log.call(self)

        while True:

            for i in range(self.min, self.max, self.step):
                # self.rotate(i)
                time.sleep(self.interval)

                yield {
                    "angle": i
                }

            for i in range(self.max - self.step, self.min + self.step, -self.step):
                # self.rotate(i)
                time.sleep(self.interval)

                yield {
                    "angle": i
                }

    def rotate(self, pulse):
        log.call(self, pulse)

        if pulse < self.min:
            pulse = self.min
        elif pulse > self.max:
            pulse = self.max

        wiringpi.pwmWrite(self.pin, pulse)
