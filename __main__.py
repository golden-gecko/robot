import logging
import RPi.GPIO as GPIO
import signal
import time
import tornado.ioloop
import tornado.web

from tornado.netutil import bind_sockets

import db
import log
import robot


server_istance = None
robot_istance = None


class RobotForward(tornado.web.RequestHandler):
    def get(self):
        robot.forward()


class RobotBackward(tornado.web.RequestHandler):
    def get(self):
        robot.backward()


class RobotLeft(tornado.web.RequestHandler):
    def get(self):
        robot.left()


class RobotRight(tornado.web.RequestHandler):
    def get(self):
        robot.right()


class RobotStop(tornado.web.RequestHandler):
    def get(self):
        robot.stop()


class RobotReset(tornado.web.RequestHandler):
    def get(self):
        robot.reset()


def make_app():
    return tornado.web.Application([
        ("/robot/forward", RobotForward),
        ("/robot/backward", RobotBackward),
        ("/robot/left", RobotLeft),
        ("/robot/right", RobotRight),
        ("/robot/stop", RobotStop),
        ("/robot/reset", RobotReset)
    ])


def signal_handler(sig, frame):
    server_istance.stop()


def setup_signals():
    signal.signal(signal.SIGINT, signal_handler)
    signal.signal(signal.SIGTERM, signal_handler)


def setup_board():
    GPIO.setmode(GPIO.BCM)


def run_http_server():
    global server_istance

    logging.info("Starting HTTP on port 8000")

    server_istance = tornado.httpserver.HTTPServer(make_app())
    server_istance.listen(8000)

    # tornado.ioloop.IOLoop.current().start()


def run_robot():
    global robot_istance

    logging.info("Starting robot")

    robot_istance = robot.Robot()
    robot_update = robot_istance.update()

    while True:
        values = next(robot_update)

        logging.info(values)

        # db.db.telemetry.insert(values)

        time.sleep(0.5)


if __name__ == "__main__":
    try:
        setup_signals()
        setup_board()

        run_http_server()
        run_robot()
    finally:
        GPIO.cleanup()
