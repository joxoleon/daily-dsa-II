# [ Name: Subsets II ]  [ Category: backtracking ]  [ Topic: backtracking ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/subsets-ii/ ]

"""
Given an integer array nums that may contain duplicates, return all possible subsets (the power set) without duplicate subsets.
The solution should return a list of lists with each inner list representing a subset.
Constraints: 1 <= nums.length <= 10, -10 <= nums[i] <= 10.
Example: Input: nums = [1,2,2]; Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""

from typing import List

def subsetsWithDup(nums: List[int]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted([sorted(x) for x in subsetsWithDup([1,2,2])]) == sorted([[],[1],[1,2],[1,2,2],[2],[2,2]])
    assert sorted([sorted(x) for x in subsetsWithDup([0])]) == sorted([[],[0]])
    assert sorted([sorted(x) for x in subsetsWithDup([4,4,4,1,4])]) == sorted([[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]])
    assert sorted([sorted(x) for x in subsetsWithDup([1])]) == sorted([[],[1]])
    assert sorted([sorted(x) for x in subsetsWithDup([1,1])]) == sorted([[],[1],[1,1]])
    assert sorted([sorted(x) for x in subsetsWithDup([2,2,2])]) == sorted([[],[2],[2,2],[2,2,2]])
    assert sorted([sorted(x) for x in subsetsWithDup([1,2,3])]) == sorted([[],[1],[1,2],[1,2,3],[1,3],[2],[2,3],[3]])
    assert sorted([sorted(x) for x in subsetsWithDup([1,2,2,2])]) == sorted([[],[1],[1,2],[1,2,2],[1,2,2,2],[2],[2,2],[2,2,2]])