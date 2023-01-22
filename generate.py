import pyrosim.pyrosim as pyrosim
  
length = 1
width = 1
height = 1
x=0
y=0
z=0.5

def Create_World():
  pyrosim.Start_SDF("world.sdf")
  pyrosim.Send_Cube(name="Box", pos=[x-2,y+2,z] , size=[length,width,height])
  pyrosim.End()
  
def Generate_Body():
  pyrosim.Start_URDF("body.urdf")
  pyrosim.Send_Cube(name="Torso", pos=[x,y,z+1] , size=[length,width,height])
  pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" , child = "BackLeg" , type = "revolute", position = [x-0.5,y,z+0.5])
  pyrosim.Send_Cube(name="BackLeg", pos=[x-0.5,y,z-1] , size=[length,width,height])
  pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" , child = "FrontLeg" , type = "revolute", position = [x+0.5,y,z+0.5])
  pyrosim.Send_Cube(name="FrontLeg", pos=[x+0.5,y,z-1] , size=[length,width,height])
  pyrosim.End()
  
def Generate_Brain():
  pyrosim.Start_NeuralNetwork("brain.nndf")
  pyrosim.Send_Sensor_Neuron(name = 0 , linkName = "Torso")
  pyrosim.Send_Sensor_Neuron(name = 1 , linkName = "BackLeg")
  pyrosim.Send_Sensor_Neuron(name = 2 , linkName = "FrontLeg")
  pyrosim.Send_Motor_Neuron( name = 3 , jointName = "Torso_BackLeg")
  pyrosim.Send_Motor_Neuron( name = 4 , jointName = "Torso_FrontLeg")
  pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0 )
  #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
  #pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 3 , weight = 1.0 )
  pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 4 , weight = 1.0 )
  pyrosim.End()
  
def Create_Robot():
  pass
  #pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length,width,height])
  #pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [x,y,z+0.5])
  #pyrosim.Send_Cube(name="Link1", pos=[x,y,z] , size=[length,width,height])
  #pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [x,y,z+0.5])
  #pyrosim.Send_Cube(name="Link2", pos=[x,y,z] , size=[length,width,height])
  #pyrosim.Send_Joint( name = "Link2_Link3" , parent= "Link2" , child = "Link3" , type = "revolute", position = [x,y+0.5,z-0.5])
  #pyrosim.Send_Cube(name="Link3", pos=[x,y+0.5,z] , size=[length,width,height])
  #pyrosim.Send_Joint( name = "Link3_Link4" , parent= "Link3" , child = "Link4" , type = "revolute", position = [x,y+1,z-0.5])
  #pyrosim.Send_Cube(name="Link4", pos=[x,y+0.5,z] , size=[length,width,height])
  #pyrosim.Send_Joint( name = "Link4_Link5" , parent= "Link4" , child = "Link5" , type = "revolute", position = [x,y+0.5,z-0.5])
  #pyrosim.Send_Cube(name="Link5", pos=[x,y,z-1] , size=[length,width,height])
  #pyrosim.Send_Joint( name = "Link5_Link6" , parent= "Link5" , child = "Link6" , type = "revolute", position = [x,y,z-1.5])
  #pyrosim.Send_Cube(name="Link6", pos=[x,y,z-1] , size=[length,width,height])

Create_World()
Create_Robot()
Generate_Body()
Generate_Brain()
  
#x = 0
#y = 0
#z = 0.5
#for j in range(5):
#  for k in range(5):
#    for i in range(10):
#      pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
#      z += 1
#      length = 0.9*length
#      width = 0.9*width
#      height = 0.9*height
#    z = 0.5
#    y += 1
#    length = 1
#    width = 1
#    height = 1
#  y = 0
#  z = 0.5
#  x += 1
#  length = 1
#  width = 1
#  height = 1
  
  
 
  
# pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
# pyrosim.Send_Cube(name="Box2", pos=[x + 1,y,z + 1] , size=[length,width,height])

#pyrosim.End()
