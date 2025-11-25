# [ Name: Union-Find — Cycle Detection in Undirected Graph ]  [ Category: union_find ]  [ Topic: cycle_detection ]  [ Weight: 7 ]

"""
Problem Description:
Given an undirected graph with n nodes labeled from 0 to n - 1 and a list of edges, detect if the graph contains any cycles.
Return True if any cycles exist, otherwise return False.

Constraints:
- 1 <= n <= 10^4
- 0 <= len(edges) <= 2 * 10^4
- Each edge is represented as a list of two integers.
- Edges may contain duplicate or self-loop edges.

Example:
Input: n = 3, edges = [[0,1],[1,2],[2,0]] -> Output: True
"""

from typing import List

def has_cycle(n: int, edges: List[List[int]]) -> bool:
    pass

if __name__ == "__main__":
    assert has_cycle(3, [[0,1],[1,2],[2,0]]) == True
    assert has_cycle(4, [[0,1],[1,2],[2,3]]) == False
    assert has_cycle(1, []) == False
    assert has_cycle(2, [[0,1],[1,0]]) == True
    assert has_cycle(4, [[0,1],[1,2],[2,0],[2,3]]) == True
    assert has_cycle(5, [[0,1],[1,2],[3,4]]) == False
    assert has_cycle(3, [[0,0]]) == True
    assert has_cycle(6, [[0,1],[1,2],[2,3],[3,4],[4,5]]) == False

    print("All tests passed.")
