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
    self.max = 7
    self.get_sensor = []
    
   
    
  def Create_World(self):
    length = self.length
    width = self.width
    height = self.height
    x = self.x
    y = self.y
    z = self.z
    ###pyrosim.Start_SDF("world.sdf")#########
    pyrosim.Start_SDF("world" + str(self.myID) + ".sdf")
    #pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length+40,width+3,height])
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
    height_offset = 1
    joint_offset = 1
    width_offset = 0
    
    ##############pyrosim.Start_URDF("body.urdf")
    pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
    #pyrosim.Send_Cube(name="Torso", pos=[x,y,z+height_offset] , size=[length,width,height])
    #pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [x+0.5,y,z+height_offset], jointAxis = "0 1 0")
    #pyrosim.Send_Cube(name="RightLeg", pos=[x+0.5,y,z-0.5] , size=[random.uniform(0.1, 2),random.uniform(0.1, 2),random.uniform(0.1, 2)])
    
    
    
    for i in range(self.max):
      flip = random.randrange(0,10)
      length = random.uniform(0.2, 1.5)
      width = random.uniform(0.2, 1.5)
      height = random.uniform(0.2, 1.5)
      current = i
      nex = i + 1
      if(random.randrange(0,10) < 5): #sends sensor, makes blue
        pyrosim.Send_Cube(name= str(i), pos=[x+(length/2*width_offset),y,z+height_offset] , size=[length, width, height], color='    <color rgba="1.0 1.0 100.0 1.0"/>')
        self.get_sensor.append(1)
      else: #no sensor, makes green
        pyrosim.Send_Cube(name= str(i), pos=[x+(length/2*width_offset),y,z+height_offset] , size=[length, width, height], color='    <color rgba="100.0 1.0 1.0 1.0"/>')
      if(i!=self.max-1):
        pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x+(length/2*joint_offset),y,z+height_offset], jointAxis = "0 1 0")
        print(str(current) + "_" + str(nex))
        height_offset = -0.5
        width_offset = 1
        joint_offset = 2
        

      
      '''
      pyrosim.Send_Cube(name= str(i), pos=[x,y,z+height_offset] , size=[length, width, height])
      #if i != self.max:
      #  pyrosim.Send_Joint(name = str(i) + "_" + str(i+1), parent= str(i) , child = str(i+1) , type = "revolute", position = [x+0.5,y,z+height_offset], jointAxis = "0 1 0")
      
      if(i == 1):
                pyrosim.Send_Joint(name = str(previous) + "_" + str(current), parent= str(previous) , child = str(current) , type = "revolute", position = [x+(width/2),y,z+height_offset], jointAxis = "0 1 0")

      if(i>1):
        
        pyrosim.Send_Joint(name = str(previous) + "_" + str(current), parent= str(previous) , child = str(current) , type = "revolute", position = [x+(width/2),y,z+height_offset], jointAxis = "0 1 0")
      '''
    pyrosim.End()

  def Create_Brain(self):
    sensor_number = 0
    pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
    for i in range(self.max):
      if(random.randrange(0,10) < 5):
        print("sending sensor to " + str(i))
        pyrosim.Send_Sensor_Neuron(name = sensor_number, linkName = str(i))
        sensor_number = sensor_number + 1
      
    
    #pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "0")
    
    #pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "1")
    '''
    pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "LeftLeg")
    pyrosim.Send_Sensor_Neuron(name = 3 , linkName = "RightLowerLeg")
    pyrosim.Send_Sensor_Neuron(name = 4 , linkName = "LeftLowerLeg")
    pyrosim.Send_Sensor_Neuron(name = 5 , linkName = "RightArm")
    pyrosim.Send_Sensor_Neuron(name = 6 , linkName = "LeftArm")
    pyrosim.Send_Sensor_Neuron(name = 7 , linkName = "LowerRightArm")
    pyrosim.Send_Sensor_Neuron(name = 8 , linkName = "LowerLeftArm")
    pyrosim.Send_Sensor_Neuron(name = 9 , linkName = "RightShoe")
    pyrosim.Send_Sensor_Neuron(name = 10 , linkName = "LeftShoe")
    '''
    
    pyrosim.Send_Motor_Neuron(name = sensor_number+1, jointName = "0_1")
    pyrosim.Send_Motor_Neuron(name = sensor_number+2, jointName = "1_2")
    pyrosim.Send_Motor_Neuron(name = sensor_number+3, jointName = "2_3")
    pyrosim.Send_Motor_Neuron(name = sensor_number+4, jointName = "3_4")
    pyrosim.Send_Motor_Neuron(name = sensor_number+5, jointName = "4_5")
    pyrosim.Send_Motor_Neuron(name = sensor_number+6, jointName = "5_6")
    '''
    pyrosim.Send_Motor_Neuron(name = 12 , jointName = "Torso_LeftLeg")
    pyrosim.Send_Motor_Neuron(name = 13 , jointName = "RightLeg_RightLowerLeg")
    pyrosim.Send_Motor_Neuron(name = 14 , jointName = "LeftLeg_LeftLowerLeg")
    pyrosim.Send_Motor_Neuron(name = 15 , jointName = "Torso_RightArm")
    pyrosim.Send_Motor_Neuron(name = 16 , jointName = "Torso_LeftArm")
    pyrosim.Send_Motor_Neuron(name = 17 , jointName = "RightArm_LowerRightArm")
    pyrosim.Send_Motor_Neuron(name = 18 , jointName = "LeftArm_LowerLeftArm")
    '''
    
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
    
