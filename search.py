from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import constants as c
import pickle
'''
os.system("del world*.sdf")
np.random.seed(1)
random.seed(1)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best1.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph1 = phc.max

os.system("del world*.sdf")
np.random.seed(2)
random.seed(2)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best2.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph2 = phc.max
'''
os.system("del world*.sdf")
np.random.seed(3)
random.seed(3)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best3.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph3 = phc.max

os.system("del world*.sdf")
np.random.seed(4)
random.seed(4)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best4.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph4 = phc.max

os.system("del world*.sdf")
np.random.seed(5)
random.seed(5)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best5.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph5 = phc.max

os.system("del world*.sdf")
np.random.seed(6)
random.seed(6)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best6.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph6 = phc.max

os.system("del world*.sdf")
np.random.seed(7)
random.seed(7)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best7.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph7 = phc.max

os.system("del world*.sdf")
np.random.seed(8)
random.seed(8)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best8.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph8 = phc.max

os.system("del world*.sdf")
np.random.seed(9)
random.seed(9)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best9.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph9 = phc.max

os.system("del world*.sdf")
np.random.seed(10)
random.seed(10)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
input("Press Enter to Continue")
phc.Show_Best()
with open('best10.txt', 'wb') as f:
  pickle.dump(phc.best, f)
  f.close()
phc.GraphBest()
graph10 = phc.max

plt.plot(graph1)
plt.plot(graph2)
plt.plot(graph3)
plt.plot(graph4)
plt.plot(graph5)
plt.plot(graph6)
plt.plot(graph7)
plt.plot(graph8)
plt.plot(graph9)
plt.plot(graph10)

plt.xticks(range(0, c.numberOfGenerations+1))
plt.xlabel("Generation")
plt.ylabel("Fitness")
plt.title("Fitness Evolution")

labels = []
for i in range(c.populationSize):
  labels.append("Seed " + str(i + 1))
plt.legend(labels)

plt.show()      

#for x in range(1, 6):
#  os.system("python3 generate.py")
#  os.system("python3 simulate.py")
