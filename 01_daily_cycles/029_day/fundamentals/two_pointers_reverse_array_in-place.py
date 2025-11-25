# [ Name: Two Pointers — Reverse Array In-Place ]  [ Category: arrays ]  [ Topic: two_pointers ]  [ Weight: 6 ]

"""
Problem Description:
Given a list of integers, reverse the elements of the list in-place and return the resulting list.
You must not use extra space for another array; modify the input list directly.
Return the modified list after reversal.

Constraints:
- Input: list of integers, 0 <= len(nums) <= 10^5
- The function should work for empty lists and single-element lists.

Example:
Input: [1, 2, 3, 4] -> Output: [4, 3, 2, 1]
"""

from typing import List

def reverse_array(nums: List[int]) -> List[int]:
    pass

if __name__ == "__main__":
    assert reverse_array([1, 2, 3, 4]) == [4, 3, 2, 1]
    assert reverse_array([]) == []
    assert reverse_array([9]) == [9]
    assert reverse_array([5, 7]) == [7, 5]
    assert reverse_array([1, 2, 3, 2, 1]) == [1, 2, 3, 2, 1]
    assert reverse_array([-1, 0, 1]) == [1, 0, -1]
    assert reverse_array([42, 13, 7, 8, 99]) == [99, 8, 7, 13, 42]
    assert reverse_array([0, 0, 0, 0]) == [0, 0, 0, 0]

    print("All tests passed.")
