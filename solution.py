import numpy
import pyrosim.pyrosim as pyrosim
import os
import random
import time
import constants as c
from link import LINK
from joint import JOINT

class SOLUTION:
  def __init__(self, nextAvailableID):
    self.myID = nextAvailableID
    self.weights = numpy.random.rand(c.numSensorNeurons, c.numMotorNeurons)
    self.weights = self.weights * 2 - 1
    #print(self.weights)
    self.length = 1
    self.width = 1
    self.height = 1
    self.x=0
    self.y=0
    self.z=0
    self.max = 7
    self.get_sensor = []
    self.num_sensors = 0
    self.num_motors = 0
    self.link_list = []
    self.added_links = []
    self.joint_list = []
    
    #Create initial link
    self.link_list.append(LINK())
    self.added_links.append(0)
    self.link_list[0].zpos += 1
    self.AddNewLinkAndJoint()
    
  def Create_World(self):#########################################################
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

  def SendSensor(self, link): ##################################################### Checks given link's color, adds to get_sensor
    if(link.color ==  '    <color rgba="0.0 0.0 1.0 1.0"/>'):
      self.get_sensor.append(1)
    else:
      self.get_sensor.append(0)
      
  def BuildBody(self):#############################################################
    '''
    for i, link in enumerate(self.link_list):
      pyrosim.Send_Cube(name = str(i), pos = [link.xpos, link.ypos, link.zpos], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
      self.SendSensor(link)
      if(i < self.max-1 and i > 0):
        print(i)
        self.joint_list[i].Send_Joint(joint)
    '''

    self.get_sensor = []
    for i, link in enumerate(self.link_list):
      pyrosim.Send_Cube(name = str(i), pos = [link.xpos, link.ypos, link.zpos], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
      #print("Send_cube for " + str(i) + " completed")
      self.SendSensor(link)
      #print("Link Name = " + str(i))
      
    for joint in self.joint_list:
      #print(self.joint_list)
      #print(self.joint_list)
      joint.Send_Joint()
    
      
  def AddNewLinkAndJoint(self):####################################################
    #variables (MIGHT TAKE THESE OUT AND PUT IN CREATE BODY)
    height_offset = 0
    x = self.x
    y = self.y
    z = self.z + height_offset
    jointTrueOffset = 0
    otherOffset = 0
    otherOffset2 = 0
    otherOffset3 = 0

    #pick random direction to move in
    direction = random.randint(1,3)

    #pick parent from existing body
    p = random.choice(self.added_links)
    
    #check to make sure we can move in that direction and change it otherwise
    while(sum(self.link_list[p].occupied) == 3):            #check if parent is full
          p = random.choice(self.added_links)
        
    #once everything with parent is set, then add the new link to the added link list
    self.link_list.append(LINK())
    self.added_links.append(len(self.added_links))
    c = len(self.added_links) - 1
        
    while(self.link_list[p].occupied[direction-1] != 0):    #check if direction is open
      direction = random.randint(1,3)
    self.link_list[p].occupied[direction-1] = 1
    self.link_list[c].occupied[direction+2] = 1
    
    #set parent xyz
    previous_direction = 0
    parentx = self.link_list[p].x
    parenty = self.link_list[p].y
    parentz = self.link_list[p].z
        
    #update previous_direction for child accordingly
    if(c > 0 and p!= 0):
      previous_direction = self.link_list[p].previous
        
    new_joint_name = str(p) + "_" + str(c)
    #z = 0
        
    #DEFINE JOINTS
    length = self.link_list[c].x
    width = self.link_list[c].y
    height = self.link_list[c].z
    if(direction == 1):#x direction
      #print("direction 1")
      if(p == 0):
        #print("parent is 0")
        jointTrueOffset = parentx/2 - parentx
        otherOffset = parentx/2
        otherOffset2 = parenty/2
        otherOffset3 = parentz/2
        z = 1
      if(previous_direction == 1 or previous_direction == 0):#coming from x #SET NAME, PARENT, CHILD, POSITION, and AXIS
        self.joint_list.append(JOINT(new_joint_name, str(p), str(c), (x + parentx + jointTrueOffset), y, z))
        z = 0
        self.link_list[c].Update_Link_Pos(x+length/2, y, z)
      if(previous_direction == 2):#coming from y
        self.joint_list.append(JOINT(new_joint_name, str(p), str(c), (x+parentx/2 + jointTrueOffset + otherOffset), y+parenty/2 - otherOffset2, z))            
        z = 0
        self.link_list[c].Update_Link_Pos(x+length/2, y, z)
      if(previous_direction == 3):#coming from z
        self.joint_list.append(JOINT(new_joint_name, str(p), str(c), (x+parentx/2 + jointTrueOffset + otherOffset), y, z+parentz/2 - otherOffset3))            
        z = 0
        self.link_list[c].Update_Link_Pos(x+length/2, y, z)
      self.link_list[c].previous = 1
          
    if(direction == 2):#y direction
      #print("direction 2")
      if(p == 0):
        jointTrueOffset = parenty/2 - parenty
        otherOffset = parentx/2
        otherOffset2 = parenty/2
        otherOffset3 = parentz/2
        z = 1
      if(previous_direction == 2 or previous_direction == 0):#coming from y
        self.joint_list.append(JOINT(new_joint_name, str(p), str(c), x, y+parenty+jointTrueOffset, z))
        z = 0
        self.link_list[c].Update_Link_Pos(x, y+width/2, z)
      if(previous_direction == 1):#coming from x
        self.joint_list.append(JOINT(new_joint_name, str(p), str(c), x+parentx/2 - otherOffset, y + parenty/2 + jointTrueOffset + otherOffset2, z))
        z = 0
        self.link_list[c].Update_Link_Pos(x, y+width/2, z)
      if(previous_direction == 3):#coming from z
        self.joint_list.append(JOINT(new_joint_name, str(p), str(c), x, y + parenty/2 + jointTrueOffset + otherOffset2, z+parentz/2 - otherOffset3))
        z = 0
        self.link_list[c].Update_Link_Pos(x, y+width/2, z)
      self.link_list[c].previous = 2

    if(direction == 3):#z direction
      #print("direction 3")
      if(p == 0):
        jointTrueOffset = parentz/2 - parentz
        otherOffset = parentx/2
        otherOffset2 = parenty/2
        otherOffset3 = parentz/2
        z = 1
      if(previous_direction == 3 or previous_direction == 0):#coming from z
        self.joint_list.append(JOINT(new_joint_name, str(p), str(c), x, y, z+parentz+jointTrueOffset))
        z = 0
        self.link_list[c].Update_Link_Pos(x, y, z+height/2)
      if(previous_direction == 1):#coming from x
        self.joint_list.append(JOINT(new_joint_name, str(p), str(c), x+parentx/2 - otherOffset, y, z + parentz/2 + jointTrueOffset + otherOffset3))
        z = 0
        self.link_list[c].Update_Link_Pos(x, y, z+height/2)
      if(previous_direction == 2):#coming from y
        self.joint_list.append(JOINT(new_joint_name, str(p), str(c), x, y+parenty/2 - otherOffset2, z + parentz/2 + jointTrueOffset + otherOffset3))
        z = 0
        self.link_list[c].Update_Link_Pos(x, y, z+height/2)
      self.link_list[c].previous = 3
  
  def Create_Body(self):##########################################################
    #print(self.added_links)
    pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
    self.BuildBody()
    #pyrosim.Send_Cube(name = str(0), pos = [0, 0, 0], size = [1, 1, 1], color =   '    <color rgba="0.0 0.0 1.0 1.0"/>', cname =  '<material name="Blue">')
    #print("AAAAAAAAAAAAAAAAAAAAAAAAA")
    pyrosim.End()

  def Create_Brain(self):#########################################################
    sensor_number = 0
    pyrosim.Start_NeuralNetwork("brain" + str(self.myID) + ".nndf")
    
    for i, link in enumerate(self.link_list):
      if(link.has_link == 1):
        pyrosim.Send_Sensor_Neuron(name = sensor_number, linkName = str(i))
        #print("name = " + str(sensor_number) + " linkName = " + str(i))
        sensor_number = sensor_number + 1
        
    #print("CCCCCCCCCCCCCCCC")    
    for i, joint in enumerate(self.joint_list):
      pyrosim.Send_Motor_Neuron(name = sensor_number, jointName = joint.name)
      #print("name = " + str(sensor_number) + " jointName = " + str(joint.name))
      sensor_number = sensor_number + 1
      #print(self.get_sensor)
    self.num_sensors = numpy.sum(self.get_sensor)
    self.num_motors = len(self.joint_list)
  
    #print("DDDDDDDDDDDDDDDDDDDD")
    #for currentRow in range(0, c.numSensorNeurons):##################
    #print("num_sensors: " + str(self.num_sensors))
    #print("num_motors: " + str(self.num_motors))
    for currentRow in range(0, self.num_sensors):
      #for currentColumn in range(0, c.numMotorNeurons):
      for currentColumn in range(0, self.num_motors):
        #print("Row: " + str(currentRow))
        #print("Column: " + str(currentColumn))
        pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.num_sensors, weight = self.weights[currentRow-1][currentColumn])
    #print("EEEEEEEEEEEEEEEEEEEEEEEEEEEE")
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
    while True:
      try:
        f = open("fitness" + str(self.myID) + ".txt", "r")
        break
      except:
        pass
    self.fitness = float(f.read())
    f.close()
    os.system("del fitness" + str(self.myID) + ".txt")
    
    
  def Mutate(self):
    randomRow = random.randint(0, c.numSensorNeurons-1)
    #print("Num sensors: " + str(self.num_sensors))
    #randomRow = random.randint(0, self.num_sensors)
    #randomRow = random.randint(0, self.num_sensors-1)
    #randomColumn = random.randint(0, self.num_motors-1)
    randomColumn = random.randint(0, c.numMotorNeurons-1)
    self.weights[randomRow, randomColumn] =  random.random() * 2 - 1
    
    if(len(self.link_list) < 12):
      self.AddNewLinkAndJoint()
      #print("Mutation Complete")
    else:
      self.link_list.pop()
      self.added_links.pop()
      self.joint_list.pop()
      self.Create_Body()
      self.Create_Brain()
      
    #else:
    #  random_link = random.randint(0, 11)
    #  self.link_list[random_link].x = random.uniform(0.2, 1)
    #  self.link_list[random_link].y = random.uniform(0.2, 1)
    #  self.link_list[random_link].z = random.uniform(0.2, 1)
    #  self.BuildBody()

    
    #Add joint and extend one link

    
  def Set_ID(self, nextAvailableID):
    self.myID = nextAvailableID
    
