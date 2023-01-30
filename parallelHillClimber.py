from solution import SOLUTION
import constants as c
import copy

class PARALLEL_HILL_CLIMBER:
  def __init__(self):
    self.parents = {}
    self.nextAvailableID = 0
    for i in range(0, (c.populationSize)):
      self.parents[i] = SOLUTION(self.nextAvailableID)
      self.nextAvailableID += 1
    
  def Spawn(self):
    self.child = copy.deepcopy(self.parent)
    self.child.Set_ID(self.nextAvailableID)
    self.nextAvailableID += 1
  
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
    for i in range(0, c.populationSize):
      self.parents[i].Start_Simulation("GUI")
      print("HELLOOOOOOOOOOOOOOOOOOOOOO")
    for j in range(0, c.populationSize):
      print("HELLOOOOOOOOOOOOOOOOOOOOOO")
      self.parents[i].Wait_For_Simulation_To_End()
      
    #for i in range(0, c.populationSize):
      #print(self.parents[i])
      #self.parents[i].Evaluate("GUI")
      #self.parents[i].Start_Simulation("GUI")
#    self.parent.Evaluate("GUI")
#    for currentGeneration in range(c.numberOfGenerations):
#      self.Evolve_For_One_Generation()  
  def Print(self):
    print(self.parent.fitness, self.child.fitness)
    
  def Show_Best(self):
    pass
    #self.parent.Evaluate("GUI")
