# [ Name: Combination Sum ]  [ Category: backtracking ]  [ Topic: backtracking ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/combination-sum/ ]

"""
Given an array of distinct integers candidates and a target integer target, find all unique combinations of candidates where the chosen numbers sum to target. Each number in candidates may be selected an unlimited number of times. Return the combinations in any order.
Constraints: 1 <= candidates.length <= 30, 2 <= candidates[i] <= 40, 1 <= target <= 40.
Example: candidates = [2,3,6,7], target = 7 => Output: [[2,2,3],[7]]
"""

from typing import List

def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted(combinationSum([2,3,6,7], 7)) == sorted([[2,2,3],[7]])
    assert sorted(combinationSum([2,3,5], 8)) == sorted([[2,2,2,2],[2,3,3],[3,5]])
    assert combinationSum([2], 1) == []
    assert sorted(combinationSum([1], 2)) == sorted([[1,1]])
    assert combinationSum([5,10], 3) == []
    assert sorted(combinationSum([2,4,6], 8)) == sorted([[2,2,2,2],[2,2,4],[2,6],[4,4]])
    assert sorted(combinationSum([7,3,2], 18)) == sorted([[7,7,2,2],[7,3,3,3,2],[3,3,3,3,3,3],[2,2,2,2,2,2,2,2,2]])
    assert sorted(combinationSum([1,2], 4)) == sorted([[1,1,1,1],[1,1,2],[2,2]])