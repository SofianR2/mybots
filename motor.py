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
    self.jointName = jointName
    Prepare_To_Act()
    
  def Prepare_To_Act(self):
    self.amplitude = c.backAmplitude
    self.frequency = c.backFrequency
    self.offset = c.backPhaseOffset

    backTargetAngles = numpy.linspace(self.offset, 2 * numpy.pi * self.frequency, 1000)
    backTargetAngles = numpy.sin(backTargetAngles) * self.amplitude

    frontTargetAngles = numpy.linspace(self.offset, 2 * numpy.pi * self.frequency, 1000)
    frontTargetAngles = numpy.sin(frontTargetAngles) * self.amplitude

  def Set_Value(self):
    pass
