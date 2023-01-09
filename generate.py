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
  
def Create_Robot():
  pyrosim.Start_URDF("body.urdf")
  pyrosim.Send_Cube(name="Link0", pos=[x,y,z] , size=[length,width,height])
  pyrosim.Send_Joint( name = "Link0_Link1" , parent= "Link0" , child = "Link1" , type = "revolute", position = [x,y,z+0.5])
  pyrosim.Send_Cube(name="Link1", pos=[x,y,z] , size=[length,width,height])
  pyrosim.Send_Joint( name = "Link1_Link2" , parent= "Link1" , child = "Link2" , type = "revolute", position = [x,y,z+1])
  pyrosim.Send_Cube(name="Link2", pos=[x,y,z] , size=[length,width,height])
  pyrosim.End()
  
Create_World()
Create_Robot()
  
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
