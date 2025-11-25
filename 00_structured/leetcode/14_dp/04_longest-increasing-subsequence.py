# [ Name: Longest Increasing Subsequence ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/longest-increasing-subsequence/ ]

"""
Given an integer array nums, return the length of the longest strictly increasing subsequence.
A subsequence is a sequence derived from the array by deleting any number of elements without changing the order.
1 <= nums.length <= 2500
-10^4 <= nums[i] <= 10^4
Example: For nums = [10,9,2,5,3,7,101,18], the output is 4.
"""

from typing import List

def lengthOfLIS(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert lengthOfLIS([10,9,2,5,3,7,101,18]) == 4
    assert lengthOfLIS([0,1,0,3,2,3]) == 4
    assert lengthOfLIS([7,7,7,7,7,7,7]) == 1
    assert lengthOfLIS([1]) == 1
    assert lengthOfLIS([4,10,4,3,8,9]) == 3
    assert lengthOfLIS([2,2]) == 1
    assert lengthOfLIS([1,3,6,7,9,4,10,5,6]) == 6
    assert lengthOfLIS([3,5,6,2,5,4,19,5,6,7,12]) == 6