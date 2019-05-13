# Choregraphe simplified export in Python.

# New_happy
from naoqi import ALProxy
import happy


try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  # motion = ALProxy("ALMotion", IP, 9559)
  motion = ALProxy("ALMotion")
  motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err


try:
  # uncomment the following line and modify the IP if you use this script outside Choregraphe.
  motion = ALProxy("ALMotion", "localhost", 46015)
#   motion = ALProxy("ALMotion")
  names, keys, times = happy()
  motion.angleInterpolation(names, keys, times, True)
  motion.angleInterpolation(names, keys, times, True)
#   motion.angleInterpolation(names, keys, times, True)
#   motion.angleInterpolation(names, keys, times, True)
#   motion.angleInterpolation(names, keys, times, True)
except BaseException, err:
  print err
