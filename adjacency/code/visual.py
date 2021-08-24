"""
Graham Harris
Summer Data Project
Takes the output of adjacency.py and creates a visual network.
"""

import networkx as nx
import pandas as pd
from pyvis.network import Network 
import sys

# -------------- MAIN --------------

for arg in sys.argv:
  try:
    df = pd.read_csv("../data/" + arg + ".csv")
    print("\nFile found: " + arg)

    net = Network(notebook=True, height="750px", width="75%")
    net.force_atlas_2based()
    net.show_buttons(filter_="physics")

    source = df['Source']
    target = df['Target']
    weight = df['Weight']

    edges = zip(source, target, weight)

    # Simplified Teams
    print("Writing nodes and edges...")
    for src, dst, wgt in edges:
      # Add nodes and edges to the graph
      net.add_node(src, src, title=src, color='#D4D4D4')
      if "Applications" in dst:
        net.add_node(dst, dst, title=dst, color='#018b95')
        net.add_edge(src, dst, color='#019ca8')
      elif "Participant" in dst:
        net.add_node(dst, dst, title=dst, color='#7908C4')
        net.add_edge(src, dst, color="#9007EB")
      else:
        net.add_node(dst, dst, title=dst, color='#707070')
        net.add_edge(src, dst, color="#707070")
  
    # net.show_buttons(filter_=['physics', 'nodes', 'edges'])
    net.show("../html/" + arg + ".html")

  except:
    print("\nunable to read argument: " + arg)