#!/usr/bin/python
import os
import multiprocessing

# Enable multithreading for ccx
os.environ['OMP_NUM_THREADS'] = str(multiprocessing.cpu_count())

# Explicitly move to example's directory
os.chdir(os.path.dirname(__file__))

# Run the example
for contact in ('tie', 'pc-ss'):
    os.system("../../Scripts/param.py par.pre.fbd contact=\"'"+contact+"'\"")
    os.system("cgx -b pre.fbd")
    os.system("ccx Tjoint")
    os.system("cgx -b post.fbd")
