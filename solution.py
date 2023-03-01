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
    self.z=0
    self.max = 7
    self.get_sensor = []
    self.num_sensors = 0
    self.num_motors = 0
    self.coordinates = []
    self.link_list = []
    self.added_links = []
    self.joint_list = []
    self.counter = 0
    
    
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
      
  '''
  def Directional_Cube(self, direction, new_joint_name, p, i):
    if(direction == 1):
      #check that we're not going back in the same direction
      #move in direction
      pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x + length + jointTrueOffset, y, z], jointAxis = "0 1 0")  
      self.joint_list.append(new_joint_name)
      z = 0
      pyrosim.Send_Cube(name = str(i), pos = [x+length/2, y, z], size = [link.x, link.y, link.z], color = link.color, cname = link.color_name)
      if(link.color ==  '    <color rgba="0.0 0.0 1.0 1.0"/>'):
        self.get_sensor.append(1)
      else:
        self.get_sensor.append(0)
      
    if(direction == 2):
      pass
    if(direction == 3):
      pass    
   '''
   

  def SendSensor(self, link):
    if(link.color ==  '    <color rgba="0.0 0.0 1.0 1.0"/>'):
      self.get_sensor.append(1)
    else:
      self.get_sensor.append(0)
  
  def Create_Body(self):
    #self.get_sensor = []
    #self.num_sensors = 0
    #self.num_motors = 0
    #self.coordinates = []
    #self.link_list = []
    #self.added_links = []
    #self.joint_list = []
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
    #self.link_list = []
    if(self.link_list == []):
      for j in range(self.max):
        self.link_list.append(LINK())
      
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


          #print("Previous Direction: " + str(previous_direction))
          #print("Direction: " + str(direction))
          #########
          if(i > 0 and p!= 0):
            previous_direction = self.link_list[p].previous

          if(direction == 1):#x direction
            #if(previous_child != p and i > 0):
              #previous_direction = 0
            #if(previous_direction == 2):
              #if(self.link_list[p].occupied[4] == 0):
                #otherOffset = parentx/2
                #otherOffset2 = parenty/2
                #otherOffset3 = parentz/2
            #if(previous_direction == 3):
              #if(self.link_list[p].occupied[5] == 0):
                #otherOffset = parentx/2
                #otherOffset2 = parenty/2
                #otherOffset3 = parentz/2
          #########
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
              #print("yx")
              #print("jointoffset = " + str(jointTrueOffset) + " otheroffset = " + str(otherOffset) + "otheroffset2 = " + str(otherOffset2))
              #if(self.link_list[p].occupied[4] == 0 and i != 0):
              #  pyrosim.Send_Joint(name = new_joint_name, parent= str(p), child = str(i), type = "revolute", position = [x+parentx, y, z], jointAxis = "0 1 0")  
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
            #if(previous_child != p and i > 0):
              #previous_direction = 0
            ####################
            #if(previous_direction == 1):
              #if(self.link_list[p].occupied[3] == 0):
                #otherOffset = parentx/2
                #otherOffset2 = parenty/2
                #otherOffset3 = parentz/2
            #if(previous_direction == 3):
              #if(self.link_list[p].occupied[5] == 0):
                #otherOffset = parentx/2
                #otherOffset2 = parenty/2
                #otherOffset3 = parentz/2
            ####################

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
            #if(previous_child != p and i > 0):
              #previous_direction = 0
              #if(previous_direction == 1):
                #if(self.link_list[p].occupied[3] == 0):
                  #otherOffset = 1.5
                  #otherOffset2 = 1.5
                  #otherOffset3 = 1.5
              #if(previous_direction == 2):
                #if(self.link_list[p].occupied[4] == 0):
                  #otherOffset = parentx/2
                  #otherOffset2 = parenty/2
                  #otherOffset3 = parentz/2
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
      pyrosim.Send_Motor_Neuron(name = sensor_number, jointName = joint)
      #print("name = " + str(sensor_number) + " jointName = " + str(joint))
      sensor_number = sensor_number + 1
    print(self.get_sensor)
    self.num_sensors = numpy.sum(self.get_sensor)
    self.num_motors = len(self.joint_list)

      

    
    #for currentRow in range(0, c.numSensorNeurons):##################
    print(self.num_sensors)
    for currentRow in range(0, self.num_sensors):
      for currentColumn in range(0, self.num_motors):
        #pyrosim.Send_Synapse(sourceNeuronName = currentRow , targetNeuronName = currentColumn + c.numSensorNeurons, weight = self.weights[currentRow][currentColumn])#######
        #print(self.weights)
        #print(currentRow)
        #print(currentColumn)
        #print(self.num_sensors)
        #print(self.num_motors)
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
    
    #self.link_list.append(LINK())
    
    #random.choice(self.link_list).x += 5
    #self.max += 1
    #c.numSensorNeurons += 1
    #c.numMotorNeurons += 1

    
  def Set_ID(self, nextAvailableID):
    self.myID = nextAvailableID
    
