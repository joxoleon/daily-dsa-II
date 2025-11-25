# [ Name: Cycle Detection — Undirected Graph ]  [ Category: graphs ]  [ Topic: cycle_detection ]  [ Weight: 7 ]

"""
Problem Description:
Given an undirected graph with num_nodes labeled from 0 to num_nodes - 1 and a list of edge pairs, determine if the graph contains at least one cycle.
Return True if a cycle exists, otherwise return False.

Constraints:
- 0 <= num_nodes <= 10^5
- 0 <= len(edges) <= 2 * 10^5
- The graph may be disconnected.
- Edges are given as pairs [u, v] where u != v.

Example:
Input: num_nodes = 3, edges = [[0,1],[1,2],[2,0]] -> Output: True
"""

from typing import List

def has_cycle_undirected(num_nodes: int, edges: List[List[int]]) -> bool:
    pass

if __name__ == "__main__":
    assert has_cycle_undirected(3, [[0, 1], [1, 2], [2, 0]]) == True
    assert has_cycle_undirected(4, [[0, 1], [1, 2], [2, 3]]) == False
    assert has_cycle_undirected(5, [[0, 1], [1, 2], [2, 0], [3, 4]]) == True
    assert has_cycle_undirected(2, []) == False
    assert has_cycle_undirected(1, []) == False
    assert has_cycle_undirected(6, [[0, 1], [1, 2], [2, 0], [3, 4], [4, 5], [5, 3]]) == True
    assert has_cycle_undirected(3, [[0, 1], [1, 2]]) == False
    assert has_cycle_undirected(7, [[0, 1], [1, 2], [2, 0], [3, 4], [5, 6]]) == True

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
