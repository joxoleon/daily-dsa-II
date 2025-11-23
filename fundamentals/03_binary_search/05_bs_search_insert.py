# [ Name: Binary Search — Search Insert Position ]  [ Category: arrays ]  [ Topic: binary_search_insert ]  [ Weight: 6 ]

"""
Problem Description:
Given a sorted array of distinct integers and a target value, return the index if the target is found.
If not, return the index where it would be if it were inserted in order.
Assume no duplicates in the array.
The array may be empty (return 0 in that case).

Constraints:
- 0 <= len(nums) <= 10^4
- -10^4 <= nums[i], target <= 10^4

Example:
Input: nums = [1,3,5,6], target = 5 -> Output: 2
"""

from typing import List

def search_insert(nums: List[int], target: int) -> int:
    pass

if __name__ == "__main__":
    assert search_insert([1,3,5,6], 5) == 2
    assert search_insert([1,3,5,6], 2) == 1
    assert search_insert([1,3,5,6], 7) == 4
    assert search_insert([1,3,5,6], 0) == 0
    assert search_insert([], 3) == 0
    assert search_insert([2], 2) == 0
    assert search_insert([2,4,6,8], 5) == 2
    assert search_insert([1,2,4,6,9], 10) == 5

    print("All tests passed.")
