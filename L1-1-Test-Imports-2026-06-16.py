# -*- coding: utf-8 -*-

####################################################################################################
#
# THEMESIS, INC. — ACTIVE INFERENCE LAB COURSE
# Building Active Inference in Python
#
#===================================================================================================
# MIT License — Copyright 2026 Themesis, Inc.
# Code created by: Alianna J. Maren; assigned to Themesis, Inc.
#===================================================================================================
#
# LAB: 1.1
# TITLE: Test Imports
# DATE: 2026-06-17
# VERSION: 1.0
#
#===================================================================================================
# WHAT THIS LAB DOES:
#===================================================================================================
#
# Confirms that your Python environment is correctly set up for the
# Themesis Active Inference Lab Course. This is your baseline check —
# run it at the start of each lab to verify all packages are working
# before proceeding to new material.
#
# By the end of this lab you will have confirmed:
#   (1) networkx is installed and accessible
#   (2) JAX (jax, jnp, jr, jtu) is installed and accessible
#   (3) jaxtyping is installed and accessible
#   (4) pymdp 1.0.3 (JAX version) is installed and accessible
#   (5) PymdpEnv is importable from pymdp.envs
#
# If all five confirmations appear in your output, your environment
# is ready for the full Lab Course series.
#
#===================================================================================================
# QUESTIONS: themesisinc1@gmail.com
# GITHUB: https://github.com/Themesis1/ActiveInf_Lab1
#===================================================================================================

import networkx as nx
from jax import numpy as jnp, random as jr, tree_util as jtu
import jaxtyping


import os
import pymdp
print(os.listdir(os.path.dirname(pymdp.__file__)))

from pymdp.envs import PymdpEnv
print("PymdpEnv imported successfully!")

# Hello World
print("Hello, World!")
print("networkx version:", nx.__version__)
print("JAX imported successfully!")
print("pymdp imported successfully!")
print(dir(pymdp))
