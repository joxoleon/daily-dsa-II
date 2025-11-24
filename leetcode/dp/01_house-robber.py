# [ Name: House Robber ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/house-robber/ ]

"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, and adjacent houses cannot be robbed on the same night.
Given an integer list nums representing the amount of money at each house, return the maximum amount you can rob tonight without alerting the police.
1 <= nums.length <= 100, 0 <= nums[i] <= 400.
Example: Input: nums = [2,7,9,3,1] Output: 12
"""

from typing import List

def rob(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert rob([2,7,9,3,1]) == 12
    assert rob([1,2,3,1]) == 4
    assert rob([0]) == 0
    assert rob([9,1,1,9]) == 18
    assert rob([5,3,4,11,2]) == 16
    assert rob([100,1,1,100]) == 200
    assert rob([1,3,1]) == 3
    assert rob([1,2]) == 2