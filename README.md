# Social Network Analysis Assignments

graph.py and row.py contain classes and methods to read in [Rollcall data for U.S. Legislatures](https://github.com/m-clark/Datasets/tree/master/rollcall) as a social network data structure, in which legislators are nodes in a complete graph. Edge weights, or tie strengths, correspond to the intersection of one legislator's voting pattern against another. Specifically, + 1 tie strength for each yes or no vote they have in common, and -1 for each vote they diverged on.

Properties of nodes:
- String Name
- String Party
- String State
- Set<Int> Votes in which they voted yes
- Set<Int> Votes in which they voted no

Properties of edges:
- Int Tie Strength (determined by voting similarity)
- Bool Same or Different Party
- Bool Same or Different State

