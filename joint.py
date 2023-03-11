import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class JOINT:
  def __init__(self, name, parent, child, x, y, z):
    self.name = name
    self.parent = parent
    self.child = child
    self.xpos = x
    self.ypos = y
    self.zpos = z
  
  def Send_Joint(self):
    pyrosim.Send_Joint(name = self.name, parent= str(self.parent), child = str(self.child), type = "revolute", position = [self.xpos, self.ypos, self.zpos], jointAxis = "0 1 0")  

