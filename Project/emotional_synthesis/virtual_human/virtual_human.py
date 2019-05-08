#!/usr/bin/env python2.7

from sys import stdout
from time import sleep
from threading import Thread
from multiprocessing import Queue
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
        self.daemon, self.running, self.rcvd_queue = True, False, Queue()
        self.conn = socket(AF_INET, SOCK_STREAM)
        self.connect(address, port)
        self.emotions = {'happiness': EmotionHappiness(self.conn),
                         'sadness': EmotionSadness(self.conn),
                         'anger': EmotionAnger(self.conn),
                         'fear': EmotionFear(self.conn),
                         'disgust': EmotionDisgust(self.conn),
                         'surprise': EmotionSurprise(self.conn)}

    def run(self):
        """
        Overrides Thread run() method to receive acknowledgements from IrisTk
        """
        if self.running:
            msg_bfr = ''

            while self.running:
                msg_bfr += self.conn.recv(self.BUFFER).decode(self.ENCODING)

                while self.END_MRK in msg_bfr:
                    self.rcvd_queue.put(msg_bfr[:msg_bfr.find(self.END_MRK)])
                    msg_bfr = msg_bfr[msg_bfr.find(self.END_MRK) +
                                      len(self.END_MRK):]
                sleep(self.SLEEP_TIME)
            print "Ending input reader"

    def connect(self, address, port):
        """
        Connects to the IrisTk Virtual Human software
        :param address: the IP address for connecting to the IrisTk software
        :param port: the port number for connecting to the IrisTk software
        """
        try:
            self.conn.connect((address, port))
            self.running = True
            self.start()
        except Exception as e:
            print "Could not connect to server:\n", e

    def display_emotion(self, emotion):
        """
        Displays a generated virtual emotional expression
        """
        self.emotions[emotion].generate_emotion()
        print "Waiting for executed ack responses:", stdout.flush()

        while self.rcvd_queue.qsize() > 0:
            print "Received:", self.rcvd_queue.get()

    def disconnect(self):
        """
        Disconnect from the Virtual Human IrisTk Software
        """
        self.conn.close()
