from hillclimber import HILLCLIMBER
import os

hc = HILLCLIMBER()
hc.Evolve()
hc.Show_Best()

#for x in range(1, 6):
#  os.system("python3 generate.py")
#  os.system("python3 simulate.py")
