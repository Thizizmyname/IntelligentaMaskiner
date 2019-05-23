#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionHappiness(EmotionResponse):
    """
    Subclass of EmotionResponse for generating a happiness expression on robot
    Author: Adam Ross & Alexis Remmers
    Date: 23/05/2019
    """

    def __init__(self, address, port):
        """
        Class constructor
        :param address: the IP address for connecting to the NAO Robot software
        :param port: the port number for connecting to the NAO Robot software
        """
        EmotionResponse.__init__(self, address, port)

    def generate_emotion(self):
        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.24, 0.52, 1, 1.52, 1.96])
        keys.append([-0.671952, -0.0244346, -0.502655, -0.195477, -0.439823])

        names.append("HeadYaw")
        times.append([0.24, 1.96])
        keys.append([-0.016916, -0.016916])

        names.append("LAnklePitch")
        times.append([0.52, 1.96])
        keys.append([-0.142704, -0.182588])

        names.append("LAnkleRoll")
        times.append([0.52, 1.96])
        keys.append([-0.110406, -0.110406])

        names.append("LElbowRoll")
        times.append([0.36, 0.68, 1.16, 1.64, 2.12])
        keys.append([-1.49226, -1.50021, -1.30027, -1.50021, -1.30027])

        names.append("LElbowYaw")
        times.append([0.68, 1.64])
        keys.append([-1.42053, -1.42053])

        names.append("LHand")
        times.append([0.36, 0.68, 1.16, 1.64, 2.12])
        keys.append([0.63, 0.27, 0, 0.26, 0])

        names.append("LHipPitch")
        times.append([0.52, 1.96])
        keys.append([-0.489305, -0.665714])

        names.append("LHipRoll")
        times.append([0.52, 1.96])
        keys.append([0.075208, 0.075208])

        names.append("LHipYawPitch")
        times.append([0.52, 1.96])
        keys.append([-0.205514, -0.226991])

        names.append("LKneePitch")
        times.append([0.52, 1.96])
        keys.append([0.645772, 0.819114])

        names.append("LShoulderPitch")
        times.append([0.28, 0.92, 1.4, 1.88, 2.04])
        keys.append([0.945968, 1.15541, 1.21475, 1.15541, 1.21475])

        names.append("LShoulderRoll")
        times.append([0.28, 0.92, 1.88])
        keys.append([0.223402, -0.11049, -0.11049])

        names.append("LWristYaw")
        times.append([0.36, 0.68, 1.64])
        keys.append([-0.630064, 0.101202, 0.101202])

        names.append("RAnklePitch")
        times.append([0.52, 1.96])
        keys.append([-0.187106, -0.233125])

        names.append("RAnkleRoll")
        times.append([0.52, 1.96])
        keys.append([0.124296, 0.124296])

        names.append("RElbowRoll")
        times.append([0.36, 0.56, 1.04, 1.52, 2])
        keys.append([1.49226, 1.48649, 1.30027, 1.48649, 1.30027])

        names.append("RElbowYaw")
        times.append([0.56, 1.52])
        keys.append([1.33914, 1.33914])

        names.append("RHand")
        times.append([0.36, 0.56, 1.04, 1.52, 2])
        keys.append([0.63, 0.27, 0, 0.26, 0])

        names.append("RHipPitch")
        times.append([0.52, 1.96])
        keys.append([-0.48632, -0.665798])

        names.append("RHipRoll")
        times.append([0.52, 1.96])
        keys.append([-0.075124, -0.0643861])

        names.append("RHipYawPitch")
        times.append([0.52, 1.96])
        keys.append([-0.205514, -0.226991])

        names.append("RKneePitch")
        times.append([0.52, 1.96])
        keys.append([0.664264, 0.843741])

        names.append("RShoulderPitch")
        times.append([0.28, 0.48, 0.8, 1.28, 1.76])
        keys.append([0.945968, 1.15541, 1.15541, 1.21475, 1.15541])

        names.append("RShoulderRoll")
        times.append([0.28, 0.48, 0.8, 1.76])
        keys.append([-0.223402, 0.075124, 0.075124, 0.075124])

        names.append("RWristYaw")
        times.append([0.36, 0.56, 1.52])
        keys.append([0.630064, 0.110406, 0.110406])

        self.sessions[self.POSTURE].goToPosture("StandInit", 0.5)
        self.sessions[self.MOTION].angleInterpolation(names, keys, times, True)
