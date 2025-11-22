import logging
import serial

import log


class Lidar:
    def __init__(self, port, baud_rate, timeout=1.0):
        log.call(self, port, baud_rate, timeout)

        self.serial = serial.Serial('/dev/ttyS0', 115200, timeout=1)
        self.serial.write(bytes(b'B'))
        self.serial.write(bytes(b'W'))
        self.serial.write(bytes(2))
        self.serial.write(bytes(0))
        self.serial.write(bytes(0))
        self.serial.write(bytes(0))
        self.serial.write(bytes(1))
        self.serial.write(bytes(6))

    def update(self):
        log.call(self)

        while True:
            yield {
                "distance": self.get()
            }

    def get(self):
        log.call(self)

        distance = 0

        while self.serial.in_waiting >= 9:
            if b'Y' == self.serial.read() and b'Y' == self.serial.read():
                distance_low = self.serial.read()
                distance_high = self.serial.read()
                distance = ord(distance_high) * 256 + ord(distance_low)

                for i in range(0, 5):
                    self.serial.read()

        return distance
