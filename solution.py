import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
from link import LINK

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
    self.num_sensors = 0
    self.coordinates = []
    self.link_list = []
    self.added_links = []
    self.joint_list = []
    
   
    
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
    self.link_list = []
    length = self.length
    width = self.width
    height = self.height
    x = self.x
    y = self.y
    z = self.z
    height_offset = 1
    joint_offset = 1
    width_offset = 0
    length_offset = 0
    z_offset = 0
    previous_direction = 99

    
    pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
    ##############################################
    
    for i in range(self.max):
      self.link_list.append(LINK())
      #print(len(self.link_list))
      
    for i, link in enumerate(self.link_list):
      if(i == 0):
        pyrosim.Send_Cube(name = str(i), pos = [x, y, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
        if(link.color ==  '    <color rgba="0.0 0.0 100.0 1.0"/>'):
          self.get_sensor.append(1)
        else:
          self.get_sensor.append(0)

        self.added_links.append(i)
      else:
        p = random.choice(self.added_links)
        new_joint_name = str(p) + "_" + str(i)
        #new_joint_name = str(p) + str(i)
        pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x, y, z], jointAxis = "0 1 0")
        self.joint_list.append(new_joint_name)
        pyrosim.Send_Cube(name = str(i), pos = [x, y, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
        self.added_links.append(i)

    
        
    ##############################################
    '''    
    self.get_sensor = []
    for i in range(self.max):
      length = random.uniform(0.2, 1)
      width = random.uniform(0.2, 1)
      height = random.uniform(0.2, 1)
      current = i
      nex = i + 1
      direction = random.randint(0,2)
      #direction = 2

      if(random.randrange(0,10) < 5): #sends sensor, makes blue
        pyrosim.Send_Cube(name= str(i), pos=[x+(length/2*length_offset),y+(width/2*width_offset),z+height_offset+(height/2*z_offset)] , size=[length, width, height], color='    <color rgba="0.0 0.0 100.0 1.0"/>', cname = '<material name="Blue">')
        self.get_sensor.append(1)
      else: #no sensor, makes green
        pyrosim.Send_Cube(name= str(i), pos=[x+(length/2*length_offset),y+(width/2*width_offset),z+height_offset+(height/2*z_offset)] , size=[length, width, height], color='    <color rgba="0.0 100.0 0.0 1.0"/>', cname = '<material name="Green">')
        self.get_sensor.append(0)
      if(i!=self.max-1):
        if (direction == 0): #x direction
          #random_multiplier = numpy.random.rand(0, 1) * 2 - 1
          if(previous_direction == 0): #x direction
            joint_offset = 2
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x+(length/2*joint_offset),y,z+height_offset], jointAxis = "0 1 0")
          elif(previous_direction == 1):
            joint_offset = 1
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x+(length/2*joint_offset),y+(length/2),z+height_offset], jointAxis = "1 0 0")
          elif(previous_direction == 2):
            joint_offset = 1
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x+(length/2*joint_offset),y,z+height_offset+(height/2)], jointAxis = "1 0 0")
          else:
            joint_offset = 0
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x+(length/2*joint_offset),y,z+height_offset], jointAxis = "0 1 0")
          height_offset = -0.5
          length_offset = 1
          width_offset = 0
          z_offset = 0
          #joint_offset = 2
          previous_direction = 0
          
        if(direction == 1): #y direction
          if(previous_direction == 1):
            joint_offset = 2
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x,y+(width/2*joint_offset),z+height_offset], jointAxis = "1 0 0")
          elif(previous_direction == 0):
            joint_offset = 1
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x+(length/2),y+(width/2*joint_offset),z+height_offset], jointAxis = "0 1 0")
          elif(previous_direction == 2):
            joint_offset = 1
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x,y+(width/2*joint_offset),z+height_offset+(height/2)], jointAxis = "0 1 0")
          else:
            joint_offset = 0
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x,y+(width/2*joint_offset),z+height_offset], jointAxis = "1 0 0")
          height_offset = -0.5
          width_offset = 1
          length_offset = 0
          z_offset = 0
          joint_offset = 2
          previous_direction = 1
          
        if(direction == 2): #z direction
          if(previous_direction == 2):
            joint_offset = 2
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x,y,z+height_offset+(height/2*joint_offset)], jointAxis = "1 0 0")
          elif(previous_direction == 0):
            joint_offset = 1
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x+(length/2),y,z+height_offset+(height/2*joint_offset)], jointAxis = "0 1 0")
          elif(previous_direction == 1):
            joint_offset = 1
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x,y+(width/2),z+height_offset+(height/2*joint_offset)], jointAxis = "0 1 0")
          else:
            joint_offset = 0
            pyrosim.Send_Joint(name = str(current) + "_" + str(nex), parent= str(current) , child = str(nex) , type = "revolute", position = [x,y,z+height_offset+(height/2*joint_offset)], jointAxis = "1 0 0")
          height_offset = -0.5
          width_offset = 0
          length_offset = 0
          z_offset = 1
          joint_offset = 2
          previous_direction = 2
            
      ################################################################################################################################################################
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
    
    for i, link in enumerate(self.link_list):
      if(link.has_link == 1):
        pyrosim.Send_Sensor_Neuron(name = sensor_number, linkName = str(i))
        #print("name = " + str(sensor_number) + " linkName = " + str(i))
        sensor_number = sensor_number + 1
        
    for i, joint in enumerate(self.joint_list):
      pyrosim.Send_Motor_Neuron(name = sensor_number, jointName = joint)
      print("name = " + str(sensor_number) + " jointName = " + str(joint))
      sensor_number = sensor_number + 1
    self.num_sensors = numpy.sum(self.get_sensor)

      
    '''
    for index, item in enumerate(self.get_sensor):
      print(self.get_sensor)
      if item == 1:
        pyrosim.Send_Sensor_Neuron(name = sensor_number, linkName = str(index))
        sensor_number = sensor_number + 1
    self.num_sensors = numpy.sum(self.get_sensor)
    ###################################################################
    pyrosim.Send_Motor_Neuron(name = sensor_number+1, jointName = "0_1")
    pyrosim.Send_Motor_Neuron(name = sensor_number+2, jointName = "1_2")
    pyrosim.Send_Motor_Neuron(name = sensor_number+3, jointName = "2_3")
    pyrosim.Send_Motor_Neuron(name = sensor_number+4, jointName = "3_4")
    pyrosim.Send_Motor_Neuron(name = sensor_number+5, jointName = "4_5")
    pyrosim.Send_Motor_Neuron(name = sensor_number+6, jointName = "5_6")
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
    
