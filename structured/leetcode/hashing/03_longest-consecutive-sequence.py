# [ Name: Longest Consecutive Sequence ]  [ Category: hashing ]  [ Topic: hashing ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/longest-consecutive-sequence/ ]

"""
Given an unsorted array of integers nums, return the length of the longest sequence of consecutive numbers.
You must write an algorithm that runs in O(n) time.
Input: nums as List[int]. Output: int representing the sequence length.
Constraints: 0 <= len(nums) <= 1e5; -1e9 <= nums[i] <= 1e9.
Example: nums = [100,4,200,1,3,2] -> Output: 4 (the sequence is [1,2,3,4])
"""

from typing import List

def longestConsecutive(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert longestConsecutive([100,4,200,1,3,2]) == 4
    assert longestConsecutive([]) == 0
    assert longestConsecutive([1]) == 1
    assert longestConsecutive([1,2,0,1]) == 3
    assert longestConsecutive([9,1,-3,2,4,8,3,-1,6,-2,-4,7]) == 4
    assert longestConsecutive([0,0,-1]) == 2
    assert longestConsecutive([10,5,12,3,55,30,4,11,2]) == 4
    assert longestConsecutive([-2,-3,-3,7,-3,0,5,0,-6,6,-4,-8,-1,2,4,2,1]) == 6