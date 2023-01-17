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
