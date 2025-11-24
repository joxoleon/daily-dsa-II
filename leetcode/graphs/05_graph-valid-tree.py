# [ Name: Graph Valid Tree ]  [ Category: graphs ]  [ Topic: graphs ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/graph-valid-tree/ ]

"""
Given n nodes labeled from 0 to n - 1, and a list of undirected edges, determine if they form a valid tree.
Return True if the edges form a valid tree with n nodes; otherwise, return False.
Inputs: an integer n (number of nodes), and a list of edges (each edge is a pair of nodes).
A valid tree is connected and has no cycles.
Example: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]] → Output: True
Constraints: 1 <= n <= 2000, 0 <= edges.length <= n*(n-1)/2
"""

from typing import List

def validTree(n: int, edges: List[List[int]]) -> bool:
    pass

if __name__ == "__main__":
    assert validTree(5, [[0,1],[0,2],[0,3],[1,4]]) == True
    assert validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]) == False
    assert validTree(1, []) == True
    assert validTree(2, [[0,1]]) == True
    assert validTree(2, []) == False
    assert validTree(4, [[0,1],[2,3]]) == False
    assert validTree(3, [[0,1],[1,2],[2,0]]) == False
    assert validTree(4, [[0,1],[1,2],[2,3]]) == True