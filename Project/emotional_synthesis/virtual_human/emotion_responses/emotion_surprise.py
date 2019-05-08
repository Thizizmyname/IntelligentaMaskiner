#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionSurprise(EmotionResponse):
    """
    Subclass of EmotionResponse for generating a surprise virtual emotion
    Author: Adam Ross
    Date: 08/05/2019
    """

    SURPRISE = "emotion_surprise\n"

    def __init__(self, vh_conn):
        """
        Class constructor
        :param vh_conn: the IrisTk Virtual Human socket connection
        """
        EmotionResponse.__init__(self, vh_conn, self.SURPRISE)
