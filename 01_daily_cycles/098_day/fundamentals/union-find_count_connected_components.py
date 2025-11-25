# [ Name: Union-Find — Count Connected Components ]  [ Category: union_find ]  [ Topic: components ]  [ Weight: 6 ]

"""
Problem Description:
Given n nodes labeled from 0 to n - 1 and a list of undirected edges, return the number of connected components in the undirected graph.
Each edge is represented as a pair of nodes [a, b].
Return an integer representing the number of connected components.
Constraints:
- 1 <= n <= 10000
- 0 <= edges.length <= min(20000, n*(n-1)/2)
- No self-loops or duplicate edges.

Example:
Input: n = 5, edges = [[0,1],[1,2],[3,4]] -> Output: 2
"""

from typing import List

def count_components(n: int, edges: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert count_components(5, [[0,1],[1,2],[3,4]]) == 2
    assert count_components(5, [[0,1],[1,2],[2,3],[3,4]]) == 1
    assert count_components(4, [[0,1],[2,3]]) == 2
    assert count_components(4, []) == 4
    assert count_components(2, [[0,1]]) == 1
    assert count_components(6, [[0,1],[2,3],[4,5]]) == 3
    assert count_components(1, []) == 1
    assert count_components(3, [[0,1]]) == 2

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
