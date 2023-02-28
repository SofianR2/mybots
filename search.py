from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import constants as c

np.random.seed(1)
random.seed(1)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
#phc.GraphBest()
graph1 = phc.max

np.random.seed(2)
random.seed(2)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
#phc.GraphBest()
graph2 = phc.max

#np.random.seed(3)
#random.seed(3)
#phc = PARALLEL_HILL_CLIMBER()
#phc.Evolve()
#phc.Show_Best()
#phc.GraphBest()

#plt.xticks(range(0, c.numberOfGenerations+1))
#plt.xlabel("Generation")
#plt.ylabel("Fitness")
#plt.title("Fitness Evolution")

#labels = []
#for i in range(c.populationSize):
#  labels.append("Seed " + str(i + 1))
#plt.legend(labels)

#plt.show()      

#for x in range(1, 6):
#  os.system("python3 generate.py")
#  os.system("python3 simulate.py")
