"""
Graham Harris
Summer Data Project
Takes the output of adjacency.py and creates a visual network.
"""

import networkx as nx
import pandas as pd
from pyvis.network import Network 

# -------------- MAIN --------------

teams = pd.read_csv("../data/adjacent_teams.csv")

T = nx.from_pandas_edgelist(teams, source="Source", target="Target", edge_attr="Weight")

nett = Network(notebook=True)

# Teams
print("Writing teams...\n")
nett.from_nx(T)
nett.show_buttons(filter_=['physics'])
nett.show("../html/adjacency_teams.html")
