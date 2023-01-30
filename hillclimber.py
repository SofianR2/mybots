from solution import SOLUTION
import constants as c

class HILLCLIMBER:
  def __init__(self):
    self.parent = SOLUTION()
    
  def Spawn(self):
    pass
  
  def Mutate(self):
    pass
  
  def Select(self):
    pass
  
  def Evolve_For_One_Generation(self):
    self.Spawn()
    self.Mutate()
    self.child.Evaluate()
    self.Select()
    
  def Evolve(self):
    self.parent.Create_World()
    self.parent.Create_Body()
    self.parent.Create_Brain()
    self.parent.Evaluate()
    for currentGeneration in range(c.numberOfGenerations):
      self.Evolve_For_One_Generation()
