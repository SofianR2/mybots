import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random
import constants as c
from pyrosim.neuralNetwork import NEURAL_NETWORK

from sensor import SENSOR
from motor import MOTOR

class ROBOT:
  def __init__(self):    
    #self.motors = {}    
    self.robotId = p.loadURDF("body.urdf")
    self.nn = NEURAL_NETWORK("brain.nndf")
    
  def Prepare_To_Sense(self):
    self.sensors = {}
    for linkName in pyrosim.linkNamesToIndices:
      self.sensors[linkName] = SENSOR(linkName)
  
  def Sense(self, t):
    #backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    for i in self.sensors:
      self.sensors[i].Get_Value(t)
    
  def Prepare_To_Act(self):
    self.motors = {} 
    for jointName in pyrosim.jointNamesToIndices:
      self.motors[jointName] = MOTOR(jointName)
   
  def Act(self, t):
    for neuronName in self.nn.Get_Neuron_Names():
      print(neuronName)
      
    for i in self.motors:
      self.motors[i].Set_Value(self.robotId, t)
  
  def Think(self):
    self.nn.Update()
    self.nn.Print()      
    
