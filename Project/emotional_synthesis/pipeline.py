#!/usr/bin/env python2.7

from sys import argv
from time import sleep
from nao_robot.nao_robot import NaoRobot
from virtual_human.virtual_human import VirtualHuman


class Pipeline:
    """
    Pipeline class for the Emotional Synthesis project
    Author: Adam Ross
    Date: 15/05/2019
    """

    ADDRESS = "127.0.0.1"  # Local host IP address
    PORT_NAO = 9959  # the port for connecting to the NAO robot
    PORT_VH = 1337  # the port for connecting to the Virtual Human
    EMOTIONS = {"happiness": "happiness",
                "sadness": "sadness",
                "anger": "anger",
                "fear": "fear",
                "disgust": "disgust",
                "surprise": "surprise"}  # mapping of input and output emotions
    SLEEP_TIME = 5
    PATH = "data/"

    def __init__(self):
        """
        Class constructor
        """
        try:
            self.nao_robot = NaoRobot(self.ADDRESS, self.PORT_NAO)
        except Exception:
            pass

        try:
            self.virtual_human = VirtualHuman(self.ADDRESS, self.PORT_VH)
        except Exception:
            pass

    def generate_emotion(self, emotion):
        """
        Generates virtual displays of an emotional response to an input emotion
        :param emotion: the emotion being generated for displaying
        """
        print "Currently displaying emotion:", emotion.upper()
        try:
            self.virtual_human.display_emotion(emotion)
        except Exception:
            pass

        try:
            self.nao_robot.display_emotion(emotion)
        except Exception:
            pass

    def emotional_synthesis(self, emotions, emotions_data):
        """
        Synthesises an appropriate emotional response to input emotion data
        :param emotions: the six basic emotions corresponding to data columns
        :param emotions_data: list(s) of floats representing emotion probability
        """
        for emotion_data in emotions_data:
            self.generate_emotion(self.EMOTIONS[emotions[emotion_data.
                                  index(max(emotion_data))].lower()])
            sleep(self.SLEEP_TIME)

    def read_file(self, file_name):
        """
        Extracts imput emotion probability data from a provided file
        :param file_name: name of file with input emotion probability data
        """
        data = [[eval(j) for j in i.split("[", 1)[-1].strip(" []\n").split(" ")
                 if len(j)] for i in open(self.PATH + file_name).readlines()]
        self.emotional_synthesis(data[0], data[1:])

    def demonstration(self):
        """
        Demonstrates each of the generated six basic human emotional responses
        """
        for emotion in self.EMOTIONS.keys():
            self.generate_emotion(emotion)
            sleep(self.SLEEP_TIME)

    def terminal_input(self):
        """
        Gets user input from terminal for displaying an emotional response
        """
        while True:
            command = raw_input("Enter one of the six basic emotions:\n")

            if command.lower() == "close":
                break
            elif command.lower() == "demo":
                self.demonstration()
            elif command.lower() in self.EMOTIONS.keys():
                self.generate_emotion(self.EMOTIONS[command.lower()])

    def close(self):
        """
        Closes all resources
        """
        try:
            self.virtual_human.disconnect()
        except Exception:
            pass


if __name__ == "__main__":
    app = Pipeline()

    if "-f" in argv and len(argv) > 2:
        app.read_file(argv[2])
    elif "-f" in argv:
        print "Error! To run file, enter: python pipeline.py -f <file>"
    elif "-d" in argv:
        app.demonstration()
    else:
        app.terminal_input()
    app.close()
