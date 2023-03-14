from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import constants as c
import pickle
import time
import best1.txt as b1


with open (b1, "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)

with open ("best2.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)

with open ("best3.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)

with open ("best4.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)

with open ("best5.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)

with open ("best6.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)

with open ("best7.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)

with open ("best8.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)

with open ("best9.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)

with open ("best10.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
f.close()
time.sleep(15)
