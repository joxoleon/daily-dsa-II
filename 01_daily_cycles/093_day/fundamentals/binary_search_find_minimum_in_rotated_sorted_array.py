# [ Name: Binary Search — Find Minimum in Rotated Sorted Array ]  [ Category: binary_search ]  [ Topic: binary_search_rotated ]  [ Weight: 8 ]

"""
Problem Description:
Given a rotated sorted array of distinct integers, find and return its minimum element.
Input: A non-empty list of integers, where the original array was sorted in ascending order and then rotated.
Output: The smallest integer from the array.

Constraints:
- 1 <= len(nums) <= 10^4
- All elements are unique.

Example:
Input: [4,5,6,7,0,1,2] -> Output: 0
"""

from typing import List

def find_min_rotated(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert find_min_rotated([4,5,6,7,0,1,2]) == 0
    assert find_min_rotated([1,2,3,4,5]) == 1
    assert find_min_rotated([2,3,4,5,1]) == 1
    assert find_min_rotated([5,1,2,3,4]) == 1
    assert find_min_rotated([7,8,9,1,2,3,4,5,6]) == 1
    assert find_min_rotated([1]) == 1
    assert find_min_rotated([3,4,5,6,1,2]) == 1
    assert find_min_rotated([2,1]) == 1

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
