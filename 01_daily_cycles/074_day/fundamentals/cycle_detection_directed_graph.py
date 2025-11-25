# [ Name: Cycle Detection — Directed Graph ]  [ Category: graphs ]  [ Topic: cycle_detection ]  [ Weight: 8 ]

"""
Problem Description:
Given a directed graph with num_nodes nodes labeled from 0 to num_nodes-1 and a list of directed edges,
determine if the graph contains any cycle. Return True if there is at least one cycle, else return False.

Constraints:
- 1 <= num_nodes <= 10^4
- 0 <= len(edges) <= 2 * 10^4
- edges[i] = [from, to], 0 <= from, to < num_nodes

Example:
Input: num_nodes = 3, edges = [[0,1],[1,2],[2,0]] -> Output: True
"""

from typing import List

def has_cycle_directed(num_nodes: int, edges: List[List[int]]) -> bool:
    pass

if __name__ == "__main__":
    assert has_cycle_directed(3, [[0,1],[1,2],[2,0]]) == True
    assert has_cycle_directed(3, [[0,1],[1,2]]) == False
    assert has_cycle_directed(4, [[0,1],[1,2],[2,3],[3,1]]) == True
    assert has_cycle_directed(1, []) == False
    assert has_cycle_directed(2, [[0,1]]) == False
    assert has_cycle_directed(2, [[0,1],[1,0]]) == True
    assert has_cycle_directed(5, [[0,1],[1,2],[2,3],[3,4]]) == False
    assert has_cycle_directed(4, [[0,1],[1,2],[2,3],[3,0]]) == True

    print("All tests passed.")
