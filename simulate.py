import pybullet as p
import time
import pybullet_data

physicsClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

p.setGravity(0,0,-9.8)
planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF("body.urdf")
p.loadSDF("world.sdf")

for x in range(1000):
  p.stepSimulation()
  backLegTouch = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
  time.sleep(1/60)
  print(x)
p.disconnect()
