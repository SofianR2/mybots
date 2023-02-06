import pybullet as p

class WORLD:
  def __init__(self, solutionID):
    self.planeId = p.loadURDF("plane.urdf")
    p.loadSDF("world.sdf")
    p.loadSDF("world" + str(solutionID) + ".sdf")
    

