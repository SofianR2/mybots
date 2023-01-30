import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c
import sys

from world import WORLD
from robot import ROBOT

class SIMULATION:
  def __init__(self, directOrGUI):
    self.directOrGUI = directOrGUI
    if(directOrGUI == "DIRECT"):
      #self.physicsClient = p.connect(p.DIRECT)
      p.connect(p.DIRECT)
    else:
      #self.physicsClient = p.connect(p.GUI)
      p.connect(p.GUI)
        
    self.physicsClient = p.connect(p.DIRECT)
    #self.robotId = p.loadURDF("body.urdf")  
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    self.world = WORLD()
    self.robot = ROBOT()  
    p.setGravity(0,0,-9.8)
    pyrosim.Prepare_To_Simulate(self.robot.robotId)
    self.robot.Prepare_To_Sense()
    self.robot.Prepare_To_Act()
    
  def __del__(self):
    self.physicsClient = p.connect(p.DIRECT)
    p.disconnect()
    
  def Run(self):
    if(self.directOrGUI == "GUI"):
      time.sleep()

    #backLegSensorValues = numpy.zeros(1000)
    #frontLegSensorValues = numpy.zeros(1000)
    #targetAngles = numpy.zeros(1000)
    
    '''
    backTargetAngles = numpy.linspace(c.backPhaseOffset, 2 * numpy.pi * c.backFrequency, 1000)
    backTargetAngles = numpy.sin(backTargetAngles) * c.backAmplitude

    frontTargetAngles = numpy.linspace(c.frontPhaseOffset, 2 * numpy.pi * c.frontFrequency, 1000)
    frontTargetAngles = numpy.sin(frontTargetAngles) * c.frontAmplitude
    '''
    
    for i in range(1000):
      p.stepSimulation()
      self.robot.Sense(i)
      self.robot.Think()
      self.robot.Act(i)
      #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
      #frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")


      #pyrosim.Set_Motor_For_Joint(
      #bodyIndex = self.robotId,
      #jointName = "Torso_BackLeg",
      #controlMode = p.POSITION_CONTROL,
      #targetPosition = backTargetAngles[i],
      #maxForce = 500)

      #pyrosim.Set_Motor_For_Joint(
      #bodyIndex = self.robotId,
      #jointName = "Torso_FrontLeg",
      #controlMode = p.POSITION_CONTROL,
      #targetPosition = frontTargetAngles[i],
      #maxForce = 500)


      #time.sleep(1/240)
      
  def Get_Fitness(self):
    self.robot.Get_Fitness()
