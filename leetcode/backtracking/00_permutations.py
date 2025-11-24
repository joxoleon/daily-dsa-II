# [ Name: Permutations ]  [ Category: backtracking ]  [ Topic: backtracking ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/permutations/ ]

"""
Given an array nums of distinct integers, return all possible permutations.
You may return the answer in any order.
Constraints: 1 <= nums.length <= 6, -10 <= nums[i] <= 10, all values unique.
Example: Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

from typing import List

def permute(nums: List[int]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted(permute([1,2,3])) == sorted([[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]])
    assert sorted(permute([0,1])) == sorted([[0,1],[1,0]])
    assert sorted(permute([1])) == sorted([[1]])
    assert sorted(permute([1,2])) == sorted([[1,2],[2,1]])
    assert sorted(permute([9,8,7])) == sorted([[9,8,7],[9,7,8],[8,9,7],[8,7,9],[7,9,8],[7,8,9]])
    assert sorted(permute([-1,0,1])) == sorted([[-1,0,1],[-1,1,0],[0,-1,1],[0,1,-1],[1,-1,0],[1,0,-1]])
    assert sorted(permute([2,4,6,8])) == sorted([
        [2,4,6,8],[2,4,8,6],[2,6,4,8],[2,6,8,4],[2,8,4,6],[2,8,6,4],
        [4,2,6,8],[4,2,8,6],[4,6,2,8],[4,6,8,2],[4,8,2,6],[4,8,6,2],
        [6,2,4,8],[6,2,8,4],[6,4,2,8],[6,4,8,2],[6,8,2,4],[6,8,4,2],
        [8,2,4,6],[8,2,6,4],[8,4,2,6],[8,4,6,2],[8,6,2,4],[8,6,4,2]
    ])
    assert sorted(permute([1,5,9])) == sorted([[1,5,9],[1,9,5],[5,1,9],[5,9,1],[9,1,5],[9,5,1]])