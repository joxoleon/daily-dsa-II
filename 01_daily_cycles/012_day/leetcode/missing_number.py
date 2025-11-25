# [ Name: Missing Number ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 8 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/missing-number/ ]

"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Input: nums - List[int]
Output: int
Constraints: 1 <= nums.length <= 10^4, 0 <= nums[i] <= n, All numbers are unique except one missing.
Example: nums = [3,0,1] -> Output: 2
"""

from typing import List

def missingNumber(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert missingNumber([3,0,1]) == 2
    assert missingNumber([0,1]) == 2
    assert missingNumber([9,6,4,2,3,5,7,0,1]) == 8
    assert missingNumber([0]) == 1
    assert missingNumber([1]) == 0
    assert missingNumber([2,0]) == 1
    assert missingNumber([4,2,1,0]) == 3
    assert missingNumber([1,2,3,4,5,6,7,8,9,10,12,13,14,15,16,17,18,19,20,0]) == 11