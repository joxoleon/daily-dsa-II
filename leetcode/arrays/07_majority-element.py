# [ Name: Majority Element ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/majority-element/ ]

"""
Given an array nums of size n, return the majority element.
The majority element is the element that appears more than ⌊n / 2⌋ times.
Assume that the majority element always exists in the array.
Input: nums = [3,2,3]
Output: 3
Constraints: 1 <= nums.length <= 5 * 10^4; nums[i] is an integer.
"""

from typing import List

def majorityElement(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert majorityElement([3,2,3]) == 3
    assert majorityElement([2,2,1,1,1,2,2]) == 2
    assert majorityElement([1]) == 1
    assert majorityElement([4,4,4,4,2,3,4]) == 4
    assert majorityElement([6,5,6]) == 6
    assert majorityElement([7,7,8,7,8,7,8,7,8,7,7]) == 7
    assert majorityElement([9,9,9,1,1,1,9]) == 9
    assert majorityElement([1000000]*100 + [2]*49) == 1000000
