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
    '''
    pyrosim.Set_Motor_For_Joint(
      bodyIndex = self.robotId,
      jointName = "Torso_BackLeg",
      controlMode = p.POSITION_CONTROL,
      targetPosition = backTargetAngles[i],
      maxForce = 500)

      pyrosim.Set_Motor_For_Joint(
      bodyIndex = self.robotId,
      jointName = "Torso_FrontLeg",
      controlMode = p.POSITION_CONTROL,
      targetPosition = frontTargetAngles[i],
      maxForce = 500)
    '''
