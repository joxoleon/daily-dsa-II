# [ Name: Graph DFS — Adjacency List ]  [ Category: graphs ]  [ Topic: dfs ]  [ Weight: 7 ]

"""
Problem Description:
Given an undirected graph represented as an adjacency list and a starting node, perform a depth-first search (DFS) traversal.
Return the list of nodes visited in the order they are first encountered.
The graph may contain cycles and may be disconnected.
If the start node does not exist in the graph, return an empty list.

Constraints:
- graph: Dict[int, List[int]], 0 <= number of nodes <= 10^4
- Node labels are integers.
- Traversal order among neighbors with the same depth can be arbitrary.

Example:
Input: graph = {0: [1,2], 1: [0,3], 2: [0], 3: [1]}, start = 0 -> Output: [0,1,3,2] or [0,2,1,3]
"""

from typing import Dict, List


def dfs(graph: Dict[int, List[int]], start: int) -> List[int]:
    pass


if __name__ == "__main__":
    assert dfs({0: [1,2], 1: [0,3], 2: [0], 3: [1]}, 0) in ([0,1,3,2],[0,2,1,3],[0,1,2,3],[0,2,0,1,3])
    assert dfs({1: [2], 2: [1,3], 3: [2]}, 1) in ([1,2,3],[1,2,3])
    assert dfs({}, 0) == []
    assert dfs({5: [6], 6: [5]}, 5) in ([5,6],[5])
    assert dfs({0: [], 1: [2], 2: [1]}, 1) in ([1,2],[1])
    assert dfs({3: [4], 4: [3,5], 5: [4]}, 3) in ([3,4,5],[3,4])
    assert dfs({1: [2], 2: [1], 3: [4], 4: [3]}, 3) in ([3,4],[3])
    assert dfs({0: [1], 1: [0], 2: []}, 2) == [2]

    print("All tests passed.")
