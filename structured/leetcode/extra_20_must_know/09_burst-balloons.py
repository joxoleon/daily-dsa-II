# [ Name: Burst Balloons ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 9 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/burst-balloons/ ]

"""
Given an array of integers nums representing balloons, each containing a number, you can burst them in any order. 
When you burst balloon i, you get nums[i - 1] * nums[i] * nums[i + 1] coins; if i is out of bounds, treat as 1.
Return the maximum coins you can collect by bursting all balloons optimally.
1 <= nums.length <= 500
0 <= nums[i] <= 100
Example: nums = [3,1,5,8] -> Output: 167
"""

from typing import List

def maxCoins(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert maxCoins([3,1,5,8]) == 167
    assert maxCoins([1,5]) == 10
    assert maxCoins([7]) == 7
    assert maxCoins([9,7,1,0,9,8,8,7,1,6]) == 1916
    assert maxCoins([1,2,3,4,5]) == 110
    assert maxCoins([1,1,1,1]) == 4
    assert maxCoins([8,2,6,8,7,4,9,6,9,2]) == 2593
    assert maxCoins([0]) == 0
