"""
Graham Harris
Summer Data Project
Takes the output of adjacency.py and creates a visual network.
"""

import networkx as nx
import pandas as pd
from pyvis.network import Network 

# -------------- MAIN --------------

simplified_teams = pd.read_csv("../data/simplified_adjacent_teams.csv")

ST = nx.from_pandas_edgelist(simplified_teams, source="Source", target="Target", edge_attr=["Weight","Color"])

netst = Network(notebook=True)

# Simplified Teams
print("Writing simplified teams...\n")
netst.from_nx(ST)
netst.show_buttons(filter_=['physics', 'nodes', 'edges'])
netst.show("../html/simplified_adjacency_teams.html")
