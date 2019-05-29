#!/usr/bin/env python

import socket
import pickle
# from time import sleep
import threading

SERVER_PORT = 48124


# Change these parts according to what you need
import pipeline

APP = pipeline.Pipeline(43879)
PAUSE = False

def threaded_task(data):
    global PAUSE, APP
    
    APP.emotional_synthesis_single(data)
    print('Ready')
    PAUSE = False



def server():
    global PAUSE
    host = socket.gethostname()   # get local machine name
    port = SERVER_PORT  # Make sure it's within the > 1024 $$ <65535 range

    s = socket.socket()
    print 'Server starting up on:', socket.gethostbyname(host), 'with port:', port
    s.bind((host, port))

    s.listen(1)
    c, adress = s.accept()
    print("Connection from: " + str(adress))

    



    while True:
        # print('Ready for new emotion!')
        data = c.recv(1024).decode('utf-8')

        if not data:
            break
        # print('From online user: ' + str(data))
        data = pickle.loads(data)


        # Run your task as a threaded task to ignore all incoming messages until the task is done.
        if not PAUSE:
            PAUSE = True
            task = threading.Thread(target=threaded_task, args=(data,))
            task.start()

        # Run the task and the socket will buffer all messages recieved and run them iteratively (dependent on recv bufsize)
        # threaded_task(data)
        

        # c.send('Ready for new messages!'.encode('utf-8'))
    c.close()

if __name__ == '__main__':
    server()

