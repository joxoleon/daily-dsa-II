# [ Name: Largest Number ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 7 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/largest-number/ ]

"""
Given a list of non-negative integers nums, arrange them so they form the largest number and return it as a string.
The result should not contain leading zeros except for the number '0' itself.
1 <= nums.length <= 100
0 <= nums[i] <= 10^9
Example: Input: nums = [10,2]; Output: "210"
"""

from typing import List

def largestNumber(nums: List[int]) -> str:
    pass

if __name__ == "__main__":
    assert largestNumber([10,2]) == "210"
    assert largestNumber([3,30,34,5,9]) == "9534330"
    assert largestNumber([1]) == "1"
    assert largestNumber([10]) == "10"
    assert largestNumber([0,0]) == "0"
    assert largestNumber([20,1]) == "201"
    assert largestNumber([121,12]) == "12121"
    assert largestNumber([8308,8308,830]) == "83088308830"