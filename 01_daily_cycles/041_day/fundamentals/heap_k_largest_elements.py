# [ Name: Heap — K Largest Elements ]  [ Category: heaps ]  [ Topic: max_heap ]  [ Weight: 8 ]

"""
Problem Description:
Given a list of integers nums and an integer k, return the k largest elements from nums in descending order.
If k is 0, return an empty list. If k >= len(nums), return all elements sorted in descending order.

Constraints:
- 0 <= k <= len(nums) <= 10^5
- -10^9 <= nums[i] <= 10^9

Example:
Input: nums = [3, 1, 5, 12, 2, 11], k = 3 -> Output: [12, 11, 5]
"""

from typing import List

def k_largest(nums: List[int], k: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert k_largest([3, 1, 5, 12, 2, 11], 3) == [12, 11, 5]
    assert k_largest([1, 2, 3, 4], 2) == [4, 3]
    assert k_largest([7, 7, 7, 7], 2) == [7, 7]
    assert k_largest([], 0) == []
    assert k_largest([5, -2, 3, 8], 0) == []
    assert k_largest([10, 9, 8], 5) == [10, 9, 8]
    assert k_largest([-1, -7, -3, -4], 2) == [-1, -3]
    assert k_largest([100], 1) == [100]
    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
