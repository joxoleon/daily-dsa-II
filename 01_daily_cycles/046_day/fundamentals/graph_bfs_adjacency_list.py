# [ Name: Graph BFS — Adjacency List ]  [ Category: graphs ]  [ Topic: bfs ]  [ Weight: 7 ]

"""
Problem Description:
Given an undirected graph represented as an adjacency list and a starting node, perform a breadth-first search (BFS). 
Return the list of nodes visited in BFS order, starting from the 'start' node.
If a node has multiple neighbors, visit them in the order provided by the adjacency list.
Assume all nodes in the input graph are labeled as integers from 0 upwards.
If the start node is not in the graph, return an empty list.

Constraints:
- 0 <= number of nodes <= 10^5
- No duplicate edges; no self-loops
- The adjacency list may be empty.

Example:
Input: graph = {0: [1, 2], 1: [0], 2: [0]}, start = 0 -> Output: [0, 1, 2]
"""

from typing import List, Dict

def bfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert bfs({0: [1, 2], 1: [0], 2: [0]}, 0) == [0, 1, 2]
    assert bfs({0: [1], 1: [0]}, 0) == [0, 1]
    assert bfs({0: [], 1: [2], 2: [1]}, 1) == [1, 2]
    assert bfs({}, 0) == []
    assert bfs({3: [4], 4: [3]}, 3) == [3, 4]
    assert bfs({0: [1], 1: [2], 2: [0]}, 0) == [0, 1, 2]
    assert bfs({5: [6, 7], 6: [5], 7: [5]}, 5) == [5, 6, 7]
    assert bfs({0: [1, 2, 3], 1: [], 2: [], 3: []}, 0) == [0, 1, 2, 3]
    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
