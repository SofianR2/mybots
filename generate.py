import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
length = 1
width = 1
height = 1
x=0
y=0
z=0

pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])

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

pyrosim.End()
