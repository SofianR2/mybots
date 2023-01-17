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
    self.sensor = {}
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName] = SENSOR(linkName)
    
