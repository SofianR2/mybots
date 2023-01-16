import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy
import math
import random

backAmplitude = numpy.pi/4
backFrequency = 10
backPhaseOffset = 0

frontAmplitude = numpy.pi/8
frontFrequency = 5
frontPhaseOffset = 0

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")
pyrosim.Prepare_To_Simulate(robotId)
backLegSensorValues = numpy.zeros(1000)
frontLegSensorValues = numpy.zeros(1000)
targetAngles = numpy.zeros(1000)

#targetAngles = numpy.linspace(0, 2 * numpy.pi, 1000)
#targetAngles = numpy.sin(targetAngles) * numpy.pi/4

backTargetAngles = numpy.linspace(backPhaseOffset, 2 * numpy.pi * backFrequency, 1000)
backTargetAngles = numpy.sin(backTargetAngles) * backAmplitude

frontTargetAngles = numpy.linspace(frontPhaseOffset, 2 * numpy.pi * frontFrequency, 1000)
frontTargetAngles = numpy.sin(frontTargetAngles) * frontAmplitude

#numpy.save('data/targetAngles', targetAngles)
#exit()

for i in range(1000):
  p.stepSimulation()
  backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
  
  pyrosim.Set_Motor_For_Joint(
  bodyIndex = robotId,
  jointName = "Torso_BackLeg",
  controlMode = p.POSITION_CONTROL,
  targetPosition = backTargetAngles[i],
  maxForce = 500)
  
  pyrosim.Set_Motor_For_Joint(
  bodyIndex = robotId,
  jointName = "Torso_FrontLeg",
  controlMode = p.POSITION_CONTROL,
  targetPosition = frontTargetAngles[i],
  maxForce = 500)
  
  time.sleep(1/240)
  
numpy.save('data/backLegSensorValues.npy', backLegSensorValues)
numpy.save('data/frontLegSensorValues.npy', frontLegSensorValues)
p.disconnect()
print(backLegSensorValues)
