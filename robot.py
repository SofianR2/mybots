import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c

from sensor import SENSOR

class ROBOT:
  def __init__(self):
    
    self.motor = {}
    #self.robotId = p.loadURDF("body.urdf")
    
  def Prepare_To_Sense(self):
    self.sensors = {}
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName] = SENSOR(linkName)
  
  def Sense(self, t):
    #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    for i in self.sensors:
      self.sensors[i].Get_Value(t)
    
    
