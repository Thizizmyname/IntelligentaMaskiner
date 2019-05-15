#!/usr/bin/env python2.7

from emotion_responses.emotion_happiness import EmotionHappiness
from emotion_responses.emotion_sadness import EmotionSadness
from emotion_responses.emotion_anger import EmotionAnger
from emotion_responses.emotion_disgust import EmotionDisgust
from emotion_responses.emotion_fear import EmotionFear
from emotion_responses.emotion_surprise import EmotionSurprise


class NaoRobot:
    """
    NAO Robot class
    Author: Adam Ross
    Date: 08/05/2019
    """

    def __init__(self, address, port):
        """
        Class constructor
        :param address: the IP address for connecting to the NAO Robot software
        :param port: the port number for connecting to the NAO Robot software
        """
        self.emotions = {'happiness': EmotionHappiness(address, port),
                         'sadness': EmotionSadness(address, port),
                         'anger': EmotionAnger(address, port),
                         'fear': EmotionFear(address, port),
                         'disgust': EmotionDisgust(address, port),
                         'surprise': EmotionSurprise(address, port)}

    def display_emotion(self, emotion):
        """
        Displays a generated NAO robot emotional body language expression
        """
        self.emotions[emotion].generate_emotion()
