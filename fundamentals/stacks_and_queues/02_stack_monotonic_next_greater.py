# [ Name: Monotonic Stack — Next Greater Element ]  [ Category: stacks ]  [ Topic: monotonic_stack ]  [ Weight: 8 ]

"""
Problem Description:
Given a list of integers nums, for every element, find the next greater element to its right.
If no such element exists, use -1 for that position.
Return a list where result[i] is the next greater element for nums[i].
- Input: a list of integers (can be empty, length up to 10^5)
- Elements may be negative or positive.
Example:
Input: [2, 1, 2, 4, 3] -> Output: [4, 2, 4, -1, -1]
"""

from typing import List


def next_greater(nums: List[int]) -> List[int]:
    pass


if __name__ == "__main__":
    assert next_greater([2, 1, 2, 4, 3]) == [4, 2, 4, -1, -1]
    assert next_greater([]) == []
    assert next_greater([5]) == [-1]
    assert next_greater([4, 3, 2, 1]) == [-1, -1, -1, -1]
    assert next_greater([1, 3, 2, 4]) == [3, 4, 4, -1]
    assert next_greater([1, 2, 3, 4]) == [2, 3, 4, -1]
    assert next_greater([2, 2, 2]) == [-1, -1, -1]
    assert next_greater([-1, 0, -2, 1]) == [0, 1, 1, -1]

    print("All tests passed.")
