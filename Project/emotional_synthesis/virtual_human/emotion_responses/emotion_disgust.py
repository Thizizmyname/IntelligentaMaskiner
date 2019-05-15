#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionDisgust(EmotionResponse):
    """
    Subclass of EmotionResponse for generating a disgust virtual emotion
    Author: Adam Ross
    Date: 15/05/2019
    """

    DISGUST = "emotion_disgust\n"
    UTTERANCE = "eehhh\n"
    GAZE = None

    def __init__(self, vh_conn):
        """
        Class constructor
        :param vh_conn: the IrisTk Virtual Human socket connection
        """
        EmotionResponse.__init__(self, vh_conn, self.DISGUST, self.GAZE,
                                 self.UTTERANCE)
