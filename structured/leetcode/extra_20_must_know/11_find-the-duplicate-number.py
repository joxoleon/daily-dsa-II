# [ Name: Find the Duplicate Number ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/find-the-duplicate-number/ ]

"""
Given an array nums containing n + 1 integers where each integer 
is between 1 and n (inclusive), return the duplicate number. 
Assume that only one duplicate exists but it could be repeated multiple times. 
The input array cannot be modified and uses only constant extra space.
Example: Input: nums = [1,3,4,2,2]; Output: 2
Constraints: 2 <= n + 1 <= 10^5; 1 <= nums[i] <= n
"""

from typing import List

def findDuplicate(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert findDuplicate([1,3,4,2,2]) == 2
    assert findDuplicate([3,1,3,4,2]) == 3
    assert findDuplicate([2,2,2,2,2]) == 2
    assert findDuplicate([1,1]) == 1
    assert findDuplicate([1,4,6,3,2,5,6]) == 6
    assert findDuplicate([2,5,9,6,9,3,8,9,7,1]) == 9
    assert findDuplicate([7,9,7,4,2,8,7,6,1,3,5]) == 7
    assert findDuplicate([2,1,4,3,4,5]) == 4