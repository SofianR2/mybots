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
    
    self.amplitude = c.amplitude
    if self.jointName == 'Torso_BackLeg':
      self.frequency = c.frequency * 2
    else:
      self.frequency = c.frequency
    self.offset = c.phaseOffset
    self.motorValues = numpy.linspace(self.offset, 2 * numpy.pi * self.frequency, 1000)
    self.motorValues = numpy.sin(self.motorValues) * self.amplitude
    
  '''
    def Prepare_To_Act(self):
      self.amplitude = 0
      if self.jointName == b'Torso_BackLeg':
        self.frequency = 0
      else:
        self.frequency = 0
      self.offset = 0
      self.motorValues = numpy.linspace(self.offset, 2 * numpy.pi * self.frequency, 1000)
      self.motorValues = numpy.sin(self.motorValues) * self.amplitude
  Prepare_To_Act(self)
  '''

  def Set_Value(self, robot, t):
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = self.jointName,
    controlMode = p.POSITION_CONTROL,
    targetPosition = self.motorValues[t],
    maxForce = 500)
    
  def Save_Values(self):
      numpy.save('data/motorValues.npy', motorValues)
      p.disconnect()


