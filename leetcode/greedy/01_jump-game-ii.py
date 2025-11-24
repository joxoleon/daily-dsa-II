# [ Name: Jump Game II ]  [ Category: greedy ]  [ Topic: greedy ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/jump-game-ii/ ]

"""
Given an array nums where each element nums[i] represents the maximum jump length from index i, return the minimum number of jumps to reach the last index.
You start at the first index and each jump must be within the range specified at that position.
Assume you can always reach the last index.
Example: Input: nums = [2,3,1,1,4] Output: 2 (Jump 1 step from index 0 to 1, then 3 steps to the last index)
Constraints: 1 <= nums.length <= 10^4, 0 <= nums[i] <= 1000
"""

from typing import List

def jump(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert jump([2,3,1,1,4]) == 2
    assert jump([2,3,0,1,4]) == 2
    assert jump([1,2,1,1,1]) == 3
    assert jump([1,1,1,1]) == 3
    assert jump([10,9,8,1,0,1,1,1]) == 1
    assert jump([0]) == 0
    assert jump([1,3,5,8,2,6,7,6,6,1,2,5,1,1,4,2,3]) == 4
    assert jump([1]*10000) == 9999
    assert jump([9,8,7,6,5,4,3,2,1,1,0]) == 1