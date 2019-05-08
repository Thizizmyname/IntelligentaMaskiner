#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionSurprise(EmotionResponse):
    """
    Subclass of EmotionResponse for generating a surprise expression on robot
    Author: Adam Ross
    Date: 08/05/2019
    """

    def __init__(self, address, port):
        """
        Class constructor
        :param address: the IP address for connecting to the NAO Robot software
        :param port: the port number for connecting to the NAO Robot software
        """
        EmotionResponse.__init__(self, address, port)
