import logging
import RPi.GPIO
import signal
import time
import threading
import tornado.ioloop
import tornado.web

import db
import log
import robot


server_istance = None
robot_istance = None


class RobotForward(tornado.web.RequestHandler):
    def get(self):
        robot_istance.forward()


class RobotBackward(tornado.web.RequestHandler):
    def get(self):
        robot_istance.backward()


class RobotLeft(tornado.web.RequestHandler):
    def get(self):
        robot_istance.left()


class RobotRight(tornado.web.RequestHandler):
    def get(self):
        robot_istance.right()


class RobotStop(tornado.web.RequestHandler):
    def get(self):
        robot_istance.stop()


class RobotReset(tornado.web.RequestHandler):
    def get(self):
        robot_istance.reset()


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
    RPi.GPIO.setmode(RPi.GPIO.BCM)


def run_http_server():
    global server_istance

    logging.info("Starting HTTP on port 8000")

    server_istance = tornado.httpserver.HTTPServer(make_app())
    server_istance.listen(8000)

    tornado.ioloop.IOLoop.current().start()


def robot_worker():
    global robot_istance

    robot_istance = robot.Robot()
    robot_update = robot_istance.update()

    while True:
        robot_values = next(robot_update)

        logging.info(robot_values)

        # db.db.telemetry.insert(robot_values)

        time.sleep(0.5)


def run_robot():
    global robot_istance

    logging.info("Starting robot")

    t = threading.Thread(target=robot_worker)
    t.start()


if __name__ == "__main__":
    try:
        setup_signals()
        setup_board()

        run_robot()
        run_http_server()
    finally:
        GPIO.cleanup()
