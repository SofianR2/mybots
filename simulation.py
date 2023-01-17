import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c

from world import WORLD
from robot import ROBOT

class SIMULATION:
  def __init__(self):
    self.physicsClient = p.connect(p.GUI)
    self.robotId = p.loadURDF("body.urdf")
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    pyrosim.Prepare_To_Simulate(self.robotId)
    self.world = WORLD()
    self.robot = ROBOT()    
    
  def Run(self):
    backLegSensorValues = numpy.zeros(1000)
    frontLegSensorValues = numpy.zeros(1000)
    targetAngles = numpy.zeros(1000)
    
    backTargetAngles = numpy.linspace(c.backPhaseOffset, 2 * numpy.pi * c.backFrequency, 1000)
    backTargetAngles = numpy.sin(backTargetAngles) * c.backAmplitude

    frontTargetAngles = numpy.linspace(c.frontPhaseOffset, 2 * numpy.pi * c.frontFrequency, 1000)
    frontTargetAngles = numpy.sin(frontTargetAngles) * c.frontAmplitude
    
    for i in range(1000):
      p.stepSimulation()
      backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
      frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

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

      time.sleep(1/240)
