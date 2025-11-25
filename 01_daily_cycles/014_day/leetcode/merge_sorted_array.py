# [ Name: Merge Sorted Array ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/merge-sorted-array/ ]

"""
Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
The final sorted array should not be returned by the function, but instead be stored inside nums1, which has a size equal to m + n.
nums1 contains m elements, followed by enough space to hold nums2's n elements.
Constraints: 0 <= m, n <= 200; nums1.length == m + n.
Example: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3 → nums1 becomes [1,2,2,3,5,6].
"""

from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    pass

if __name__ == "__main__":
    arr1 = [1,2,3,0,0,0]
    merge(arr1, 3, [2,5,6], 3)
    assert arr1 == [1,2,2,3,5,6]
    arr2 = [1]
    merge(arr2, 1, [], 0)
    assert arr2 == [1]
    arr3 = [0]
    merge(arr3, 0, [1], 1)
    assert arr3 == [1]
    arr4 = [2,0]
    merge(arr4, 1, [1], 1)
    assert arr4 == [1,2]
    arr5 = [4,5,6,0,0,0]
    merge(arr5, 3, [1,2,3], 3)
    assert arr5 == [1,2,3,4,5,6]
    arr6 = [1,2,4,5,6,0]
    merge(arr6, 5, [3], 1)
    assert arr6 == [1,2,3,4,5,6]
    arr7 = [0,0,0]
    merge(arr7, 0, [2,5,6], 3)
    assert arr7 == [2,5,6]
    arr8 = [1,0,0]
    merge(arr8, 1, [2,3], 2)
    assert arr8 == [1,2,3]