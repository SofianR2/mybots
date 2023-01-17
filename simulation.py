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
    
  def Run():
    for i in range(1000):
      p.stepSimulation()
      backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
      frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")

      pyrosim.Set_Motor_For_Joint(
      bodyIndex = robotId,
      jointName = "Torso_BackLeg",
      controlMode = p.POSITION_CONTROL,
      targetPosition = backTargetAngles[i],
      maxForce = 500)

      pyrosim.Set_Motor_For_Joint(
      bodyIndex = robotId,
      jointName = "Torso_FrontLeg",
      controlMode = p.POSITION_CONTROL,
      targetPosition = frontTargetAngles[i],
      maxForce = 500)

      time.sleep(1/240)
