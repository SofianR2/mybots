import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c

class SOLUTION:
  def __init__(self, nextAvailableID):
    self.myID = nextAvailableID
    self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
    self.weights = self.weights * 2 - 1
    self.length = 1
    self.width = 1
    self.height = 1
    self.x=0
    self.y=0
    self.z=0.5
   
    
  def Create_World(self):
    length = self.length
    width = self.width
    height = self.height
    x = self.x
    y = self.y
    z = self.z
    ###pyrosim.Start_SDF("world.sdf")#########
    pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
    pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length+40,width+3,height])
    os.system("del world" + str(self.myID) + ".sdf")
    pyrosim.End()
    
    #while not os.path.exists("world.sdf"):##########
    while not os.path.exists("world" + str(self.myID) + ".sdf"):
      time.sleep(0.01)

  def Create_Body(self):
    length = self.length
    width = self.width
    height = self.height
    x = self.x
    y = self.y
    z = self.z
    height_offset = 3
    ##############pyrosim.Start_URDF("body.urdf")
    pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z+0.5+height_offset] , size=[length,width,height])
    pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [x,y+0.4,z+height_offset], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightLeg", pos=[x,y,z-1] , size=[length-0.4,width-0.4,height])
    pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [x,y-0.4,z+height_offset], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LeftLeg", pos=[x,y,z-1] , size=[length-0.4,width-0.4,height])
    
    pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [x,y,z-1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightLowerLeg", pos=[x,y,z-1.5] , size=[length-0.2,width-0.2,height])
    pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [x,y,z-1], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LeftLowerLeg", pos=[x,y,z-1.5] , size=[length-0.2,width-0.2,height])
    
    pyrosim.Send_Joint(name = "Torso_RightArm" , parent= "Torso" , child = "RightArm" , type = "revolute", position = [x,y+0.5,z+height_offset], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightArm", pos=[x,y,z] , size=[length-0.8,width-0.8,height-0.5])
    
    
    
    ''' long thing
    pyrosim.Send_Cube(name="Torso", pos=[x,y,z+0.5+height_offset] , size=[length+2,width-0.5,height])
    
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x,y,z+0.5+height_offset], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="FrontLeg", pos=[x,y+0.5,z-0.5] , size=[length-0.8,width,height-0.8])
    pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [x,y+1,z], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="FrontLowerLeg", pos=[x,y,z-1] , size=[length-0.2, width-0.8, height])
    #pyrosim.Send_Sphere(name="FrontLowerLeg", pos=[x,y,z-1] , size=[0])
    
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x,y,z+0.5+height_offset], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="BackLeg", pos=[x,y-0.5,z-0.5] , size=[length-0.8,width,height-0.8])
    pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [x,y-1,z], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="BackLowerLeg", pos=[x,y,z-1] , size=[length-0.2, width-0.8, height])
    #pyrosim.Send_Sphere(name="BackLowerLeg", pos=[x,y,z-1] , size=[0])
    '''

    '''
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x,y-0.5,z+0.5+height_offset], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="BackLeg", pos=[x,y-0.5,z-0.5] , size=[length-0.8,width,height-0.8])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x,y+0.5,z+0.5+height_offset], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="FrontLeg", pos=[x,y+0.5,z-0.5] , size=[length-0.8,width,height-0.8])
    pyrosim.Send_Joint(name = "Torso_LeftLeg" , parent= "Torso" , child = "LeftLeg" , type = "revolute", position = [x-0.5,y,z+0.5+height_offset], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LeftLeg", pos=[x-0.5,y,z-0.5] , size=[length,width-0.8,height-0.8])
    pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [x+0.5,y,z+0.5+height_offset], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightLeg", pos=[x+0.5,y,z-0.5] , size=[length,width-0.8,height-0.8])
    pyrosim.Send_Joint(name = "FrontLeg_FrontLowerLeg" , parent= "FrontLeg" , child = "FrontLowerLeg" , type = "revolute", position = [x,y+1,z-0.5], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="FrontLowerLeg", pos=[x,y,z-1] , size=[length-0.8,width-0.8,height])
    pyrosim.Send_Joint(name = "BackLeg_BackLowerLeg" , parent= "BackLeg" , child = "BackLowerLeg" , type = "revolute", position = [x,y-1,z-0.5], jointAxis = "1 0 0")
    pyrosim.Send_Cube(name="BackLowerLeg", pos=[x,y,z-1] , size=[length-0.8,width-0.8,height])
    pyrosim.Send_Joint(name = "RightLeg_RightLowerLeg" , parent= "RightLeg" , child = "RightLowerLeg" , type = "revolute", position = [x+1,y,z-0.5], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="RightLowerLeg", pos=[x,y,z-1] , size=[length-0.8,width-0.8,height])
    pyrosim.Send_Joint(name = "LeftLeg_LeftLowerLeg" , parent= "LeftLeg" , child = "LeftLowerLeg" , type = "revolute", position = [x-1,y,z-0.5], jointAxis = "0 1 0")
    pyrosim.Send_Cube(name="LeftLowerLeg", pos=[x,y,z-1] , size=[length-0.8,width-0.8,height])
    '''
    pyrosim.End()

  def Create_Brain(self):
    pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
    pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
    
    pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "RightLeg")
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLeg")
    pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")
    pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "LeftLowerLeg")
    pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "RightArm")
    
    #pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "FrontLeg")
    #pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "BackLeg")
    
    #pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "FrontLowerLeg")
    #pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "BackLowerLeg")
    

    #pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
    #pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
    #pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "LeftLeg")
    #pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "RightLeg")
    #pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "FrontLowerLeg")
    #pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "BackLowerLeg")
    #pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "RightLowerLeg")
    #pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LeftLowerLeg")
    
    pyrosim.Send_Motor_Neuron(name = 6 , jointName = "Torso_RightLeg")
    pyrosim.Send_Motor_Neuron(name = 7 , jointName = "Torso_LeftLeg")
    pyrosim.Send_Motor_Neuron(name = 8 , jointName = "RightLeg_RightLowerLeg")
    pyrosim.Send_Motor_Neuron(name = 9 , jointName = "LeftLeg_LeftLowerLeg")
    pyrosim.Send_Motor_Neuron(name = 10 , jointName = "Torso_RightArm")

    #pyrosim.Send_Motor_Neuron( name = 5 , jointName = "Torso_FrontLeg")
    #pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_BackLeg")
    #pyrosim.Send_Motor_Neuron( name = 7 , jointName = "FrontLeg_FrontLowerLeg")
    #pyrosim.Send_Motor_Neuron( name = 8 , jointName = "BackLeg_BackLowerLeg")
    
    #pyrosim.Send_Motor_Neuron( name = 6 , jointName = "Torso_BackLeg")
    #pyrosim.Send_Motor_Neuron( name = 7 , jointName = "Torso_FrontLeg")
    #pyrosim.Send_Motor_Neuron( name = 8 , jointName = "Torso_LeftLeg")
    #pyrosim.Send_Motor_Neuron( name = 9 , jointName = "Torso_RightLeg")
    #pyrosim.Send_Motor_Neuron( name = 10 , jointName = "FrontLeg_FrontLowerLeg")
    #pyrosim.Send_Motor_Neuron( name = 11 , jointName = "BackLeg_BackLowerLeg")
    #pyrosim.Send_Motor_Neuron( name = 12 , jointName = "RightLeg_RightLowerLeg")
    #pyrosim.Send_Motor_Neuron( name = 13 , jointName = "LeftLeg_LeftLowerLeg")
    
    
    for currentRow in range(0, c.numSensorNeurons):
      for currentColumn in range(0, c.numMotorNeurons):
        pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons , weight = self.weights[currentRow][currentColumn])
    pyrosim.End()
    
  def Evaluate(self, directOrGUI):
    '''
    os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))
    
    self.Create_World()
    self.Create_Body()
    self.Create_Brain()
    
    f = open("fitness" + str(self.myID) + ".txt", "r")
    
    while not os.path.exists("fitness" + str(self.myID) + ".txt"):
      time.sleep(0.01)
    
    self.fitness = float(f.read())
    print(self.fitness)
    f.close()
    '''
    
  def Start_Simulation(self, directOrGUI):
    self.Create_World()
    self.Create_Body()
    self.Create_Brain()
    
    os.system("start /B python3 simulate.py " + directOrGUI + " " + str(self.myID))

    
  def Wait_For_Simulation_To_End(self):
    while not os.path.exists("fitness" + str(self.myID) + ".txt"):
      time.sleep(0.1)
    
    f = open("fitness" + str(self.myID) + ".txt", "r")
    self.fitness = float(f.read())
    f.close()
    os.system("del fitness" + str(self.myID) + ".txt")
    
    
  def Mutate(self):
    randomRow = random.randint(0, c.numSensorNeurons-1)
    randomColumn = random.randint(0, c.numMotorNeurons-1)
    self.weights[randomRow, randomColumn] =  random.random() * 2 - 1
    
  def Set_ID(self, nextAvailableID):
    self.myID = nextAvailableID
    
