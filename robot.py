class ROBOT:
  def __init__(self):
    self.sensor = {}
    self.motor = {}
    self.robotId = p.loadURDF("body.urdf")
