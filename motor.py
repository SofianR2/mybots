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
    def Prepare_To_Act(self):
      self.amplitude = c.backAmplitude
      self.frequency = c.backFrequency
      self.offset = c.backPhaseOffset
      self.backTargetAngles = numpy.linspace(self.offset, 2 * numpy.pi * self.frequency, 1000)
      self.backTargetAngles = numpy.sin(self.backTargetAngles) * self.amplitude
    Prepare_To_Act(self)
   
    
  def Prepare_To_Act(self):
    self.amplitude = c.backAmplitude
    self.frequency = c.backFrequency
    self.offset = c.backPhaseOffset

   

    #frontTargetAngles = numpy.linspace(self.offset, 2 * numpy.pi * self.frequency, 1000)
    #frontTargetAngles = numpy.sin(frontTargetAngles) * self.amplitude

  def Set_Value(self, robot, t):
    pyrosim.Set_Motor_For_Joint(
    bodyIndex = robot,
    jointName = self.jointName,
    controlMode = p.POSITION_CONTROL,
    targetPosition = self.backTargetAngles[t],
    maxForce = 500)

