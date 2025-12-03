import i2clibraries.i2c_hmc5883l
import logging

import log


class Compass:
    def __init__(self, port, declination):
        log.call(self, port, declination)

        self.port = port
        self.declination = declination

    def update(self):
        log.call(self)

        while True:
            yield self.get()

    def get(self):
        # log.call(self)

        hmc5883l = i2clibraries.i2c_hmc5883l.i2c_hmc5883l(self.port)
        hmc5883l.setContinuousMode()
        hmc5883l.setDeclination(self.declination[0], self.declination[1])

        return hmc5883l.getAxes()
