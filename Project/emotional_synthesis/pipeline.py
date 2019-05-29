#!/usr/bin/env python2.7

from sys import argv
from time import sleep
from collections import OrderedDict
from nao_robot.nao_robot import NaoRobot
from virtual_human.virtual_human import VirtualHuman


class Pipeline:
    """
    Pipeline class for the Emotional Synthesis project
    Author: Adam Ross & Alexis Remmers
    Date: 29/05/2019
    """

    ADDRESS = "127.0.0.1"  # Local host IP address
    PORT_NAO = 9559  # the fixed port for connecting to the NAO robot
    PORT_VH = 1337  # the fixed port for connecting to the Virtual Human
    SLEEP_TIME = 5
    DEMO = "demo"
    CLOSE = "close"
    PATH = "data/"
    EMOTIONS_MAP = OrderedDict([("anger", "fear"),
                                ("disgust", "sadness"),
                                ("fear", "happiness"),
                                ("happiness", "happiness"),
                                ("sadness", "sadness"),
                                ("surprise", "surprise")])  # map of emotions

    def __init__(self, port_nao=None):
        """
        Class constructor
        :param port_nao: the NAO robot app TCP connection port
        """
        if not port_nao:
            port_nao = self.PORT_NAO

        try:
            self.nao_robot = NaoRobot(self.ADDRESS, port_nao)
        except Exception as e:
            print "There was an error connecting to the NAO robot:", e
            pass

        try:
            self.virtual_human = VirtualHuman(self.ADDRESS, self.PORT_VH)
        except Exception as e:
            print "There was an error connecting to the virtual human:", e
            pass

    def generate_emotion(self, emotion):
        """
        Generates virtual displays of an emotional response to an input emotion
        :param emotion: the emotion being generated for displaying
        """
        print "Currently displaying emotion:", emotion.upper()

        try:
            self.virtual_human.display_emotion(emotion)
        except Exception as e:
            print "There was an error displaying the virtual human emotion:", e
            pass

        try:
            self.nao_robot.display_emotion(emotion)
        except Exception as e:
            print "There was an error displaying the NAO robot emotion:", e
            pass

    def emotional_synthesis(self, emotions_data):
        """
        Synthesises an emotional response from input emotion probability data
        :param emotions_data: lists of floats representing emotion probability
        """
        for emotion in emotions_data:
            try:
                input_emotion = self.EMOTIONS_MAP.keys()[emotion.
                                                         index(max(emotion))]
                print "Retrieved data representing: ", input_emotion.upper()
                self.generate_emotion(self.EMOTIONS_MAP[input_emotion])
            except Exception as e:
                print "There is an error in the input emotions data:", e
                self.close()
            sleep(self.SLEEP_TIME)

    def emotional_synthesis_single(self, emotion):
        """
        Synthesises an emotional response from input emotion probability data
        :param emotions_data: lists of floats representing emotion probability
        """
        try:
            input_emotion = self.EMOTIONS_MAP.keys()[emotion.
                                                     index(max(emotion))]
            print "Retrieved data representing:", input_emotion.upper()
            self.generate_emotion(self.EMOTIONS_MAP[input_emotion])

        except Exception as e:
            print "There is an error in the input emotions data:", e
            self.close()

    def read_file(self, file_name):
        """
        Extracts input emotion probability data from a provided file
        :param file_name: name of file with input emotion probability data
        """
        data = [[eval(j) for j in i.split("[", 1)[-1].strip(" []\n").split(" ")
                 if len(j)] for i in open(self.PATH + file_name).readlines()]
        self.emotional_synthesis(data[1:])

    def demonstration(self):
        """
        Demonstrates each of the generated six basic human emotional responses
        """
        for emotion in self.EMOTIONS_MAP.keys():
            self.generate_emotion(emotion)
            sleep(self.SLEEP_TIME)

    def terminal_input(self):
        """
        Gets user input from terminal for displaying an emotional response
        """
        while True:
            command = raw_input("Enter one of the six basic emotions:\n")

            if command.lower() == self.CLOSE:
                break
            elif command.lower() == self.DEMO:
                self.demonstration()
            elif command.lower() in self.EMOTIONS_MAP.keys():
                self.generate_emotion(self.EMOTIONS_MAP[command.lower()])

    def close(self):
        """
        Closes all resources
        """
        try:
            self.virtual_human.disconnect()
        except Exception as e:
            print "There was an error while attempting to close resources:", e
            pass


if __name__ == "__main__":
    if "-p" in argv:
        try:
            app = Pipeline(int(argv[2]))
        except Exception as ie:
            app = None
            print "Error: ", ie, \
                "\nTo use custom NAO port, enter: python pipeline.py -p [port]"
    else:
        app = Pipeline()

    if app and "-f" in argv and len(argv) > 2:
        try:
            app.read_file(argv[-1])
        except Exception as ie:
            print "Error: ", ie, \
                "\nTo run file, enter: python pipeline.py -f <file>"
    elif app and "-d" in argv:
        app.demonstration()
    elif app:
        app.terminal_input()

    if app:
        app.close()
