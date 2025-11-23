# [ Name: Topological Sort — Kahn's Algorithm ]  [ Category: graphs ]  [ Topic: toposort ]  [ Weight: 8 ]

"""
Problem Description:
Given a directed graph with 'num_nodes' labeled from 0 to num_nodes - 1 and a list of edges, return a possible topological ordering of its nodes.
Each edge is represented as a pair [u, v] meaning there is a directed edge from u to v.
If multiple valid orders exist, return any of them.
If the graph is not a Directed Acyclic Graph (DAG), return an empty list.

Constraints:
- 1 <= num_nodes <= 10^4
- 0 <= len(edges) <= 10^5

Example:
Input: num_nodes = 4, edges = [[0,1],[1,2],[2,3]], Output: [0,1,2,3]
"""

from typing import List

def topological_sort(num_nodes: int, edges: List[List[int]]) -> List[int]:
    pass

if __name__ == "__main__":
    assert topological_sort(4, [[0,1],[1,2],[2,3]]) in ([0,1,2,3],)
    assert topological_sort(3, [[0,1],[0,2]]) in ([0,1,2], [0,2,1])
    assert topological_sort(2, [[0,1]]) == [0,1]
    assert topological_sort(2, [[1,0]]) == [1,0]
    assert topological_sort(1, []) == [0]
    assert topological_sort(3, []) in ([0,1,2], [0,2,1], [1,0,2], [1,2,0], [2,0,1], [2,1,0])
    assert topological_sort(2, [[0,1],[1,0]]) == []
    assert topological_sort(5, [[1,0],[2,0],[3,1],[3,2],[4,3]]) in ([4,3,2,1,0], [4,3,1,2,0])

    print("All tests passed.")
