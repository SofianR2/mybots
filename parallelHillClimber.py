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
    self.fitness = numpy.empty((c.numberOfGenerations+1, c.populationSize))###########one generation
    self.max = []########### stores max of generations
    self.currentgeneration = 0
    self.best = []
    
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
  
  def AddBest(self):###############################################
    #for i in self.parents:
    #  self.fitness[self.currentgeneration][i] = -self.parents[i].fitness
    #self.currentgeneration = self.currentgeneration + 1
    
    for i in self.parents:
      best = self.parents[0]
    for i in self.parents:
      if (self.parents[i].fitness < best.fitness):
        best = self.parents[i]
    self.max.append(-best.fitness)
    
  def GraphBest(self):#############################################
    #for i in self.fitness:
    #for j in range(c.numberofGenerations):
    #  self.max.append(self.fitness[j][0])
    
    #print(self.max)
    #print(self.fitness)
    #plt.plot(range(0, c.numberOfGenerations+1), self.fitness)
    plt.plot(self.max)
    plt.xticks(range(0, c.numberOfGenerations+1))
    plt.xlabel("Generation")
    plt.ylabel("Fitness")
    plt.title("Fitness Evolution")
    
    labels = []
    for i in range(c.populationSize):
      labels.append("Seed " + str(i + 1))
    plt.legend(labels)
    
    #plt.show()
    
    plt.show(block=False)
    plt.pause(11)
    plt.close()

  
  def Evolve_For_One_Generation(self):
    self.Spawn()
    self.Mutate()
    self.Evaluate(self.children)
    self.Print()
    self.Select()
    self.AddBest()
    
  def Evolve(self):
    self.Evaluate(self.parents)
    self.AddBest()
    self.currentgeneration -= 1
      
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
    self.best.append(best)
    best.Start_Simulation("GUI")
  
  def Evaluate(self, solutions):
    for i in range(0, c.populationSize):
      solutions[i].Start_Simulation("DIRECT")

    for j in range(0, c.populationSize):
      solutions[j].Wait_For_Simulation_To_End()    
