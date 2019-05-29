#!/usr/bin/env python2.7

import socket
import pickle


HOST = '127.0.0.1'
PORT = 48124


class Client:
    """
    TCP client class to be able to connect to multiple servers
    Author: Alexis Remmers
    Date: 29/05/2019
    """

    

    def __init__(self, server_host=None, port=None):
        """
        Class constructor
        :param server_host: Server IP adress
        :param port: Server port adress
        """
        
        assert server_host and port

        self.server = socket.socket()
        self.server.connect((server_host, port))

    # def send_string(self, msg):
    #     """
    #     Send a regular string to server
    #     """
    #     self.server.send(msg.encode('utf-8'))

    def send_vector(self, vector):
        """
        Send a vector to server
        Example:
        servers.send_vector([32, 1, 1.42, 0. , 0.5])
        """
        data = pickle.dumps(vector)
        self.server.send(data.encode('utf-8'))

    def wait_for_reply(self):
        """
        Recieve message from server
        This will halt thread until message is recieved
        """
        data = self.server.recv(1024).decode('utf-8')
        print 'Received from server:', data

        return data

    def close(self):
        """
        Close the connection
        """
        self.server.close()




# Change these parts according to what you need

import random

# just a list of all emotions
TEST_EMOTION = [[1.0, 0. , 0.5, 0.1, 0.1, 0. ],
     [0.1, 1.2, 0.3, 0.0, 0.1, 0. ],
     [0.1, 0.2, 1.1, 0.1, 0. , 0.2],
     [0.1, 0.2, 0.1, 1.0, 0.0, 0.1],
     [0.1, 0.2, 0.2, 0.1, 1. , 0.2],
     [0.1, 0.1, 0.3, 0.1, 0. , 1.2]]


def client():


    server_conn = Client(socket.gethostname(), PORT)   # fetching local machine name
    
    # raw_input expects input directly from terminal change for your implementation
    # uses this just to manually insert data at different timeframes
    message = raw_input('-> ')
    index = 0
    test_length = 6

    # quit connection at sometime can be nice
    while message != 'q':
        
        server_conn.send_vector(TEST_EMOTION[index % test_length])

        index += 1
        
        message = raw_input('-> ')
    server_conn.close()

if __name__ == '__main__':
    client()