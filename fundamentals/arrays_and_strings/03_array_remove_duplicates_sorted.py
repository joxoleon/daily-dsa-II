# [ Name: Remove Duplicates from Sorted Array — Count Unique ]  [ Category: arrays ]  [ Topic: in_place ]  [ Weight: 7 ]

"""
Problem Description:
Given a sorted list of integers, return the number of unique elements.
The operation must be performed in O(1) extra space.
The input list may be empty or contain duplicates.
Return an integer representing the count of unique elements.

Constraints:
- Input: sorted list of integers (0 <= len(nums) <= 10^5)

Example:
Input: [1,1,2,2,3] -> Output: 3
"""

from typing import List

def count_unique(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert count_unique([1,1,2,2,3]) == 3
    assert count_unique([1,1,1,1]) == 1
    assert count_unique([]) == 0
    assert count_unique([5]) == 1
    assert count_unique([1,2,3,4]) == 4
    assert count_unique([2,2,2,3,3,4,5,5,5,6]) == 5
    assert count_unique([0,0,0,0,0,0]) == 1
    assert count_unique([-2, -1, -1, 0, 0, 2]) == 4

    print("All tests passed.")
