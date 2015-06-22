# Algorithms Design - Eva Tardos


## Chapter 7 - 14

We define the Escape Problem as follows. We are given a directed graph G = (V , E) (picture a network of roads). A certain collection of nodes X E V are designated as populated nodes, and a certain other collection S E V
are designated as safe nodes. (Assume that X and S are disjoint.) In case of an emergency, we want evacuation routes from the populated nodes to the safe nodes. A set of evacuation routes is defined as a set of paths in G so that (i) each node in X is the tail of one path, (ii) the last node on each path lies in S, and (iii) the paths do not share any edges. Such a set of paths gives a way for the occupants of the populated nodes to “escape” to S, without overly congesting any edge in G.

(a) Given G, X, and S, show how to decide in polynomial time whether such a set of evacuation routes exists.

## Running solution

```sh
python routes.py
```

Python dependencies:
- networkx
- matplotlib
