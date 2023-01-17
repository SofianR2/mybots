import pybullet as p
from world import WORLD
from robot import ROBOT
class SIMULATION:
  def __init__(self):
    self.physicsClient = p.connect(p.GUI)
    self.world = WORLD()
    self.robot = ROBOT()    
    p.setAdditionalSearchPath(pybullet_data.getDataPath())
    p.setGravity(0,0,-9.8)
    pyrosim.Prepare_To_Simulate(robotId)
