# [ Name: Binary Search — Find Peak Element ]  [ Category: binary_search ]  [ Topic: binary_search_mountain ]  [ Weight: 7 ]

"""
Problem Description:
Given a list of integers, find an index of a peak element.
A peak element is one that is strictly greater than its neighbors.
Return the index of any one peak. Array may have multiple peaks.
For boundary elements, only one neighbor is considered.
Constraints:
- 1 <= len(nums) <= 10^5
- nums[i] may be any integer

Example:
Input: [1, 3, 2, 1] -> Output: 1
"""

from typing import List


def find_peak(nums: List[int]) -> int:
    pass


if __name__ == "__main__":
    assert find_peak([1, 3, 2, 1]) == 1
    assert find_peak([1]) == 0
    assert find_peak([1, 2, 3, 4, 5]) == 4
    assert find_peak([5, 4, 3, 2, 1]) == 0
    assert find_peak([2, 1, 2]) in [0, 2]
    assert find_peak([1, 2, 1, 3, 5, 6, 4]) in [1, 5]
    assert find_peak([1, 1, 1, 2, 1]) == 3
    assert find_peak([10, 9, 8, 8, 8]) == 0

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
