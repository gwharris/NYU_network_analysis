"""
Graham Harris
Summer Data Project
Takes the output of adjacency.py and creates a visual network.
"""

import networkx as nx
import pandas as pd
from pyvis.network import Network 

# -------------- MAIN --------------

people = pd.read_csv("../data/adjacent_people.csv")

P = nx.from_pandas_edgelist(people, source="Source", target="Target", edge_attr="Weight")

netp = Network(notebook=True)

# People
print("Writing people...\n")
netp.from_nx(P)
netp.show_buttons(filter_=['physics'])
netp.show("../html/adjacency_people.html")