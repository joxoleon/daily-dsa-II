# [ Name: Two Sum ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 10 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/two-sum/ ]

"""
Given an integer array nums and an integer target, return the indices of the two numbers such that they add up to target.
You may assume each input has exactly one solution, and you may not use the same element twice.
Return the answer as a list of two indices.
Constraints: 2 <= nums.length <= 10^4, -10^9 <= nums[i] <= 10^9, only one valid answer.
Example: Input: nums = [2,7,11,15], target = 9; Output: [0,1]
"""

from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert set(twoSum([2,7,11,15], 9)) == set([0,1])
    assert set(twoSum([3,2,4], 6)) == set([1,2])
    assert set(twoSum([3,3], 6)) == set([0,1])
    assert set(twoSum([1,2,3,4], 5)) == set([1,3])
    assert set(twoSum([0,4,3,0], 0)) == set([0,3])
    assert set(twoSum([-1,-2,-3,-4,-5], -8)) == set([2,4])
    assert set(twoSum([5,75,25], 100)) == set([1,2])
    assert set(twoSum([1,5,1,5], 10)) == set([1,3])
