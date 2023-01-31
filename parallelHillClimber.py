from solution import SOLUTION
import constants as c
import copy
import os

class PARALLEL_HILL_CLIMBER:
  def __init__(self):
    os.system("del brain*.nndf")
    os.system("del fitness*.nndf")
    self.parents = {}
    self.nextAvailableID = 0
    for i in range(0, (c.populationSize)):
      self.parents[i] = SOLUTION(self.nextAvailableID)
      self.nextAvailableID += 1
    
  def Spawn(self):
    self.children = {}
    
    for i in self.parents:      
      self.children[i] = copy.deepcopy(self.parents[i])
      self.children[i].Set_ID(self.nextAvailableID)
      self.nextAvailableID += 1
    
    #self.child = copy.deepcopy(self.parent)
    #self.child.Set_ID(self.nextAvailableID)
    #self.nextAvailableID += 1
  
  def Mutate(self):
    for i in self.children:
      self.children[i].Mutate()
  
  def Select(self):
    for i in self.parents:
      if (self.parents[i].fitness > self.children[i].fitness):
        self.parents[i] = self.children[i]
  
  def Evolve_For_One_Generation(self):
    self.Spawn()
    self.Mutate()
    self.Evaluate(self.children)
    self.Print()
    self.Select()
    
  def Evolve(self):
    self.Evaluate(self.parents)
      
    for currentGeneration in range(c.numberOfGenerations):
      self.Evolve_For_One_Generation()  
      
    #for i in range(0, c.populationSize):
      #print(self.parents[i])
      #self.parents[i].Evaluate("GUI")
      #self.parents[i].Start_Simulation("GUI")
      #self.parent.Evaluate("GUI")

  def Print(self):
    for i in self.parents:
      print()
      print(self.parents[i].fitness, self.children[i].fitness)
      print()
      
  def Show_Best(self):
    best = self.parents[0].fitness
    for i in self.parents:
      if (self.parents[i].fitness < best):
        best = self.parents[i]      
    best.Start_Simulation("GUI")
  
  def Evaluate(self, solutions):
    for i in range(0, c.populationSize):
      solutions[i].Start_Simulation("DIRECT")

    for j in range(0, c.populationSize):
      solutions[j].Wait_For_Simulation_To_End()    
