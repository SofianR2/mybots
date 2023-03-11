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
    self.coordinates = []
    self.link_list = []
    self.added_links = []
    self.joint_list = []
    
    #Create initial link
    self.link_list.append(LINK())
    self.added_links.append(0)
    
  def Create_World(self):#########################################################
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

  def SendSensor(self, link): ##################################################### Checks given link's color, adds to get_sensor
    if(link.color ==  '    <color rgba="0.0 0.0 1.0 1.0"/>'):
      self.get_sensor.append(1)
    else:
      self.get_sensor.append(0)
      
  def BuildBody(self):#############################################################
    for i, link in enumerate(self.link_list):
      pyrosim.Send_Cube(name = str(i), pos = [link.xpos, link.ypos, link.zpos], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
      self.SendSensor(link)
      
    for joint in self.joint_list:
      joint.Send_Joint(joint)
      
  def AddNewLinkAndJoint(self):####################################################
    #variables (MIGHT TAKE THESE OUT AND PUT IN CREATE BODY)
    height_offset = 1
    x = self.x
    y = self.y
    z = self.z + height_offset

    #pick random direction to move in
    direction = random.randint(1,3)

    #pick parent from existing body
    p = random.choice(self.added_links)
    
    #check to make sure we can move in that direction and change it otherwise
    while(sum(self.link_list[p].occupied) == 3):            #check if parent is full
          p = random.choice(self.added_links)
        
    #once everything with parent is set, then add the new link to the added link list
    self.link_list.append(LINK())
    self.added_links.append(len(added_links))
    c = len(added_links) - 1
        
    while(self.link_list[p].occupied[direction-1] != 0):    #check if direction is open
      direction = random.randint(1,3)
    self.link_list[p].occupied[direction-1] = 1
    self.link_list[c].occupied[direction+2] = 1
    
    #set parent xyz
    parentx = self.link_list[p].x
    parenty = self.link_list[p].y
    parentz = self.link_list[p].z
        
    #update previous_direction for child accordingly
    if(c > 0 and p!= 0):
          previous_direction = self.link_list[p].previous
        
    new_joint_name = str(p) + "_" + str(i)
    z = 0
        
    #DEFINE JOINTS
    #self.joint_list.append[JOINT()]    
    if(direction == 1):#x direction
          if(p == 0):
            jointTrueOffset = parentx/2 - parentx
            otherOffset = parentx/2
            otherOffset2 = parenty/2
            otherOffset3 = parentz/2
            z = 1
          if(previous_direction == 1 or previous_direction == 0):#coming from x #SET NAME, PARENT, CHILD, POSITION, and AXIS
            self.joint_list.append(JOINT(new_joint_name, str(p), str(c), (x + parentx + jointTrueOffset), y, z))
            z = 0
          if(previous_direction == 2):#coming from y
            self.joint_list.append(JOINT(new_joint_name, str(p), str(c), (x+parentx/2 + jointTrueOffset + otherOffset), y+parenty/2 - otherOffset2, z))            
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x+length/2, y, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
          if(previous_direction == 3):#coming from z
            self.joint_list.append(JOINT(new_joint_name, str(p), str(c), (x+parentx/2 + jointTrueOffset + otherOffset), y, z+parentz/2 - otherOffset3))            
            z = 0
          #previous_direction = 1
          self.link_list[i].previous = 1
          
  if(direction == 2):#y direction
          if(p == 0):
            jointTrueOffset = parenty/2 - parenty
            otherOffset = parentx/2
            otherOffset2 = parenty/2
            otherOffset3 = parentz/2
            z = 1
          if(previous_direction == 2 or previous_direction == 0):#coming from y
            self.joint_list.append(JOINT(new_joint_name, str(p), str(c), x, y+parenty+jointTrueOffset, z))
            z = 0
          if(previous_direction == 1):#coming from x
            self.joint_list.append(JOINT(new_joint_name, str(p), str(c), x+parentx/2 - otherOffset, y + parenty/2 + jointTrueOffset + otherOffset2, z))
            z = 0
          if(previous_direction == 3):#coming from z
            self.joint_list.append(JOINT(new_joint_name, str(p), str(c), x, y + parenty/2 + jointTrueOffset + otherOffset2, z+parentz/2 - otherOffset3))
            z = 0
          self.link_list[i].previous = 2
        
        
      
    
    
    
    
    
    
    
    
    
    #udpate previous direction PUT THIS AFTER ACTUALLY PLACING JOINTS
    self.link_list[c].previous = 1
    

  
  def Create_Body(self):##############################################################
    self.get_sensor = []
    self.num_sensors = 0
    self.num_motors = 0
    self.coordinates = []
    self.link_list = []
    self.added_links = []
    self.joint_list = []
    height_offset = 1
    x = self.x
    y = self.y
    z = self.z + height_offset
    joint_offset = 1
    width_offset = 0
    length_offset = 0
    z_offset = 0
    previous_child = 99


    pyrosim.Start_URDF("body" + str(self.myID) + ".urdf")
    
    ##############################################
    self.get_sensor = []
    self.link_list = []
    
    #OLD ADDING LINKS TO LINK LIST
    #for j in range(self.max):
    #  self.link_list.append(LINK())
    #  if(j == 0):
    #    self.link_list[j].x += c.dx
        #self.link_list[j].y += self.vy
        #self.link_list[j].z += self.vz
    
    #OLD RESETTING OCCUPIED FOR LINKS
    for i, l in enumerate(self.link_list):
      l.occupied = [0, 0, 0, 0, 0, 0]
    
    self.joint_list = []  

    
    for i, link in enumerate(self.link_list):
      if(i == 0):
        previous_direction = 0
        parentx = link.x
        parenty = link.y
        parentz = link.z
      #print("Previous Direction: " + str(previous_direction))
      length = link.x
      width = link.y
      height = link.z
      direction = random.randint(1,3)
      #direction = random.choice([1, 2])
      #direction = 3

      jointTrueOffset = 0
      otherOffset = 0
      otherOffset2 = 0  
      otherOffset3 = 0
      
      #initial cube
      if(i == 0):
        pyrosim.Send_Cube(name = str(i), pos = [x, y, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
        #add sensors based on color
        self.SendSensor(link)
        self.added_links.append(i)
      else:
        #choose random parent link and add joint and link
        p = random.choice(self.added_links)
        
        while(sum(self.link_list[p].occupied) == 3):
          p = random.choice(self.added_links)
        while(self.link_list[p].occupied[direction-1] != 0):#MIGHT TIME OUT IF ALL OF OCCUPIED IS FULL
          direction = random.randint(1,3)
          #direction = random.choice([1, 2])
        self.link_list[p].occupied[direction-1] = 1
        #print(self.link_list[i].occupied)
        self.link_list[i].occupied[direction+2] = 1
        #print("Direction: " + str(direction))
          
        parentx = self.link_list[p].x
        parenty = self.link_list[p].y
        parentz = self.link_list[p].z
        #add and store newest link
        self.added_links.append(i)
        #make new joint and link
        new_joint_name = str(p) + "_" + str(i)
        z = 0

        if(i > 0 and p!= 0):
          previous_direction = self.link_list[p].previous
        
        '''
        if(direction == 1):#x direction
          if(p == 0):
            jointTrueOffset = parentx/2 - parentx
            otherOffset = parentx/2
            otherOffset2 = parenty/2
            otherOffset3 = parentz/2
            z = 1
          if(previous_direction == 1 or previous_direction == 0):#coming from x
            #print("xx")
            pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x + parentx + jointTrueOffset, y, z], jointAxis = "0 1 0")  
            self.joint_list.append(new_joint_name)
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x+length/2, y, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
          if(previous_direction == 2):#coming from y

            pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x+parentx/2 + jointTrueOffset + otherOffset, y+parenty/2 - otherOffset2, z], jointAxis = "0 1 0")  
            self.joint_list.append(new_joint_name)
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x+length/2, y, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
          if(previous_direction == 3):#coming from z
            #print("zx")
            pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x+parentx/2 + jointTrueOffset + otherOffset, y, z+parentz/2 - otherOffset3], jointAxis = "0 1 0")  
            self.joint_list.append(new_joint_name)
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x+length/2, y, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
          previous_direction = 1
          self.link_list[i].previous = 1
          self.SendSensor(link)
        
        if(direction == 2):#y direction
          if(p == 0):
            jointTrueOffset = parenty/2 - parenty
            otherOffset = parentx/2
            otherOffset2 = parenty/2
            otherOffset3 = parentz/2
            z = 1
          if(previous_direction == 2 or previous_direction == 0):#coming from y
            pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x, y+parenty+jointTrueOffset, z], jointAxis = "0 1 0")  
            self.joint_list.append(new_joint_name)
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x, y+width/2, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
          if(previous_direction == 1):#coming from x
            #print("jointoffset = " + str(jointTrueOffset) + " otheroffset = " + str(otherOffset) + "otheroffset2 = " + str(otherOffset2))
            pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x+parentx/2 - otherOffset, y + parenty/2 + jointTrueOffset + otherOffset2, z], jointAxis = "0 1 0")  
            self.joint_list.append(new_joint_name)
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x, y+width/2, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
          if(previous_direction == 3):#coming from z
            pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x, y + parenty/2 + jointTrueOffset + otherOffset2, z+parentz/2 - otherOffset3], jointAxis = "0 1 0")  
            self.joint_list.append(new_joint_name)
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x, y+width/2, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
          previous_direction = 2
          self.link_list[i].previous = 2
          self.SendSensor(link)
          
        if(direction == 3):#z direction
          if(p == 0):
            jointTrueOffset = parentz/2 - parentz
            otherOffset = parentx/2
            otherOffset2 = parenty/2
            otherOffset3 = parentz/2
            z = 1
          if(previous_direction == 3 or previous_direction == 0):#coming from z
            #print("zz")
            pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x, y, z+parentz+jointTrueOffset], jointAxis = "0 1 0")  
            self.joint_list.append(new_joint_name)
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x, y, z+height/2], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)

          if(previous_direction == 1):#coming from x
            #print("xz")
            pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x+parentx/2 - otherOffset, y, z + parentz/2 + jointTrueOffset + otherOffset3], jointAxis = "0 1 0")  
            self.joint_list.append(new_joint_name)
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x, y, z+height/2], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)

          if(previous_direction == 2):#coming from y
            #print("yz")
            pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x, y+parenty/2 - otherOffset2, z + parentz/2 + jointTrueOffset + otherOffset3], jointAxis = "0 1 0")  
            self.joint_list.append(new_joint_name)
            z = 0
            pyrosim.Send_Cube(name = str(i), pos = [x, y, z+height/2], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)

          previous_direction = 3
          self.link_list[i].previous = 3
          self.SendSensor(link)
          '''
          
      if(i > 0):    
        previous_child = i
      previousx = link.x
      previousy = link.y
      previousz = link.z
          
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
      pyrosim.Send_Motor_Neuron(name = sensor_number, jointName = joint.name)
      #print("name = " + str(sensor_number) + " jointName = " + str(joint))
      sensor_number = sensor_number + 1
    self.num_sensors = numpy.sum(self.get_sensor)
    self.num_motors = len(self.joint_list)

      

    
    #for currentRow in range(0, c.numSensorNeurons):##################
    for currentRow in range(0, self.num_sensors):
      for currentColumn in range(0, self.num_motors):
        pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + self.num_sensors, weight = self.weights[currentRow][currentColumn])
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
    randomColumn = random.randint(0, self.num_motors-1)
    self.weights[randomRow, randomColumn] =  random.random() * 2 - 1
    
    #Add joint and extend one link

    
  def Set_ID(self, nextAvailableID):
    self.myID = nextAvailableID
    
