import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class LINK:
  def __init__(self):
    if(random.randrange(0,10) < 5):
      self.color = '    <color rgba="0.0 0.0 100.0 1.0"/>'
      self.color_name =  '<material name="Blue">'
      self.has_link = 1
    else:
      self.color = '    <color rgba="0.0 100.0 0.0 1.0"/>'
      self.color_name =  '<material name="Green">'
      self.has_link = 0
    self.x = random.uniform(0.2, 1)
    self.y = random.uniform(0.2, 1)
    self.z= random.uniform(0.2, 1)
