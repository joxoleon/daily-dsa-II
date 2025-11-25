# [ Name: Connected Components — DFS Count ]  [ Category: graphs ]  [ Topic: components ]  [ Weight: 7 ]

"""
Problem Description:
Given an undirected graph with 'num_nodes' labeled from 0 to num_nodes - 1 and a list of edges, count the number of connected components in the graph.
Return an integer representing the number of connected components.
If there are no edges, each node is its own component.

Constraints:
- 0 <= num_nodes <= 10^4
- 0 <= len(edges) <= 10^5
- Edges contain valid node indices.

Example:
Input: num_nodes = 5, edges = [[0,1],[1,2],[3,4]] -> Output: 2
"""

from typing import List

def count_components(num_nodes: int, edges: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert count_components(5, [[0,1],[1,2],[3,4]]) == 2
    assert count_components(5, []) == 5
    assert count_components(3, [[0,1],[1,2],[0,2]]) == 1
    assert count_components(4, [[0,1],[2,3]]) == 2
    assert count_components(1, []) == 1
    assert count_components(0, []) == 0
    assert count_components(6, [[0,1],[2,3],[4,5]]) == 3
    assert count_components(7, [[0,1],[1,2],[3,4],[4,5]]) == 3

    print("All tests passed.")
