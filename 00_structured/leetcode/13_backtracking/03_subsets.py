# [ Name: Subsets ]  [ Category: backtracking ]  [ Topic: backtracking ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/subsets/ ]

"""
Given an integer array nums of unique elements, return all possible subsets (the power set).
The solution set must not contain duplicate subsets.
Input: nums is a list of up to 10 integers, all unique.
Output: List of lists, each inner list is a possible subset.
Example: Input: nums = [1,2,3]  Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
"""

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted([sorted(l) for l in subsets([1,2,3])]) == sorted([sorted(l) for l in [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]])
    assert sorted([sorted(l) for l in subsets([])]) == sorted([sorted(l) for l in [[]]])
    assert sorted([sorted(l) for l in subsets([1])]) == sorted([sorted(l) for l in [[],[1]]])
    assert sorted([sorted(l) for l in subsets([0])]) == sorted([sorted(l) for l in [[],[0]]])
    assert sorted([sorted(l) for l in subsets([1,2])]) == sorted([sorted(l) for l in [[],[1],[2],[1,2]]])
    assert sorted([sorted(l) for l in subsets([4,5,6])]) == sorted([sorted(l) for l in [[],[4],[5],[6],[4,5],[4,6],[5,6],[4,5,6]]])
    assert sorted([sorted(l) for l in subsets([10,20,30,40])]) == sorted([sorted(l) for l in [[],[10],[20],[30],[40],[10,20],[10,30],[10,40],[20,30],[20,40],[30,40],[10,20,30],[10,20,40],[10,30,40],[20,30,40],[10,20,30,40]]])
    assert sorted([sorted(l) for l in subsets([7,8,9,10,11])]) == sorted([sorted(l) for l in [
        [],[7],[8],[9],[10],[11],
        [7,8],[7,9],[7,10],[7,11],[8,9],[8,10],[8,11],[9,10],[9,11],[10,11],
        [7,8,9],[7,8,10],[7,8,11],[7,9,10],[7,9,11],[7,10,11],[8,9,10],[8,9,11],[8,10,11],[9,10,11],
        [7,8,9,10],[7,8,9,11],[7,8,10,11],[7,9,10,11],[8,9,10,11],
        [7,8,9,10,11]
    ]])