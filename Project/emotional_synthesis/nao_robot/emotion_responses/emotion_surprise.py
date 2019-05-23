#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionSurprise(EmotionResponse):
    """
    Subclass of EmotionResponse for generating a surprise expression on robot
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
        """
        Sends instructions to NAO Robot for emotional body language responses
        """

        names = list()
        times = list()
        keys = list()

        names.append("HeadPitch")
        times.append([0.24, 0.44, 1.12, 1.28, 1.52, 1.6, 1.88, 2.36, 5.32])
        keys.append([[-0.481711, [3, -0.08, 0], [3, 0.0666667, 0]],
                     [-0.109956, [3, -0.0666667, 0], [3, 0.226667, 0]],
                     [-0.109956, [3, -0.226667, 0], [3, 0.0533333, 0]],
                     [-0.0907571, [3, -0.0533333, 0], [3, 0.08, 0]],
                     [-0.0907571, [3, -0.08, 0], [3, 0.0266667, 0]],
                     [-0.0855211, [3, -0.0266667, 0], [3, 0.0933333, 0]],
                     [-0.0855211, [3, -0.0933333, 0], [3, 0.16, 0]],
                     [-0.109956, [3, -0.16, 0], [3, 0.986667, 0]],
                     [0.000321877, [3, -0.986667, 0], [3, 0, 0]]])

        names.append("HeadYaw")
        times.append([0.24, 1.12, 1.28, 1.52, 1.6, 1.88, 2.36, 5.32])
        keys.append([[0, [3, -0.08, 0], [3, 0.293333, 0]],
                     [0.0488692, [3, -0.293333, -0.0488692],
                      [3, 0.0533333, 0.00888531]],
                     [0.307178, [3, -0.0533333, 0], [3, 0.08, 0]],
                     [0.307178, [3, -0.08, 0], [3, 0.0266667, 0]],
                     [-0.274017, [3, -0.0266667, 0], [3, 0.0933333, 0]],
                     [-0.274017, [3, -0.0933333, 0], [3, 0.16, 0]],
                     [0.0488692, [3, -0.16, 0], [3, 0.986667, 0]],
                     [0.00110706, [3, -0.986667, 0], [3, 0, 0]]])

        names.append("LAnklePitch")
        times.append([0.36, 2.72, 3.12, 5.32])
        keys.append([[-0.551524, [3, -0.12, 0], [3, 0.786667, 0]],
                     [-0.551524, [3, -0.786667, 0], [3, 0.133333, 0]],
                     [-0.551524, [3, -0.133333, 0], [3, 0.733333, 0]],
                     [-0.341283, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([5.32])
        keys.append([[0, [3, -1.77333, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([0.28, 5.32])
        keys.append([[-1.47707, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [-1.00383, [3, -1.68, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.28, 5.32])
        keys.append([[-2.07638, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [-1.38683, [3, -1.68, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.28, 5.32])
        keys.append([[0.8, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [0.251043, [3, -1.68, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.36, 2.72, 3.12, 5.32])
        keys.append([[-0.0959931, [3, -0.12, 0], [3, 0.786667, 0]],
                     [-0.0959931, [3, -0.786667, 0], [3, 0.133333, 0]],
                     [-0.207694, [3, -0.133333, 0.0179241],
                      [3, 0.733333, -0.0985825]],
                     [-0.445513, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([5.32])
        keys.append([[0, [3, -1.77333, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([5.32])
        keys.append([[0, [3, -1.77333, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.36, 2.72, 3.12, 5.32])
        keys.append([[0.825541, [3, -0.12, 0], [3, 0.786667, 0]],
                     [0.825541, [3, -0.786667, 0], [3, 0.133333, 0]],
                     [0.825541, [3, -0.133333, 0], [3, 0.733333, 0]],
                     [0.693018, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.28, 0.72, 2.04, 5.32])
        keys.append([[0.00526988, [3, -0.0933333, 0], [3, 0.146667, 0]],
                     [0.0116059, [3, -0.146667, 0], [3, 0.44, 0]],
                     [0.0116059, [3, -0.44, 0], [3, 1.09333, 0]],
                     [1.39961, [3, -1.09333, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.28, 5.32])
        keys.append([[0.581959, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [0.296865, [3, -1.68, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.28, 5.32])
        keys.append([[0.238066, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [0.00246784, [3, -1.68, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.36, 2.72, 3.12, 5.32])
        keys.append([[-0.551524, [3, -0.12, 0], [3, 0.786667, 0]],
                     [-0.551524, [3, -0.786667, 0], [3, 0.133333, 0]],
                     [-0.551524, [3, -0.133333, 0], [3, 0.733333, 0]],
                     [-0.341283, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([5.32])
        keys.append([[0, [3, -1.77333, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.28, 5.32])
        keys.append([[1.47707, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [1.01811, [3, -1.68, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.28, 5.32])
        keys.append([[2.07638, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [1.38746, [3, -1.68, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.28, 5.32])
        keys.append([[0.8, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [0.251048, [3, -1.68, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.36, 2.72, 3.12, 5.32])
        keys.append([[-0.0959931, [3, -0.12, 0], [3, 0.786667, 0]],
                     [-0.0959931, [3, -0.786667, 0], [3, 0.133333, 0]],
                     [-0.207694, [3, -0.133333, 0.0179241],
                      [3, 0.733333, -0.0985825]],
                     [-0.445513, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([5.32])
        keys.append([[0, [3, -1.77333, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([5.32])
        keys.append([[0, [3, -1.77333, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.36, 2.72, 3.12, 5.32])
        keys.append([[0.825541, [3, -0.12, 0], [3, 0.786667, 0]],
                     [0.825541, [3, -0.786667, 0], [3, 0.133333, 0]],
                     [0.825541, [3, -0.133333, 0], [3, 0.733333, 0]],
                     [0.693018, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.28, 0.72, 2.04, 5.32])
        keys.append([[0.00526988, [3, -0.0933333, 0], [3, 0.146667, 0]],
                     [0.0116059, [3, -0.146667, 0], [3, 0.44, 0]],
                     [0.0116059, [3, -0.44, 0], [3, 1.09333, 0]],
                     [1.39961, [3, -1.09333, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.28, 5.32])
        keys.append([[-0.581959, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [-0.297544, [3, -1.68, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.28, 5.32])
        keys.append([[-0.238066, [3, -0.0933333, 0], [3, 1.68, 0]],
                     [-0.00994626, [3, -1.68, 0], [3, 0, 0]]])

        self.sessions[self.POSTURE].goToPosture("StandInit", 0.5)
        self.sessions[self.MOTION].angleInterpolationBezier(names, times, keys)
