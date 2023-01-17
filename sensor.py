import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c

class SENSOR:
  def __init__(self, linkName):
    self.linkName = linkName
    self.values = numpy.zeros(1000)
    print(self.values)
