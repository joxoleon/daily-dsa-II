# [ Name: Median of Two Sorted Arrays ]  [ Category: binary_search ]  [ Topic: binary_search ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/median-of-two-sorted-arrays/ ]

"""
Given two sorted arrays nums1 and nums2 of size m and n, return the median of the two sorted arrays.
The total run time complexity should be O(log (m+n)).
Inputs: two sorted integer arrays.
Output: a float representing the median value.
1 <= m, n <= 1000, 0 <= elements <= 10^6
Example: nums1 = [1,3], nums2 = [2] -> Output: 2.0
"""

from typing import List

def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    pass

if __name__ == "__main__":
    assert findMedianSortedArrays([1, 3], [2]) == 2.0
    assert findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert findMedianSortedArrays([], [1]) == 1.0
    assert findMedianSortedArrays([2], []) == 2.0
    assert findMedianSortedArrays([1, 3, 5], [2, 4, 6]) == 3.5
    assert findMedianSortedArrays([1], [2, 3, 4, 5, 6]) == 3.5
    assert findMedianSortedArrays([5, 7, 9], [1, 2, 3, 4, 6, 8, 10]) == 5.5