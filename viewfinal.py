from parallelHillClimber import PARALLEL_HILL_CLIMBER
import os
import numpy as np
import random
import matplotlib.pyplot as plt
import constants as c
import pickle
import time



with open ("best3.txt", "rb") as f:
  p = pickle.load(f)
p[0].Start_Simulation("GUI")
