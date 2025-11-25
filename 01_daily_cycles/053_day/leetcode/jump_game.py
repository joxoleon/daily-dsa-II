# [ Name: Jump Game ]  [ Category: greedy ]  [ Topic: greedy ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/jump-game/ ]

"""
Given an array nums where each element represents your maximum jump length from that position, determine if you can reach the last index starting at the first index. Return True if you can reach the last index, or False otherwise.
Input: nums is a list of integers (1 <= len(nums) <= 10^4, 0 <= nums[i] <= 10^5).
Output: Boolean indicating if it's possible to reach the end.
Example: Input: [2,3,1,1,4] Output: True
"""

from typing import List

def canJump(nums: List[int]) -> bool:
    pass

if __name__ == "__main__":
    assert canJump([2,3,1,1,4]) == True
    assert canJump([3,2,1,0,4]) == False
    assert canJump([0]) == True
    assert canJump([2,0,0]) == True
    assert canJump([1,1,1,0]) == True
    assert canJump([1,0,1,0]) == False
    assert canJump([2,5,0,0]) == True
    assert canJump([1,2,0,1,0,0,1]) == False