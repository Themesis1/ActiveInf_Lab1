# -*- coding: utf-8 -*-
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
# LAB: 1.2
# TITLE: The Graph as a World Model
# DATE: 2026-06-17
# VERSION: 1.0
#
#===================================================================================================
# WHAT THIS LAB DOES:
#===================================================================================================
#
# Introduces the Python package networkx as a tool for representing
# a simple world as a graph — nodes are locations, edges are connections.
# This is the foundation for the active inference grid world we will
# build across Labs 1.3 through 1.6.
#
# By the end of this lab you will:
#   (1) Build a simple graph with named nodes and edges
#   (2) Visualize it as a network diagram
#   (3) Query the graph to understand its structure
#
#===================================================================================================
# QUESTIONS: themesisinc1@gmail.com
# GITHUB: https://github.com/Themesis1/ActiveInf_Lab1
#===================================================================================================


# Lab 1.2 - The Graph as a World Model
# Themesis Active Inference Lab Course
# Building Active Inference in Python
#
# Goal: Build a simple graph and visualize it.
# This is your first "world" - nodes are locations,
# edges are connections between them.

import networkx as nx
import matplotlib.pyplot as plt

# Build a simple world - 5 locations
G = nx.Graph()

# Add nodes - these are locations in our world
G.add_nodes_from([0, 1, 2, 3, 4])

# Add edges - these are connections between locations
G.add_edges_from([
    (0, 1),  # location 0 connects to location 1
    (1, 2),  # location 1 connects to location 2
    (2, 3),  # location 2 connects to location 3
    (3, 4),  # location 3 connects to location 4
    (1, 3),  # location 1 also connects to location 3
])

# Give locations meaningful names
labels = {
    0: "Start",
    1: "Room A",
    2: "Hallway",
    3: "Room B",
    4: "Goal"
}

# Set the layout - controls how nodes are positioned visually
pos = nx.spring_layout(G, seed=42, k=2)

# Draw the world
plt.figure(figsize=(8, 5))
nx.draw(G, 
        labels=labels,
        with_labels=True,
        node_color='#e8f4f8',  # light teal - Themesis colors!
        node_size=2000,
        font_size=11,
        font_color='#1a4a5e',
        edge_color='#2a6070',
        width=2)
plt.title("Lab 1.2 — My First World Model", 
          fontsize=13, 
          color='#1a4a5e')
plt.tight_layout()
plt.show()

# Now let's ask some questions about our world
print("Number of locations:", G.number_of_nodes())
print("Number of connections:", G.number_of_edges())
print("Neighbors of Room A:", 
      list(G.neighbors(1)))
print("Can I get from Start to Goal directly?", 
      G.has_edge(0, 4))
