import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class JOINT:
  def __init__(self):
    self.parent
    self.child
    self.xpos
    self.ypos
    self.zpos
    self.axis
  
  def Send_Joint(self):
    pyrosim.Send_Joint(name = new_joint_name, parent= str(self.parent), child = str(self.child), type = "revolute", position = [self.xpos, self.ypos, self.zpos], jointAxis = "0 1 0")  

