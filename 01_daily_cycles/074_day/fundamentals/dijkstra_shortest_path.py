# [ Name: Dijkstra — Shortest Path ]  [ Category: graphs ]  [ Topic: dijkstra ]  [ Weight: 9 ]

"""
Problem Description:
Given an undirected, weighted graph with n nodes (labeled 0 to n-1), represented by a list of edges [u, v, w] (edge between u and v with weight w), compute the shortest distance from the start node to all other nodes.
Return a list of integers where the ith element is the minimum distance from start to node i (use -1 if node i is unreachable).
Constraints: 
- 1 <= n <= 1000
- 0 <= edges.length <= 10^4
- All weights are positive integers.

Example:
Input: n = 4, edges = [[0,1,2],[1,2,1],[0,3,4]], start = 0 -> Output: [0,2,3,4]
"""

from typing import List

def dijkstra(n: int, edges: List[List[int]], start: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert dijkstra(4, [[0,1,2],[1,2,1],[0,3,4]], 0) == [0,2,3,4]
    assert dijkstra(5, [[1,2,2],[0,1,10],[2,3,3]], 0) == [0,10,12,15,-1]
    assert dijkstra(3, [], 0) == [0,-1,-1]
    assert dijkstra(2, [[0,1,7]], 1) == [7,0]
    assert dijkstra(1, [], 0) == [0]
    assert dijkstra(4, [[0,1,5],[1,2,10],[2,3,1]], 3) == [16,11,1,0]
    assert dijkstra(6, [[0,1,1],[1,2,2],[2,3,3],[3,4,4],[4,5,5]], 0) == [0,1,3,6,10,15]
    assert dijkstra(3, [[0,1,2],[1,2,2],[0,2,1]], 1) == [2,0,2]

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
