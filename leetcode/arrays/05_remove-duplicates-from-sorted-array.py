# [ Name: Remove Duplicates from Sorted Array ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/ ]

"""
Given a sorted array nums, remove the duplicates in-place such that each unique element appears only once. 
Return the new length of the array after duplicates have been removed.
Input: nums as List[int]; Output: int length, with nums modified in-place.
Constraints: 1 <= len(nums) <= 3 * 10^4, nums sorted in non-decreasing order.
Example: Input: nums = [1,1,2], Output: 2, nums = [1,2,_]
"""

from typing import List

def removeDuplicates(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    nums1 = [1,1,2]
    assert removeDuplicates(nums1) == 2 and nums1[:2] == [1,2]
    nums2 = [0,0,1,1,1,2,2,3,3,4]
    assert removeDuplicates(nums2) == 5 and nums2[:5] == [0,1,2,3,4]
    nums3 = [1]
    assert removeDuplicates(nums3) == 1 and nums3[:1] == [1]
    nums4 = [1,1,1,1]
    assert removeDuplicates(nums4) == 1 and nums4[:1] == [1]
    nums5 = [1,2,3,4,5]
    assert removeDuplicates(nums5) == 5 and nums5[:5] == [1,2,3,4,5]
    nums6 = [2,2,2,3,4,4,5,5,5,6]
    assert removeDuplicates(nums6) == 5 and nums6[:5] == [2,3,4,5,6]
    nums7 = [-1,-1,0,0,1,2,2]
    assert removeDuplicates(nums7) == 4 and nums7[:4] == [-1,0,1,2]
    nums8 = [1,2]
    assert removeDuplicates(nums8) == 2 and nums8[:2] == [1,2]