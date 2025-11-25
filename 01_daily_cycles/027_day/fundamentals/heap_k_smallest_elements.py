# [ Name: Heap — K Smallest Elements ]  [ Category: heaps ]  [ Topic: min_heap ]  [ Weight: 8 ]

"""
Problem Description:
Given an integer list nums and an integer k, return a list containing the k smallest elements from nums, in any order.
If nums contains fewer than k elements, return all of them.
Assume 1 <= k <= len(nums) and all elements fit in memory.
If nums is empty, return an empty list.

Example:
Input: nums = [7, 10, 4, 3, 20, 15], k = 3 -> Output: [3, 4, 7] (order may vary)
"""

from typing import List

def k_smallest(nums: List[int], k: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert sorted(k_smallest([7, 10, 4, 3, 20, 15], 3)) == [3, 4, 7]
    assert sorted(k_smallest([5, 2, 1, 9, 3], 2)) == [1, 2]
    assert sorted(k_smallest([5, 5, 5, 5], 2)) == [5, 5]
    assert sorted(k_smallest([1, 2, 3], 3)) == [1, 2, 3]
    assert k_smallest([], 1) == []
    assert sorted(k_smallest([6, 1, 2, 8, 7], 1)) == [1]
    assert sorted(k_smallest([8], 1)) == [8]
    assert sorted(k_smallest([10, 9, -1, 5, 2], 4)) == [-1, 2, 5, 9]

    print("All tests passed.")
