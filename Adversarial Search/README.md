# Adversarial Search Problem

## Tic Tac Toe and Minimax algorithms

In normal search, the optimal solution would be a sequence of actions leading to a goal state. In adversarial search, the other player will try and stop you from achieving the goal. 

There are two players, MIN and MAX, that are trying to win the game and both of them are trying to do the optimal move. MAX therefore must find a contingent strategy, which specifies MAX’s move in the initial state, then MAX’s moves in the states resulting from every possible response by MIN, then MAX’s moves in the states resulting from every possible response by MIN to those moves, and so on. 

The minimax algorithm computes the minimax decision from the current state and it uses recursive computation to find each successor state. The recursion proceeds all the way down to the leaves of the tree, and then the minimax values are backed up through the tree as the recursion unwinds.

![tic tac toe](imgs/tic&#32;tac&#32;toe.png)
