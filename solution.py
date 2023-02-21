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
    self.max = 14
    self.get_sensor = []
    self.num_sensors = 0
    
   
    
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
    makeArm = 0
    armoffset = 0
    
    ##############pyrosim.Start_URDF("body.urdf")
    pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
    #pyrosim.Send_Cube(name="Torso", pos=[x,y,z+height_offset] , size=[length,width,height])
    #pyrosim.Send_Joint(name = "Torso_RightLeg" , parent= "Torso" , child = "RightLeg" , type = "revolute", position = [x+0.5,y,z+height_offset], jointAxis = "0 1 0")
    #pyrosim.Send_Cube(name="RightLeg", pos=[x+0.5,y,z-0.5] , size=[random.uniform(0.1, 2),random.uniform(0.1, 2),random.uniform(0.1, 2)])
    
    
    self.get_sensor = []
    for i in range(self.max):
      length = random.uniform(0.2, 1.5)
      width = random.uniform(0.2, 1.5)
      height = random.uniform(0.2, 1.5)
      current = i
      nex = i + 1
      arms = random.randrange(0, 2)
      skip = 0
      
      print("New Iteration")
      
      if(makeArm > 0):
        print("making arm")
        if(makeArm == 2):
          pyrosim.Send_Cube(name= str(i), pos=[x,y+(width/2),z+height_offset] , size=[0.2, 1, 0.2], color='    <color rgba="1.0 0.0 0.0 1.0"/>', cname = '<material name="Red">')
        if(makeArm == 1):
          pyrosim.Send_Cube(name= str(i), pos=[x,y-width,z+height_offset] , size=[0.2, 1, 0.2], color='    <color rgba="1.0 0.0 0.0 1.0"/>', cname = '<material name="Red">')

        if(makeArm == 2):
          arms = 1
        if(makeArm == 1):
          arms = 0
        
        
      if(makeArm == 0):  #if no arms, regularly make cube
        if(random.randrange(0,10) < 5): #sends sensor, makes blue
          print("making blue cube")
          pyrosim.Send_Cube(name= str(i), pos=[x+(length/2*width_offset),y,z+height_offset] , size=[length, width, height], color='    <color rgba="0.0 0.0 1.0 1.0"/>', cname = '<material name="Blue">')
          self.get_sensor.append(1)
        else: #no sensor, makes green
          print("making green cube")
          pyrosim.Send_Cube(name= str(i), pos=[x+(length/2*width_offset),y,z+height_offset] , size=[length, width, height], color='    <color rgba="0.0 1.0 0.0 1.0"/>', cname = '<material name="Green">')
          self.get_sensor.append(0)
      
      if(makeArm > 0):
        makeArm = makeArm - 1    
      
      if(i!=self.max-1):
        print(str(current) + " " + str(nex))
        
        if(i > 0 and arms == 1):
          print("making arm joint")
          if(makeArm == 0):
            makeArm = 2
          if(makeArm == 2):    
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x+(length/2),y+(length/2),z+height_offset], jointAxis = "0 1 0")
          if(makeArm == 1):
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x,y-(length/2),z+height_offset], jointAxis = "0 1 0")
            armoffset = 0.5

          
        else:
          print("making joint")
          pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x+(length/2*joint_offset)-armoffset,y,z+height_offset], jointAxis = "0 1 0")
          #armoffset = 0
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
    
    for index, item in enumerate(self.get_sensor):
      print(self.get_sensor)
      if item == 1:
        pyrosim.Send_Sensor_Neuron(name = sensor_number, linkName = str(index))
        print("name = " + str(sensor_number) + " " + "linkName = " + str(index))
        sensor_number = sensor_number + 1
    self.num_sensors = numpy.sum(self.get_sensor)
    
    
    '''
    for i in range(self.max):
      if(random.randrange(0,10) < 5):
        print("sending sensor to " + str(i))
        pyrosim.Send_Sensor_Neuron(name = sensor_number, linkName = str(i))
        sensor_number = sensor_number + 1
    '''
      
    
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
    #pyrosim.Send_Motor_Neuron(name = sensor_number+3, jointName = "2_3")
    #pyrosim.Send_Motor_Neuron(name = sensor_number+4, jointName = "3_4")
    #pyrosim.Send_Motor_Neuron(name = sensor_number+5, jointName = "4_5")
    #pyrosim.Send_Motor_Neuron(name = sensor_number+6, jointName = "5_6")
    '''
    pyrosim.Send_Motor_Neuron(name = 12 , jointName = "Torso_LeftLeg")
    pyrosim.Send_Motor_Neuron(name = 13 , jointName = "RightLeg_RightLowerLeg")
    pyrosim.Send_Motor_Neuron(name = 14 , jointName = "LeftLeg_LeftLowerLeg")
    pyrosim.Send_Motor_Neuron(name = 15 , jointName = "Torso_RightArm")
    pyrosim.Send_Motor_Neuron(name = 16 , jointName = "Torso_LeftArm")
    pyrosim.Send_Motor_Neuron(name = 17 , jointName = "RightArm_LowerRightArm")
    pyrosim.Send_Motor_Neuron(name = 18 , jointName = "LeftArm_LowerLeftArm")
    '''
    
    #for currentRow in range(0, c.numSensorNeurons):##################
    for currentRow in range(0, self.num_sensors):
      for currentColumn in range(0, c.numMotorNeurons):
        #pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])#######
        pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.num_sensors, weight = self.weights[currentRow-1][currentColumn])
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
    #randomRow = random.randint(0, c.numSensorNeurons-1)
    randomRow = random.randint(0, self.num_sensors-1)
    randomColumn = random.randint(0, c.numMotorNeurons-1)
    self.weights[randomRow, randomColumn] =  random.random() * 2 - 1
    
  def Set_ID(self, nextAvailableID):
    self.myID = nextAvailableID
    
