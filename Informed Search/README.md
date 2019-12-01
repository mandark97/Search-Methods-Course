# Informed Search Problem

## Pathfinding in a maze

Given a maze (represented as a matrix with 1 values being the walls), find the shortest path to reach the destination. 

### Proposed Algorithms

The general approach for this problem is named **best-first search**. Best-first search is an instance of the GRAPH-SEARCH algorithm in which a node is selected for expansion based on an **evaluation function** *f(n)*. The node with the lowest evaluation is expanded first. Most best-first algorithms include an component names **heuristic function** *h(n)*.

Based on the chosen **evaluation function** we present two algorithms:

- Greedy best-first search
- A* search

#### Greedy best-first search

**Greedy best-first search** tries to expand the node that is closest to the goal. In this case *f(n) = h(n)*. This algorithm doesn't guarantee the optimal solution.

#### A* search

**A\* search** evaluates nodes by combining **the cost to reach the node** *g(n)*, and *h(n)* the estimated cost of the cheapest path. The **evaluation function** is *f(n) = h(n) + g(n)*. This algorithm finds the optimal solution.
