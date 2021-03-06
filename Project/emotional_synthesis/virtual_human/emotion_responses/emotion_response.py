#!/usr/bin/env python2.7


class EmotionResponse:
    """
    Superclass for generating IrisTk Virtual Human emotional response displays
    Author: Adam Ross
    Date: 23/05/2019
    """

    GESTURE = "gesture:"
    SAY = "say:"
    GAZE = "gaze:"
    ENCODING = "UTF-8"
    RESET = "emotion_neutral\n"  # resets virtual human expression to neutral

    def __init__(self, vh_conn, gesture, gaze=None, utterance=None):
        """
        Class constructor
        :param vh_conn: the IrisTk Virtual Human socket connection
        :param gesture: the emotional of the virtual expression
        :param gaze: the gaze of the virtual expression
        :param utterance: the speech of the virtual expression
        """
        self.conn = vh_conn
        self.gesture = gesture
        self.gaze = gaze
        self.utterance = utterance
        self.reset_emotion()

    def generate_emotion(self):
        """
        Sends a message request to the virtual human for an emotional response
        """
        self.reset_emotion()

        if self.utterance:
            self.conn.sendall((self.SAY + self.utterance).encode(self.ENCODING))

            if len(self.utterance) > 10:
                self.conn.sendall((self.SAY + self.utterance).encode(self.ENCODING))
        self.conn.sendall((self.GESTURE + self.gesture).encode(self.ENCODING))

        if self.gaze:
            self.conn.sendall((self.GAZE + self.gaze).encode(self.ENCODING))

    def reset_emotion(self):
        """
        Resets the virtual human to display a neutral emotional expression
        """
        self.conn.sendall((self.GESTURE + self.RESET).encode(self.ENCODING))
