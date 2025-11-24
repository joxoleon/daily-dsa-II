# [ Name: Find Kth Largest Element in an Array ]  [ Category: binary_search ]  [ Topic: binary_search ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/kth-largest-element-in-an-array/ ]

"""
Given an integer array nums and an integer k, return the k-th largest element in the array.
The input array may not be sorted. The answer must be an actual element in the array.
1 <= k <= len(nums)
1 <= len(nums) <= 10^5
-10^4 <= nums[i] <= 10^4
Example: nums = [3,2,1,5,6,4], k = 2 => Output: 5
"""

from typing import List

def findKthLargest(nums: List[int], k: int) -> int:
    pass

if __name__ == "__main__":
    assert findKthLargest([3,2,1,5,6,4], 2) == 5
    assert findKthLargest([3,2,3,1,2,4,5,5,6], 4) == 4
    assert findKthLargest([1], 1) == 1
    assert findKthLargest([2,1], 1) == 2
    assert findKthLargest([2,1], 2) == 1
    assert findKthLargest([7,6,5,4,3,2,1], 5) == 3
    assert findKthLargest([5,5,5,5,5], 3) == 5
    assert findKthLargest([99,100,-1,-2,45], 3) == 45