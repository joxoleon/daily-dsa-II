# [ Name: House Robber II ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/house-robber-ii/ ]

"""
You are given a list of non-negative integers representing the amount of money in each house arranged in a circle.
Return the maximum amount of money you can rob without robbing two adjacent houses.
Input: a list of integers nums (length 1 to 100, each 0 <= nums[i] <= 1000)
Output: an integer representing the maximum amount that can be robbed.
Example: nums = [2,3,2] -> Output: 3
"""

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        pass

if __name__ == "__main__":
    s = Solution()
    assert s.rob([2,3,2]) == 3
    assert s.rob([1,2,3,1]) == 4
    assert s.rob([1,2,3]) == 3
    assert s.rob([0]) == 0
    assert s.rob([5,1,1,5]) == 10
    assert s.rob([4,1,2,7,5,3,1]) == 14
    assert s.rob([200,3,140,20,10]) == 340
    assert s.rob([2,7,9,3,1]) == 11