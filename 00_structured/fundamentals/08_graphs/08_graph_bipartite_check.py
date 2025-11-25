# [ Name: Graph — Bipartite Check ]  [ Category: graphs ]  [ Topic: bipartite ]  [ Weight: 6 ]

"""
Problem Description:
Given an undirected graph represented as an adjacency list, determine if the graph is bipartite.
A graph is bipartite if its nodes can be divided into two groups where no two nodes within the same group are adjacent.
Input: a list of lists, where graph[i] is a list of nodes connected to node i.
Return True if the graph is bipartite, else return False.

Constraints:
- 0 <= len(graph) <= 1000
- 0 <= number of edges per node <= 1000

Example:
Input: [[1,3],[0,2],[1,3],[0,2]] -> Output: True
"""

from typing import List

def is_bipartite(graph: List[List[int]]) -> bool:
    pass

if __name__ == "__main__":
    assert is_bipartite([[1,3],[0,2],[1,3],[0,2]]) == True
    assert is_bipartite([[1,2,3],[0,2],[0,1,3],[0,2]]) == False
    assert is_bipartite([[]]) == True
    assert is_bipartite([[1],[0]]) == True
    assert is_bipartite([[1,2,3],[0],[0],[0]]) == True
    assert is_bipartite([[1,4],[0,2,3],[1,3],[1,2,4],[0,3]]) == False
    assert is_bipartite([[1],[0,3],[3],[1,2]]) == True
    assert is_bipartite([]) == True

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
