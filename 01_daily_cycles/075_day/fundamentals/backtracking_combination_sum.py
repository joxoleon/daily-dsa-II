# [ Name: Backtracking — Combination Sum ]  [ Category: backtracking ]  [ Topic: combination_sum ]  [ Weight: 8 ]

"""
Problem Description:
Given a list of distinct positive integers called candidates and a target integer,
return all unique combinations of candidates where the chosen numbers sum to target.
Each number in candidates may be used an unlimited number of times in the combination.
Return the combinations as a list of lists. If no combination is possible, return an empty list.

Constraints:
- 1 <= candidates.length <= 30
- 1 <= candidates[i] <= 200, all unique
- 1 <= target <= 500

Example:
Input: candidates = [2,3,6,7], target = 7 -> Output: [[2,2,3],[7]]
"""

from typing import List


def combination_sum(candidates: List[int], target: int) -> List[List[int]]:
    pass


if __name__ == "__main__":
    assert sorted([sorted(x) for x in combination_sum([2,3,6,7], 7)]) == sorted([sorted(x) for x in [[2,2,3],[7]]])
    assert sorted([sorted(x) for x in combination_sum([2,3,5], 8)]) == sorted([sorted(x) for x in [[2,2,2,2],[2,3,3],[3,5]]])
    assert combination_sum([2], 1) == []
    assert sorted([sorted(x) for x in combination_sum([1], 2)]) == sorted([sorted(x) for x in [[1,1]]])
    assert combination_sum([5,10], 1) == []
    assert sorted([sorted(x) for x in combination_sum([7,3,2], 18)]) == sorted([sorted(x) for x in [
        [2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,2,3,3,2],
        [2,2,2,2,3,3,3,3],
        [3,3,3,3,3,3],
        [2,2,2,2,2,2,2,2,2],
        [2,2,2,2,2,3,3,3],
        [2,2,2,3,3,3,3],
        [2,2,2,2,7,3],
        [7,7,2,2],
        [7,3,3,3,2],
        [7,7,3,1]
    ] if sum(x)==18])  # filter to valid outputs
    assert sorted([sorted(x) for x in combination_sum([2,4,8], 8)]) == sorted([sorted(x) for x in [[2,2,2,2],[4,4],[8]]])
    assert combination_sum([9], 3) == []
    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
