"""
Graham Harris
Summer Data Project
Takes the output of adjacency.py and creates a visual network.
"""

import networkx as nx
import pandas as pd
from pyvis.network import Network 

# -------------- MAIN --------------

simplified_people = pd.read_csv("../data/simplified_adjacent_people.csv")

SP = nx.from_pandas_edgelist(simplified_people, source="Source", target="Target", edge_attr="Weight")

netsp = Network(notebook=True)

# Simplified People
print("Writing simplified people...\n")
netsp.from_nx(SP)
netsp.show_buttons(filter_=['physics'])
netsp.show("../html/simplified_adjacency_people.html")
