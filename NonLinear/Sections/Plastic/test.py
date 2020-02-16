#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# Explicitly move to example's directory
os.chdir(os.path.dirname(__file__))

# Run the example
os.system("../../../Scripts/param.py par.pre.fbl")
os.system("cgx -b pre.fbl")
os.system("ccx Biegung")
os.system("../../../Scripts/monitor.py Biegung")
os.system("cgx -b movie.fbl")
os.system("cgx -b chart.fbl")
