# [ Name: Search Insert Position ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/search-insert-position/ ]

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be inserted in order. The array contains no duplicates and may have length from 1 up to 10^4. All elements and the target are integers between -10^4 and 10^4.
Example: Input: nums = [1,3,5,6], target = 5; Output: 2
"""

from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    pass

if __name__ == "__main__":
    assert searchInsert([1,3,5,6], 5) == 2
    assert searchInsert([1,3,5,6], 2) == 1
    assert searchInsert([1,3,5,6], 7) == 4
    assert searchInsert([1,3,5,6], 0) == 0
    assert searchInsert([1], 0) == 0
    assert searchInsert([1], 2) == 1
    assert searchInsert([1,3,5,6,9,12], 10) == 5
    assert searchInsert([-10,-5,0,7,20], 0) == 2