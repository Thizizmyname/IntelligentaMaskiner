#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionAnger(EmotionResponse):
    """
    Subclass of EmotionResponse for generating an anger expression on robot
    Author: Adam Ross & Alexis Remmers
    Date: 08/05/2019
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
        times.append([1.2, 2])
        keys.append([[-0.00420227, [3, -0.4, 0], [3, 0.266667, 0]], [-0.218166, [3, -0.266667, 0], [3, 0, 0]]])

        names.append("HeadYaw")
        times.append([1.2, 2])
        keys.append([[0.986111, [3, -0.4, 0], [3, 0.266667, 0]], [0.978469, [3, -0.266667, 0], [3, 0, 0]]])

        names.append("LAnklePitch")
        times.append([0.92, 2])
        keys.append([[-0.35, [3, -0.306667, 0], [3, 0.36, 0]], [-0.35, [3, -0.36, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([0.92, 2])
        keys.append([[0, [3, -0.306667, 0], [3, 0.36, 0]], [0, [3, -0.36, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([1.48, 2])
        keys.append([[-1.54462, [3, -0.493333, 0], [3, 0.173333, 0]], [-1.53668, [3, -0.173333, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([1.48, 2])
        keys.append([[-2.08567, [3, -0.493333, 0], [3, 0.173333, 0]], [-2.08235, [3, -0.173333, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([1.48, 2])
        keys.append([[0, [3, -0.493333, 0], [3, 0.173333, 0]], [0, [3, -0.173333, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.92, 1.12, 2])
        keys.append([[0.0349066, [3, -0.306667, 0], [3, 0.0666667, 0]], [0.0349066, [3, -0.0666667, 0], [3, 0.293333, 0]], [0.0349066, [3, -0.293333, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([0.92, 2])
        keys.append([[0.270526, [3, -0.306667, 0], [3, 0.36, 0]], [0.268565, [3, -0.36, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([0.92, 1.12, 2])
        keys.append([[-1.14494, [3, -0.306667, 0], [3, 0.0666667, 0]], [-1.14494, [3, -0.0666667, 0], [3, 0.293333, 0]], [-1.14494, [3, -0.293333, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.92, 2])
        keys.append([[0.7, [3, -0.306667, 0], [3, 0.36, 0]], [0.7, [3, -0.36, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([1.48, 2])
        keys.append([[1.028, [3, -0.493333, 0], [3, 0.173333, 0]], [1.03583, [3, -0.173333, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([1.48, 2])
        keys.append([[0.321141, [3, -0.493333, 0], [3, 0.173333, 0]], [0.317072, [3, -0.173333, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([1.48, 2])
        keys.append([[-0.607375, [3, -0.493333, 0], [3, 0.173333, 0]], [-0.610248, [3, -0.173333, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.92, 2])
        keys.append([[-0.35, [3, -0.306667, 0], [3, 0.36, 0]], [-0.35, [3, -0.36, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([0.92, 2])
        keys.append([[0, [3, -0.306667, 0], [3, 0.36, 0]], [0, [3, -0.36, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([1.4, 2])
        keys.append([[1.47965, [3, -0.466667, 0], [3, 0.2, 0]], [1.4499, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([1.4, 2])
        keys.append([[0.440977, [3, -0.466667, 0], [3, 0.2, 0]], [0.489829, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([1.4, 2])
        keys.append([[0, [3, -0.466667, 0], [3, 0.2, 0]], [0, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.92, 1.12, 2])
        keys.append([[0.185005, [3, -0.306667, 0], [3, 0.0666667, 0]], [0.185005, [3, -0.0666667, 0], [3, 0.293333, 0]], [0.185005, [3, -0.293333, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([0.92, 1.12, 2])
        keys.append([[-0.0331613, [3, -0.306667, 0], [3, 0.0666667, 0]], [-0.0331613, [3, -0.0666667, 0], [3, 0.293333, 0]], [-0.0248305, [3, -0.293333, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([0.92, 2])
        keys.append([[-1.14494, [3, -0.306667, 0], [3, 0.36, 0]], [-1.14494, [3, -0.36, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.92, 2])
        keys.append([[0.7, [3, -0.306667, 0], [3, 0.36, 0]], [0.7, [3, -0.36, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([1.4, 2])
        keys.append([[1.23596, [3, -0.466667, 0], [3, 0.2, 0]], [1.18011, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([1.4, 2])
        keys.append([[-0.096008, [3, -0.466667, 0], [3, 0.2, 0]], [-0.160072, [3, -0.2, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([1.4, 2])
        keys.append([[0.00525523, [3, -0.466667, 0], [3, 0.2, 0]], [0.00525523, [3, -0.2, 0], [3, 0, 0]]])

        self.sessions[self.POSTURE].goToPosture("StandInit", 0.5)
        self.sessions[self.MOTION].angleInterpolationBezier(names, times, keys)
