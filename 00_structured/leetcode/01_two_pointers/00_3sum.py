# [ Name: 3Sum ]  [ Category: two_pointers ]  [ Topic: two_pointers ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/3sum/ ]

"""
Given an array nums of n integers, find all unique triplets in the array which give the sum of zero.
Return a list of all the unique triplets [nums[i], nums[j], nums[k]] such that i ≠ j ≠ k and nums[i] + nums[j] + nums[k] == 0.
The answer must not contain duplicate triplets.
Constraints: 3 <= len(nums) <= 3000, -10^5 <= nums[i] <= 10^5.
Example: Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

from typing import List

def threeSum(nums: List[int]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted([sorted(triplet) for triplet in threeSum([-1,0,1,2,-1,-4])]) == sorted([[-1,-1,2],[-1,0,1]])
    assert threeSum([]) == []
    assert threeSum([0]) == []
    assert threeSum([0,0,0]) == [[0,0,0]]
    assert sorted([sorted(triplet) for triplet in threeSum([1,-1,-1,0])]) == [[-1,0,1]]
    assert threeSum([1,2,-2,-1]) == []
    assert sorted([sorted(triplet) for triplet in threeSum([3,0,-2,-1,1,2])]) == sorted([[-2,-1,3],[-2,0,2],[-1,0,1]])
    assert threeSum([-2,0,1,1,2]) == [[-2,0,2],[-2,1,1]]