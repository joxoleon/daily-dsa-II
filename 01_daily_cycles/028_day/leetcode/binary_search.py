# [ Name: Binary Search ]  [ Category: binary_search ]  [ Topic: binary_search ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/binary-search/ ]

"""
Given a sorted array of n integers and a target value, return the index if the target is found; otherwise, return -1.
The input array has no duplicate elements and is sorted in ascending order.
You must write an algorithm with O(log n) runtime complexity.
Example: Input: nums = [-1,0,3,5,9,12], target = 9  Output: 4
Constraints: 1 <= nums.length <= 10^4, -10^4 < nums[i], target < 10^4
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    pass

if __name__ == "__main__":
    assert search([-1,0,3,5,9,12], 9) == 4
    assert search([-1,0,3,5,9,12], 2) == -1
    assert search([5], 5) == 0
    assert search([5], -5) == -1
    assert search([1,2,3,4,5,6,7], 1) == 0
    assert search([1,2,3,4,5,6,7], 7) == 6
    assert search([1,3,5,7,9], 3) == 1
    assert search([1,3,5,7,9], 8) == -1