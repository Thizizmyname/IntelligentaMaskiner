#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionFear(EmotionResponse):
    """
    Subclass of EmotionResponse for generating a fear expression on robot
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
        times.append([0.24, 1, 2.2, 2.56, 3.56, 5.32])
        keys.append([[0.230383, [3, -0.08, 0], [3, 0.253333, 0]],
                     [0.230383, [3, -0.253333, 0], [3, 0.4, 0]],
                     [-0.0541052, [3, -0.4, 0], [3, 0.12, 0]],
                     [0.230383, [3, -0.12, 0], [3, 0.333333, 0]],
                     [0.230383, [3, -0.333333, 0], [3, 0.586667, 0]],
                     [0.000321877, [3, -0.586667, 0], [3, 0, 0]]])

        names.append("HeadYaw")
        times.append([0.24, 1, 2.2, 2.56, 3.56, 5.32])
        keys.append([[0.792379, [3, -0.08, 0], [3, 0.253333, 0]],
                     [0.792379, [3, -0.253333, 0], [3, 0.4, 0]],
                     [0.371755, [3, -0.4, 0], [3, 0.12, 0]],
                     [0.792379, [3, -0.12, 0], [3, 0.333333, 0]],
                     [0.792379, [3, -0.333333, 0], [3, 0.586667, 0]],
                     [0.00110706, [3, -0.586667, 0], [3, 0, 0]]])

        names.append("LAnklePitch")
        times.append([0.4, 2.72, 3.12, 5.32])
        keys.append([[-0.551524, [3, -0.133333, 0], [3, 0.773333, 0]],
                     [-0.551524, [3, -0.773333, 0], [3, 0.133333, 0]],
                     [-0.551524, [3, -0.133333, 0], [3, 0.733333, 0]],
                     [-0.341283, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([5.32])
        keys.append([[0, [3, -1.77333, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([0.32, 1.04, 2.28, 2.6, 3.4, 5.32])
        keys.append([[-0.840615, [3, -0.106667, 0], [3, 0.24, 0]],
                     [-0.840615, [3, -0.24, 0], [3, 0.413333, 0]],
                     [-0.840615, [3, -0.413333, 0], [3, 0.106667, 0]],
                     [-0.840615, [3, -0.106667, 0], [3, 0.266667, 0]],
                     [-0.840615, [3, -0.266667, 0], [3, 0.64, 0]],
                     [-1.00383, [3, -0.64, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.32, 1.04, 2.28, 2.6, 3.4, 5.32])
        keys.append([[-0.361699, [3, -0.106667, 0], [3, 0.24, 0]],
                     [-0.361699, [3, -0.24, 0], [3, 0.413333, 0]],
                     [-0.361699, [3, -0.413333, 0], [3, 0.106667, 0]],
                     [-0.361699, [3, -0.106667, 0], [3, 0.266667, 0]],
                     [-0.361699, [3, -0.266667, 0], [3, 0.64, 0]],
                     [-1.38683, [3, -0.64, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.32, 1.04, 2.28, 2.6, 3.4, 5.32])
        keys.append([[0.996717, [3, -0.106667, 0], [3, 0.24, 0]],
                     [0.996717, [3, -0.24, 0], [3, 0.413333, 0]],
                     [0.996717, [3, -0.413333, 0], [3, 0.106667, 0]],
                     [0.996717, [3, -0.106667, 0], [3, 0.266667, 0]],
                     [0.996717, [3, -0.266667, 0], [3, 0.64, 0]],
                     [0.251043, [3, -0.64, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.4, 2.72, 3.12, 5.32])
        keys.append([[-0.0959931, [3, -0.133333, 0], [3, 0.773333, 0]],
                     [-0.0959931, [3, -0.773333, 0], [3, 0.133333, 0]],
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
        times.append([0.4, 2.72, 3.12, 5.32])
        keys.append([[0.825541, [3, -0.133333, 0], [3, 0.773333, 0]],
                     [0.825541, [3, -0.773333, 0], [3, 0.133333, 0]],
                     [0.825541, [3, -0.133333, 0], [3, 0.733333, 0]],
                     [0.693018, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.32, 1.04, 2.28, 2.6, 3.4, 5.32])
        keys.append([[-0.109795, [3, -0.106667, 0], [3, 0.24, 0]],
                     [-0.109795, [3, -0.24, 0], [3, 0.413333, 0]],
                     [0.181514, [3, -0.413333, 0], [3, 0.106667, 0]],
                     [-0.109795, [3, -0.106667, 0], [3, 0.266667, 0]],
                     [-0.109795, [3, -0.266667, 0], [3, 0.64, 0]],
                     [1.39961, [3, -0.64, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.32, 1.04, 2.28, 2.6, 3.4, 5.32])
        keys.append([[0.104254, [3, -0.106667, 0], [3, 0.24, 0]],
                     [0.104254, [3, -0.24, 0], [3, 0.413333, 0]],
                     [0.104254, [3, -0.413333, 0], [3, 0.106667, 0]],
                     [0.104254, [3, -0.106667, 0], [3, 0.266667, 0]],
                     [0.104254, [3, -0.266667, 0], [3, 0.64, 0]],
                     [0.296865, [3, -0.64, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.32, 1.04, 2.28, 2.6, 3.4, 5.32])
        keys.append([[1.82293, [3, -0.106667, 0], [3, 0.24, 0]],
                     [1.82293, [3, -0.24, 0], [3, 0.413333, 0]],
                     [1.82293, [3, -0.413333, 0], [3, 0.106667, 0]],
                     [1.82293, [3, -0.106667, 0], [3, 0.266667, 0]],
                     [1.82293, [3, -0.266667, 0], [3, 0.64, 0]],
                     [0.00246784, [3, -0.64, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.4, 2.72, 3.12, 5.32])
        keys.append([[-0.551524, [3, -0.133333, 0], [3, 0.773333, 0]],
                     [-0.551524, [3, -0.773333, 0], [3, 0.133333, 0]],
                     [-0.551524, [3, -0.133333, 0], [3, 0.733333, 0]],
                     [-0.341283, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([5.32])
        keys.append([[0, [3, -1.77333, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.2, 1.24, 2.36, 2.52, 3.32, 5.32])
        keys.append([[1.51666, [3, -0.0666667, 0], [3, 0.346667, 0]],
                     [1.51666, [3, -0.346667, 0], [3, 0.373333, 0]],
                     [1.51666, [3, -0.373333, 0], [3, 0.0533333, 0]],
                     [1.51666, [3, -0.0533333, 0], [3, 0.266667, 0]],
                     [1.51666, [3, -0.266667, 0], [3, 0.666667, 0]],
                     [1.01811, [3, -0.666667, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.2, 1.24, 2.36, 2.52, 3.32, 5.32])
        keys.append([[0.564982, [3, -0.0666667, 0], [3, 0.346667, 0]],
                     [0.564982, [3, -0.346667, 0], [3, 0.373333, 0]],
                     [0.564982, [3, -0.373333, 0], [3, 0.0533333, 0]],
                     [0.564982, [3, -0.0533333, 0], [3, 0.266667, 0]],
                     [0.564982, [3, -0.266667, 0], [3, 0.666667, 0]],
                     [1.38746, [3, -0.666667, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.2, 1.24, 2.36, 2.52, 3.32, 5.32])
        keys.append([[1, [3, -0.0666667, 0], [3, 0.346667, 0]],
                     [1, [3, -0.346667, 0], [3, 0.373333, 0]],
                     [1, [3, -0.373333, 0], [3, 0.0533333, 0]],
                     [1, [3, -0.0533333, 0], [3, 0.266667, 0]],
                     [1, [3, -0.266667, 0], [3, 0.666667, 0]],
                     [0.251048, [3, -0.666667, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.4, 2.72, 3.12, 5.32])
        keys.append([[-0.0959931, [3, -0.133333, 0], [3, 0.773333, 0]],
                     [-0.0959931, [3, -0.773333, 0], [3, 0.133333, 0]],
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
        times.append([0.4, 2.72, 3.12, 5.32])
        keys.append([[0.825541, [3, -0.133333, 0], [3, 0.773333, 0]],
                     [0.825541, [3, -0.773333, 0], [3, 0.133333, 0]],
                     [0.825541, [3, -0.133333, 0], [3, 0.733333, 0]],
                     [0.693018, [3, -0.733333, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.2, 1.24, 2.36, 2.52, 3.32, 5.32])
        keys.append([[-0.102217, [3, -0.0666667, 0], [3, 0.346667, 0]],
                     [-0.102217, [3, -0.346667, 0], [3, 0.373333, 0]],
                     [-0.102217, [3, -0.373333, 0], [3, 0.0533333, 0]],
                     [-0.102217, [3, -0.0533333, 0], [3, 0.266667, 0]],
                     [-0.102217, [3, -0.266667, 0], [3, 0.666667, 0]],
                     [1.39961, [3, -0.666667, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.2, 1.24, 2.36, 2.52, 3.32, 5.32])
        keys.append([[0.0541691, [3, -0.0666667, 0], [3, 0.346667, 0]],
                     [0.0541691, [3, -0.346667, 0], [3, 0.373333, 0]],
                     [-0.242601, [3, -0.373333, 0], [3, 0.0533333, 0]],
                     [0.0541691, [3, -0.0533333, 0], [3, 0.266667, 0]],
                     [0.0541691, [3, -0.266667, 0], [3, 0.666667, 0]],
                     [-0.297544, [3, -0.666667, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.2, 1.24, 2.36, 2.52, 3.32, 5.32])
        keys.append([[-1.41577, [3, -0.0666667, 0], [3, 0.346667, 0]],
                     [-1.41577, [3, -0.346667, 0], [3, 0.373333, 0]],
                     [-1.41577, [3, -0.373333, 0], [3, 0.0533333, 0]],
                     [-1.41577, [3, -0.0533333, 0], [3, 0.266667, 0]],
                     [-1.41577, [3, -0.266667, 0], [3, 0.666667, 0]],
                     [-0.00994626, [3, -0.666667, 0], [3, 0, 0]]])

        self.sessions[self.POSTURE].goToPosture("StandInit", 0.5)
        self.sessions[self.MOTION].angleInterpolationBezier(names, times, keys)