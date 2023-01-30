from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
  def __init__(self):
    self.parents = {}
    for i in range(0, c.populationSize-1):
      self.parents[i] = SOLUTION()
      print(self.parents[i])
    
  def Spawn(self):
    self.child = copy.deepcopy(self.parent)
  
  def Mutate(self):
    self.child.Mutate()
  
  def Select(self):
    if(self.parent.fitness > self.child.fitness):
      self.parent = self.child
  
  def Evolve_For_One_Generation(self):
    self.Spawn()
    self.Mutate()
    self.child.Evaluate("DIRECT")
    self.Print()
    self.Select()
    
  def Evolve(self):
    for i in range(0, c.populationSize-1):
      print(self.parents[i])
      #self.parents[i].Evaluate("GUI")
#    self.parent.Evaluate("GUI")
#    for currentGeneration in range(c.numberOfGenerations):
#      self.Evolve_For_One_Generation()
      
  def Print(self):
    print(self.parent.fitness, self.child.fitness)
    
  def Show_Best(self):
    pass
    #self.parent.Evaluate("GUI")
