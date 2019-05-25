#!/usr/bin/env python2.7

from emotion_response import EmotionResponse


class EmotionSadness(EmotionResponse):
    """
    Subclass of EmotionResponse for generating a sadness expression on robot
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
        times.append([0.6, 1, 2, 3.08, 4.4, 8.44, 11.44])
        keys.append([[0.363028, [3, -0.2, 0], [3, 0.133333, 0]],
                     [0.363028, [3, -0.133333, 0], [3, 0.333333, 0]],
                     [0.45204, [3, -0.333333, 0], [3, 0.36, 0]],
                     [0.45204, [3, -0.36, 0], [3, 0.44, 0]],
                     [0.419556, [3, -0.44, 0], [3, 1.34667, 0]],
                     [0.420087, [3, -1.34667, 0], [3, 1, 0]],
                     [0.00120356, [3, -1, 0], [3, 0, 0]]])

        names.append("HeadYaw")
        times.append([0.6, 1, 2, 3.08, 3.92, 4.84, 5.28, 5.8, 6.2,
                      6.64, 7.08, 8.44, 11.44])
        keys.append([[0.274017, [3, -0.2, 0], [3, 0.133333, 0]],
                     [0.274017, [3, -0.133333, 0], [3, 0.333333, 0]],
                     [-0.50091, [3, -0.333333, 0], [3, 0.36, 0]],
                     [-0.50091, [3, -0.36, 0], [3, 0.28, 0]],
                     [0, [3, -0.28, 0], [3, 0.306667, 0]],
                     [-0.174533, [3, -0.306667, 0], [3, 0.146667, 0]],
                     [0.174533, [3, -0.146667, 0], [3, 0.173333, 0]],
                     [-0.174533, [3, -0.173333, 0], [3, 0.133333, 0]],
                     [0.174533, [3, -0.133333, 0], [3, 0.146667, 0]],
                     [-0.174533, [3, -0.146667, 0], [3, 0.146667, 0]],
                     [0.174533, [3, -0.146667, 0], [3, 0.453333, 0]],
                     [0, [3, -0.453333, 0], [3, 1, 0]],
                     [0, [3, -1, 0], [3, 0, 0]]])

        names.append("LAnklePitch")
        times.append([0.4, 2.2, 4.08, 7.12, 8.44, 11.44])
        keys.append([[-0.355986, [3, -0.133333, 0], [3, 0.6, 0]],
                     [-0.411898, [3, -0.6, 0], [3, 0.626667, 0]],
                     [-0.40307, [3, -0.626667, -0.00778067],
                      [3, 1.01333, 0.0125815]],
                     [-0.350811, [3, -1.01333, 0], [3, 0.44, 0]],
                     [-0.353516, [3, -0.44, 0], [3, 1, 0]],
                     [-0.353516, [3, -1, 0], [3, 0, 0]]])

        names.append("LAnkleRoll")
        times.append([0.4, 2.2, 4.08, 8.44, 11.44])
        keys.append([[0, [3, -0.133333, 0], [3, 0.6, 0]],
                     [0, [3, -0.6, 0], [3, 0.626667, 0]],
                     [0, [3, -0.626667, 0], [3, 1.45333, 0]],
                     [0, [3, -1.45333, 0], [3, 1, 0]],
                     [0, [3, -1, 0], [3, 0, 0]]])

        names.append("LElbowRoll")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[-1.00209, [3, -0.133333, 0], [3, 0.44, 0]],
                     [-0.28536, [3, -0.44, 0], [3, 0.906667, 0]],
                     [-1.47306, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [-1.46896, [3, -1.33333, -0.00410153],
                      [3, 1, 0.00307615]],
                     [-1.01271, [3, -1, 0], [3, 0, 0]]])

        names.append("LElbowYaw")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[-1.39072, [3, -0.133333, 0], [3, 0.44, 0]],
                     [-1.39072, [3, -0.44, 0], [3, 0.906667, 0]],
                     [-0.947714, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [-0.960703, [3, -1.33333, 0.0129888],
                      [3, 1, -0.00974158]],
                     [-1.38743, [3, -1, 0], [3, 0, 0]]])

        names.append("LHand")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[0.249591, [3, -0.133333, 0], [3, 0.44, 0]],
                     [0.249591, [3, -0.44, 0], [3, 0.906667, 0]],
                     [1, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [0.999879, [3, -1.33333, 0.000120997],
                      [3, 1, -9.07481e-05]],
                     [0.252151, [3, -1, 0], [3, 0, 0]]])

        names.append("LHipPitch")
        times.append([0.4, 2.2, 4.08, 7.12, 8.44, 11.44])
        keys.append([[-0.458529, [3, -0.133333, 0], [3, 0.6, 0]],
                     [-0.95644, [3, -0.6, 0], [3, 0.626667, 0]],
                     [-0.950627, [3, -0.626667, 0], [3, 1.01333, 0]],
                     [-1.25489, [3, -1.01333, 0], [3, 0.44, 0]],
                     [-1.24659, [3, -0.44, -0.00830427], [3, 1, 0.0188733]],
                     [-0.452309, [3, -1, 0], [3, 0, 0]]])

        names.append("LHipRoll")
        times.append([0.4, 2.2, 4.08, 8.44, 11.44])
        keys.append([[0, [3, -0.133333, 0], [3, 0.6, 0]],
                     [0, [3, -0.6, 0], [3, 0.626667, 0]],
                     [0, [3, -0.626667, 0], [3, 1.45333, 0]],
                     [0, [3, -1.45333, 0], [3, 1, 0]],
                     [0, [3, -1, 0], [3, 0, 0]]])

        names.append("LHipYawPitch")
        times.append([0.4, 2.2, 4.08, 8.44, 11.44])
        keys.append([[0, [3, -0.133333, 0], [3, 0.6, 0]],
                     [0, [3, -0.6, 0], [3, 0.626667, 0]],
                     [0, [3, -0.626667, 0], [3, 1.45333, 0]],
                     [0, [3, -1.45333, 0], [3, 1, 0]],
                     [0, [3, -1, 0], [3, 0, 0]]])

        names.append("LKneePitch")
        times.append([0.4, 2.2, 4.08, 7.12, 8.44, 11.44])
        keys.append([[0.704172, [3, -0.133333, 0], [3, 0.6, 0]],
                     [0.947714, [3, -0.6, 0], [3, 0.626667, 0]],
                     [0.946988, [3, -0.626667, 0], [3, 1.01333, 0]],
                     [1.02974, [3, -1.01333, 0], [3, 0.44, 0]],
                     [1.02654, [3, -0.44, 0.00320618], [3, 1, -0.00728677]],
                     [0.700945, [3, -1, 0], [3, 0, 0]]])

        names.append("LShoulderPitch")
        times.append([0.4, 1.72, 2.2, 4.44, 8.44, 11.44])
        keys.append([[1.3911, [3, -0.133333, 0], [3, 0.44, 0]],
                     [1.3757, [3, -0.44, 0.0154043], [3, 0.16, -0.00560155]],
                     [1.23918, [3, -0.16, 0.0578236],
                      [3, 0.746667, -0.269843]],
                     [0.392699, [3, -0.746667, 0], [3, 1.33333, 0]],
                     [0.396376, [3, -1.33333, -0.00367739],
                      [3, 1, 0.00275804]],
                     [1.3974, [3, -1, 0], [3, 0, 0]]])

        names.append("LShoulderRoll")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[0.297329, [3, -0.133333, 0], [3, 0.44, 0]],
                     [0.182312, [3, -0.44, 0.0261096],
                      [3, 0.906667, -0.0538015]],
                     [0.0575959, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [0.0683221, [3, -1.33333, -0.0107263],
                      [3, 1, 0.0080447]],
                     [0.296743, [3, -1, 0], [3, 0, 0]]])

        names.append("LWristYaw")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[0, [3, -0.133333, 0], [3, 0.44, 0]],
                     [0, [3, -0.44, 0], [3, 0.906667, 0]],
                     [-1.01404, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [-1.00928, [3, -1.33333, -0.00475601],
                      [3, 1, 0.003567]],
                     [-0.00260372, [3, -1, 0], [3, 0, 0]]])

        names.append("RAnklePitch")
        times.append([0.4, 2.2, 4.08, 7.12, 8.44, 11.44])
        keys.append([[-0.355986, [3, -0.133333, 0], [3, 0.6, 0]],
                     [-0.411898, [3, -0.6, 0], [3, 0.626667, 0]],
                     [-0.40307, [3, -0.626667, -0.00778067],
                      [3, 1.01333, 0.0125815]],
                     [-0.350811, [3, -1.01333, 0], [3, 0.44, 0]],
                     [-0.353516, [3, -0.44, 0], [3, 1, 0]],
                     [-0.353516, [3, -1, 0], [3, 0, 0]]])

        names.append("RAnkleRoll")
        times.append([0.4, 2.2, 4.08, 8.44, 11.44])
        keys.append([[0, [3, -0.133333, 0], [3, 0.6, 0]],
                     [0, [3, -0.6, 0], [3, 0.626667, 0]],
                     [0, [3, -0.626667, 0], [3, 1.45333, 0]],
                     [0, [3, -1.45333, 0], [3, 1, 0]],
                     [0, [3, -1, 0], [3, 0, 0]]])

        names.append("RElbowRoll")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[1.00209, [3, -0.133333, 0], [3, 0.44, 0]],
                     [0.28536, [3, -0.44, 0], [3, 0.906667, 0]],
                     [1.47306, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [1.45976, [3, -1.33333, 0.0132977], [3, 1, -0.00997327]],
                     [1.01271, [3, -1, 0], [3, 0, 0]]])

        names.append("RElbowYaw")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[1.39072, [3, -0.133333, 0], [3, 0.44, 0]],
                     [1.39072, [3, -0.44, 0], [3, 0.906667, 0]],
                     [0.947714, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [0.960703, [3, -1.33333, -0.0129888],
                      [3, 1, 0.00974158]],
                     [1.38743, [3, -1, 0], [3, 0, 0]]])

        names.append("RHand")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[0.249591, [3, -0.133333, 0], [3, 0.44, 0]],
                     [0.249591, [3, -0.44, 0], [3, 0.906667, 0]],
                     [1, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [0.999879, [3, -1.33333, 0.000120997],
                      [3, 1, -9.07481e-05]],
                     [0.252151, [3, -1, 0], [3, 0, 0]]])

        names.append("RHipPitch")
        times.append([0.4, 2.2, 4.08, 7.12, 8.44, 11.44])
        keys.append([[-0.458529, [3, -0.133333, 0], [3, 0.6, 0]],
                     [-0.95644, [3, -0.6, 0], [3, 0.626667, 0]],
                     [-0.950627, [3, -0.626667, 0], [3, 1.01333, 0]],
                     [-1.25489, [3, -1.01333, 0], [3, 0.44, 0]],
                     [-1.24659, [3, -0.44, -0.00830427], [3, 1, 0.0188733]],
                     [-0.452309, [3, -1, 0], [3, 0, 0]]])

        names.append("RHipRoll")
        times.append([0.4, 2.2, 4.08, 8.44, 11.44])
        keys.append([[0, [3, -0.133333, 0], [3, 0.6, 0]],
                     [0, [3, -0.6, 0], [3, 0.626667, 0]],
                     [0, [3, -0.626667, 0], [3, 1.45333, 0]],
                     [0, [3, -1.45333, 0], [3, 1, 0]],
                     [0, [3, -1, 0], [3, 0, 0]]])

        names.append("RHipYawPitch")
        times.append([0.4, 2.2, 4.08, 8.44, 11.44])
        keys.append([[0, [3, -0.133333, 0], [3, 0.6, 0]],
                     [0, [3, -0.6, 0], [3, 0.626667, 0]],
                     [0, [3, -0.626667, 0], [3, 1.45333, 0]],
                     [0, [3, -1.45333, 0], [3, 1, 0]],
                     [0, [3, -1, 0], [3, 0, 0]]])

        names.append("RKneePitch")
        times.append([0.4, 2.2, 4.08, 7.12, 8.44, 11.44])
        keys.append([[0.704172, [3, -0.133333, 0], [3, 0.6, 0]],
                     [0.947714, [3, -0.6, 0], [3, 0.626667, 0]],
                     [0.946988, [3, -0.626667, 0], [3, 1.01333, 0]],
                     [1.02974, [3, -1.01333, 0], [3, 0.44, 0]],
                     [1.02654, [3, -0.44, 0.00320618],
                      [3, 1, -0.00728677]],
                     [0.700945, [3, -1, 0], [3, 0, 0]]])

        names.append("RShoulderPitch")
        times.append([0.4, 1.72, 2.2, 4.44, 8.44, 11.44])
        keys.append([[1.3911, [3, -0.133333, 0], [3, 0.44, 0]],
                     [1.3757, [3, -0.44, 0.0154043], [3, 0.16, -0.00560155]],
                     [1.23918, [3, -0.16, 0.0578236],
                      [3, 0.746667, -0.269843]],
                     [0.392699, [3, -0.746667, 0], [3, 1.33333, 0]],
                     [0.39575, [3, -1.33333, -0.00305085], [3, 1, 0.00228814]],
                     [1.3974, [3, -1, 0], [3, 0, 0]]])

        names.append("RShoulderRoll")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[-0.297329, [3, -0.133333, 0], [3, 0.44, 0]],
                     [-0.182312, [3, -0.44, -0.0261096],
                      [3, 0.906667, 0.0538015]],
                     [-0.0575959, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [-0.0683221, [3, -1.33333, 0.0107263],
                      [3, 1, -0.0080447]],
                     [-0.296743, [3, -1, 0], [3, 0, 0]]])

        names.append("RWristYaw")
        times.append([0.4, 1.72, 4.44, 8.44, 11.44])
        keys.append([[0, [3, -0.133333, 0], [3, 0.44, 0]],
                     [0, [3, -0.44, 0], [3, 0.906667, 0]],
                     [1.01404, [3, -0.906667, 0], [3, 1.33333, 0]],
                     [1.00928, [3, -1.33333, 0.00475601], [3, 1, -0.003567]],
                     [0.00260372, [3, -1, 0], [3, 0, 0]]])

        self.sessions[self.POSTURE].goToPosture("StandInit", 0.5)
        self.sessions[self.MOTION].angleInterpolationBezier(names, times, keys)