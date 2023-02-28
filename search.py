from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import numpy as np
import random

np.random.seed(1)
random.seed(1)
phc = PARALLEL_HILL_CLIMBER()
phc.Evolve()
phc.Show_Best()
phc.GraphBest()

#for x in range(1, 6):
#  os.system("python3 generate.py")
#  os.system("python3 simulate.py")
