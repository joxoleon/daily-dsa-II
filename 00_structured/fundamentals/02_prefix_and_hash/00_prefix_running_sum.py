# [ Name: Prefix Sum — Running Sum Array ]  [ Category: arrays ]  [ Topic: prefix_sum_basic ]  [ Weight: 3 ]

"""
Problem Description:
Given a list of integers, return a new list where each element at index i is the sum of all elements from index 0 to i (inclusive).
The input list may be empty.
Return an empty list if given an empty list.

Constraints:
- 0 <= len(nums) <= 10^4
- Each element: -10^6 <= nums[i] <= 10^6

Example:
Input: [1, 2, 3, 4] -> Output: [1, 3, 6, 10]
"""

from typing import List

def running_sum(nums: List[int]) -> List[int]:
    pass

if __name__ == "__main__":
    assert running_sum([1, 2, 3, 4]) == [1, 3, 6, 10]
    assert running_sum([0, 0, 0, 0]) == [0, 0, 0, 0]
    assert running_sum([]) == []
    assert running_sum([5]) == [5]
    assert running_sum([-1, 2, -3, 4]) == [-1, 1, -2, 2]
    assert running_sum([1000000, -1000000]) == [1000000, 0]
    assert running_sum([7, 1, 2]) == [7, 8, 10]
    assert running_sum([10, 20, 30, 40, 50]) == [10, 30, 60, 100, 150]

    print("All tests passed.")
