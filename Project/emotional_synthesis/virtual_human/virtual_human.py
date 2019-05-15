#!/usr/bin/env python2.7

from threading import Thread
from socket import socket, AF_INET, SOCK_STREAM

from emotion_responses.emotion_anger import EmotionAnger
from emotion_responses.emotion_disgust import EmotionDisgust
from emotion_responses.emotion_fear import EmotionFear
from emotion_responses.emotion_happiness import EmotionHappiness
from emotion_responses.emotion_sadness import EmotionSadness
from emotion_responses.emotion_surprise import EmotionSurprise


class VirtualHuman(Thread):
    """
    Virtual Human class - refactored from Lab 3 'Furnet' class
    Author: Adam Ross
    Date: 08/05/2019
    """

    BUFFER = 8192
    SLEEP_TIME = 0.02
    ENCODING = "UTF-8"
    END_MRK = '\n'

    def __init__(self, address, port):
        """
        Class constructor
        :param address: the IP address for connecting to the IrisTk software
        :param port: the port number for connecting to the IrisTk software
        """
        Thread.__init__(self)
        self.daemon = True
        self.conn = socket(AF_INET, SOCK_STREAM)
        self.connect(address, port)
        self.emotions = {'happiness': EmotionHappiness(self.conn),
                         'sadness': EmotionSadness(self.conn),
                         'anger': EmotionAnger(self.conn),
                         'fear': EmotionFear(self.conn),
                         'disgust': EmotionDisgust(self.conn),
                         'surprise': EmotionSurprise(self.conn)}

    def connect(self, address, port):
        """
        Connects to the IrisTk Virtual Human software
        :param address: the IP address for connecting to the IrisTk software
        :param port: the port number for connecting to the IrisTk software
        """
        try:
            self.conn.connect((address, port))
            self.start()
        except Exception as e:
            print "Could not connect to server:\n", e

    def display_emotion(self, emotion):
        """
        Displays a generated virtual emotional expression
        """
        self.emotions[emotion].generate_emotion()

    def disconnect(self):
        """
        Disconnect from the Virtual Human IrisTk Software
        """
        self.conn.close()
