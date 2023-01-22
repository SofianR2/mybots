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
    #print(self.values)
    
  def Get_Value(self, i):
    self.values[i] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
    if self.values[len(self.values) - 1] != 0:
      print(self.values)
      
  def Save_Values(self):
    numpy.save('data/sensorValues.npy', self.values)
    p.disconnect()
