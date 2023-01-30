from solution import SOLUTION

class HILLCLIMBER:
  def __init__(self):
    self.parent = SOLUTION()
    
  def Evolve(self):
    #self.parent.Create_World()
    #self.parent.Create_Body()
    #self.parent.Create_Brain()
    self.parent.Evaluate()
