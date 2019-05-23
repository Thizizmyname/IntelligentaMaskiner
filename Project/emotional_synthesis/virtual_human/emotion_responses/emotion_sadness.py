#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionSadness(EmotionResponse):
    """
    Subclass of EmotionResponse for generating a sadness virtual emotion
    Author: Adam Ross
    Date: 23/05/2019
    """

    SADNESS = "emotion_sadness\n"
    UTTERANCE = "aoie aoie\n"
    GAZE = None

    def __init__(self, vh_conn):
        """
        Class constructor
        :param vh_conn: the IrisTk Virtual Human socket connection
        """
        EmotionResponse.__init__(self, vh_conn, self.SADNESS, self.GAZE,
                                 self.UTTERANCE)
