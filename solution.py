import numpy
import pyrosim.pyrosim as pyrosim

class SOLUTION:
  def __init__(self):
    self.weights = numpy.random.rand(3,2)
    self.weights = self.weights * 2 - 1
    
  def Evaluate(self):
    pass
  
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
    #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 3 , weight = 1.0 )
    #pyrosim.Send_Synapse( sourceNeuronName = 1 , targetNeuronName = 3 , weight = 1.0 )
    #pyrosim.Send_Synapse( sourceNeuronName = 0 , targetNeuronName = 4 , weight = -0.5 )
    #pyrosim.Send_Synapse( sourceNeuronName = 2 , targetNeuronName = 4 , weight = -0.5 )
    for i in [0, 1, 2]:
      for j in [3, 4]:
        pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j , weight = random.randrange(-1, 1))
    pyrosim.End()
