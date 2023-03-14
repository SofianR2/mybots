from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import constants as c
import pickle
import time



with open ("best1.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")

with open ("best2.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")

with open ("best3.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")

with open ("best4.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")

with open ("best5.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")

with open ("best6.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")

with open ("best7.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")

with open ("best8.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")

with open ("best9.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")

with open ("best10.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
