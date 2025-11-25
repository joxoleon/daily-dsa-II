# [ Name: Rotate Array ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/rotate-array/ ]

"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Return the modified array after rotation.
1 <= nums.length <= 10^5, 0 <= k <= 10^5, -2^31 <= nums[i] <= 2^31 - 1.
Example: Input: nums = [1,2,3,4,5,6,7], k = 3 Output: [5,6,7,1,2,3,4]
"""

from typing import List

def rotate(nums: List[int], k: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert rotate([1,2,3,4,5,6,7], 3) == [5,6,7,1,2,3,4]
    assert rotate([1,2], 0) == [1,2]
    assert rotate([1,2], 2) == [1,2]
    assert rotate([1], 10) == [1]
    assert rotate([1,2,3], 1) == [3,1,2]
    assert rotate([1,2,3], 4) == [3,1,2]
    assert rotate([-1,-100,3,99], 2) == [3,99,-1,-100]
    assert rotate([], 1) == []
