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

try:
  line = sys.argv[1] # Get file name

  df = pd.read_csv("../data/" + line + ".csv")

  # ST = nx.from_pandas_edgelist(df, source="Source", target="Target", edge_attr=["Weight"])

  net = Network(notebook=True, height="750px", width="75%")
  net.force_atlas_2based()
  net.show_buttons(filter_="physics")

  source = df['Source']
  target = df['Target']
  weight = df['Weight']

  edges = zip(source, target, weight)

  subfunnel = ["JSprint", "SLP", "Summer Sprint"]
  applications = ["Bootcamp Apps", "Summer Applicants"]
  temp = []
  for i in range(2018, 2022):
    year = str(i)
    for s in subfunnel:
      temp.append(s + " " + year)
  subfunnel = subfunnel + temp

  # Simplified Teams
  print("\nWriting nodes and edges...\n")
  for src, dst, wgt in edges:
    # Add nodes and edges to the graph
    net.add_node(src, src, title=src, color='#D4D4D4')
    if dst in applications:
      net.add_node(dst, dst, title=dst, color='#02aebb')
      net.add_edge(src, dst, color='#1ac8d9')
    if dst in subfunnel:
      net.add_node(dst, dst, title=dst, color='#7908C4')
      net.add_edge(src, dst, color="#9007EB")
    else:
      net.add_node(dst, dst, title=dst, color='#707070')
      net.add_edge(src, dst, color="#707070")
  
  # net.show_buttons(filter_=['physics', 'nodes', 'edges'])
  net.show("../html/" + line + ".html")

except:
  print("\nunable to read argument 1\n")