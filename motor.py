import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c

class MOTOR:
  def __init__(self, jointName):
    self.jointName = jointName'
    
  def Prepare_To_Act(self):
    for jointName in pyrosim.jointNamesToIndices:
      self.motor[jointName] = MOTOR(jointName)
