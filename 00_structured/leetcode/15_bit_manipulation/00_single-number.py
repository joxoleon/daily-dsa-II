# [ Name: Single Number ]  [ Category: bit_manipulation ]  [ Topic: bit_manipulation ]  [ Weight: 8 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/single-number/ ]

"""
Given a non-empty list of integers, every element appears twice except for one. Find that single one.
Input: List[int] nums with 1 <= len(nums) <= 3 * 10^4; each element is an integer in range [-3*10^4, 3*10^4].
Output: The single integer that does not appear twice.
Example: Input: nums = [2,2,1] Output: 1
Each input will have exactly one solution. 
"""

from typing import List

def singleNumber(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert singleNumber([2,2,1]) == 1
    assert singleNumber([4,1,2,1,2]) == 4
    assert singleNumber([1]) == 1
    assert singleNumber([0,0,7]) == 7
    assert singleNumber([-1,2,2]) == -1
    assert singleNumber([5,5,10]) == 10
    assert singleNumber([100,1,1]) == 100
    assert singleNumber([-10,-10,0]) == 0