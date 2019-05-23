#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionHappiness(EmotionResponse):
    """
    Subclass of EmotionResponse for generating a happiness virtual emotion
    Author: Adam Ross
    Date: 23/05/2019
    """

    HAPPINESS = "emotion_happiness\n"
    UTTERANCE = "he he he he he\n"
    GAZE = None

    def __init__(self, vh_conn):
        """
        Class constructor
        :param vh_conn: the IrisTk Virtual Human socket connection
        """
        EmotionResponse.__init__(self, vh_conn, self.HAPPINESS, self.GAZE,
                                 self.UTTERANCE)
