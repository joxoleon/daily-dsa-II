# [ Name: Backtracking — Combination Sum II ]  [ Category: backtracking ]  [ Topic: combination_sum ]  [ Weight: 9 ]

"""
Problem Description:
Given a list of positive integers (candidates) and a target number, find all unique combinations of candidates where the numbers sum to the target.
Each number in candidates may only be used once in each combination.
Return a list of all unique combinations; do not include duplicate combinations.
Numbers and target are positive integers; candidates may have duplicates, but combinations must be unique.

Constraints:
- 1 <= len(candidates) <= 100
- 1 <= candidates[i], target <= 50

Example:
Input: candidates = [10,1,2,7,6,1,5], target = 8 ➞ Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
"""

from typing import List

def combination_sum_ii(candidates: List[int], target: int) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted([sorted(c) for c in combination_sum_ii([10,1,2,7,6,1,5], 8)]) == sorted([sorted(x) for x in [[1,1,6],[1,2,5],[1,7],[2,6]]])
    assert sorted([sorted(c) for c in combination_sum_ii([2,5,2,1,2], 5)]) == sorted([sorted(x) for x in [[1,2,2],[5]]])
    assert combination_sum_ii([3,1,3,5,1,1], 8) == [[1,1,1,5],[1,1,3,3],[3,5]]
    assert combination_sum_ii([2], 1) == []
    assert combination_sum_ii([1,1,1,1], 2) == [[1,1]]
    assert combination_sum_ii([4,4,2,1], 9) == []
    assert sorted([sorted(c) for c in combination_sum_ii([1,2,3], 6)]) == [[1,2,3]]
    assert combination_sum_ii([5,3,2,7,3,2,1], 7) == [[1,2,2,2],[1,3,3],[1,2,4],[2,5],[3,4],[7]] or combination_sum_ii([5,3,2,7,3,2,1], 7) == [[1,2,2,2],[1,3,3],[2,5],[3,4],[7]]
    print("All tests passed.")
