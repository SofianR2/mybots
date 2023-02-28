from solution import SOLUTION
import constants as c
import copy
import os
import matplotlib.pyplot as plt
import numpy

class PARALLEL_HILL_CLIMBER:
  def __init__(self):
    os.system("del brain*.nndf")
    os.system("del fitness*.txt")
    self.parents = {}
    self.nextAvailableID = 0
    self.fitness = numpy.zeros((c.numberOfGenerations, c.populationSize))###########one generation
    self.max = []########### stores max of generations
    self.currentgeneration = 0
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
  
  def AddBest(self, currentgeneration):###############################################
    for i in self.parents:
      self.fitness[currentgeneration][i]
    self.currentgeneration = self.currentgeneration + 1
    
    for i in self.parents:
      best = self.parents[0]
    for i in self.parents:
      if (self.parents[i].fitness < best.fitness):
        best = self.parents[i]
    self.max.append(-best.fitness)
    
  def GraphBest(self):#############################################
    for i in self.fitness:
      for j in range(c.numberofGenerations):
        self.max[i].append(self.fitness[j][i])
      plt.plot(self.max,label='PHC')
      self.max = []
    plt.show()
      
  
  def Evolve_For_One_Generation(self):
    self.Spawn()
    self.Mutate()
    self.Evaluate(self.children)
    self.Print()
    self.Select()
    self.AddBest(self.currentgeneration)
    
  def Evolve(self):
    self.Evaluate(self.parents)
      
    for currentGeneration in range(c.numberOfGenerations):
      self.Evolve_For_One_Generation()  
      
    #for i in range(0, c.populationSize):
      #print(self.parents[i])
      #self.parents[i].Evaluate("GUI")
      #self.parents[i].Start_Simulation("GUI")
      #self.parent.Evaluate("GUI")

  def Print(self):################################## CHANGE THIS TO PRINT FITNESS
    for i in self.parents:
      pass
      #print()
      #print(self.parents[i].fitness, self.children[i].fitness)
      #print()
      
  def Show_Best(self):
    best = self.parents[0]
    for i in self.parents:
      if (self.parents[i].fitness < best.fitness):
        best = self.parents[i]
    best.Start_Simulation("GUI")
  
  def Evaluate(self, solutions):
    for i in range(0, c.populationSize):
      solutions[i].Start_Simulation("DIRECT")

    for j in range(0, c.populationSize):
      solutions[j].Wait_For_Simulation_To_End()    
