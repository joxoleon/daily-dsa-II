# [ Name: Backtracking — Combinations ]  [ Category: backtracking ]  [ Topic: combinations ]  [ Weight: 6 ]

"""
Problem Description:
Given two integers n and k, return all possible combinations of k numbers chosen from the range 1 to n (inclusive).
Each combination must be a list of k distinct integers in ascending order.
Return the list of all combinations in any order.

Constraints:
- 1 <= k <= n <= 20
- Return an empty list if k == 0 or n == 0.

Example:
Input: n = 4, k = 2 -> Output: [[1,2], [1,3], [1,4], [2,3], [2,4], [3,4]]
"""

from typing import List

def combinations(n: int, k: int) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert combinations(4, 2) == [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert combinations(1, 1) == [[1]]
    assert combinations(3, 1) == [[1],[2],[3]]
    assert combinations(3, 3) == [[1,2,3]]
    assert combinations(0, 0) == []
    assert combinations(2, 0) == []
    assert combinations(5, 3) == [[1,2,3],[1,2,4],[1,2,5],[1,3,4],[1,3,5],[1,4,5],[2,3,4],[2,3,5],[2,4,5],[3,4,5]]
    assert combinations(2, 2) == [[1,2]]
    print("All tests passed.")
