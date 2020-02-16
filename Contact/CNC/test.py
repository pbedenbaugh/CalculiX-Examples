#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# Explicitly move to example's directory
os.chdir(os.path.dirname(__file__))

# Run the example
os.system("cgx -b profile.fbd")
os.system("cgx -b winkel.fbd")
os.system("cgx -b rod.fbd")
os.system("cgx -b SK.fbd")
os.system("cgx -b assembly.fbd")
os.system("ccx solve")
os.system("cgx -b post.fbd")
