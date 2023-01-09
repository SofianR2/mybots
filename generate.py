import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("box.sdf")
length = 1
width = 1
height = 1
x = 0
y = 0
z = 0.5

for x in range(10):
  pyrosim.Send_Cube(name="Box", pos=[x,y,z] , size=[length,width,height])
  z += 1
 
  


pyrosim.End()
