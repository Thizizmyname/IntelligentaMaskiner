#!/usr/bin/env python2.7

from nao_robot.nao_robot import NaoRobot
from virtual_human.virtual_human import VirtualHuman


class Pipeline:
    """
    Pipeline class for the Emotional Synthesis project
    Author: Adam Ross
    Date: 08/05/2019
    """

    ADDRESS = "127.0.0.1"  # Local host IP address
    PORT_NAO = 52239  # the port for connecting to the NAO robot
    PORT_VH = 1337  # the port for connecting to the Virtual Human
    EMOTIONS = {"happiness": "happiness",
                "sadness": "sadness",
                "anger": "anger",
                "fear": "fear",
                "disgust": "disgust",
                "surprise": "surprise"}  # mapping of input and output emotions

    def __init__(self):
        """
        Class constructor
        """
        self.nao_robot = NaoRobot(self.ADDRESS, self.PORT_NAO)
        self.virtual_human = VirtualHuman(self.ADDRESS, self.PORT_VH)

    def generate_emotion(self, emotion):
        """
        Generates virtual displays of an emotional response to an input emotion
        :param emotion: the emotion being generated for displaying
        """
        self.virtual_human.display_emotion(emotion)
        self.nao_robot.display_emotion(emotion)

    def terminal_input(self):
        """
        Gets user input from terminal for displaying an emotional response
        """
        while True:
            command = raw_input("Enter one of the six basic emotions:\n")

            if command == "close":
                break
            elif command.lower() in self.EMOTIONS.keys():
                self.generate_emotion(self.EMOTIONS[command.lower()])

    def close(self):
        """
        Closes all resources
        """
        self.virtual_human.disconnect()


if __name__ == "__main__":
    app = Pipeline()
    app.terminal_input()
    app.close()
