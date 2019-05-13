#!/usr/bin/env python

# Choregraphe simplified export in Python.

from naoqi import ALProxy
import emotion


def main(robotIP, port):
    try:

        motion = ALProxy("ALMotion", robotIP, port)
        posture_proxy = ALProxy("ALRobotPosture", robotIP, port)

        # Recomend to send robot to inital stand
        # posture before any emotion
        posture_proxy.goToPosture("Stand", 0.5)

        names, keys, times = emotion.happy()
        motion.angleInterpolation(names, keys, times, True)




        posture_proxy.goToPosture("Stand", 0.5)


        names, keys, times = emotion.suprised()
        motion.angleInterpolation(names, keys, times, True)


    except BaseException, err:
        print err


if __name__ == "__main__":
    main("localhost", 45845)
