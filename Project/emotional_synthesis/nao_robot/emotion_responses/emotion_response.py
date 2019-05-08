#!/usr/bin/env python2.7

from naoqi import ALProxy


class EmotionResponse:
    """
    Superclass for generating NAO Robot emotion body language response displays
    Author: Adam Ross
    Date: 08/05/2019
    """

    MOTION = "ALMotion"
    POSTURE = "ALRobotPosture"

    def __init__(self, address, port):
        """
        Class constructor
        :param address: the IP address for connecting to the NAO Robot software
        :param port: the port number for connecting to the NAO Robot software
        """
        self.sessions = {self.MOTION: ALProxy(self.MOTION, address, port),
                         self.POSTURE: ALProxy(self.POSTURE, address, port)}

    def generate_emotion(self):
        """
        Sends instructions to NAO Robot for emotional body language responses
        """
        pass
