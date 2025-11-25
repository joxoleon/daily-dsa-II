# [ Name: DP — Jump Game Reachability ]  [ Category: dp ]  [ Topic: 1d_dp ]  [ Weight: 6 ]

"""
Problem Description:
Given a list of non-negative integers nums, where each element represents your maximum jump length from that position, determine if you can reach the last index starting from index 0.
Return True if you can reach the last index, otherwise return False.

Constraints:
- 1 <= len(nums) <= 10^4
- 0 <= nums[i] <= 10^5

Example:
Input: [2,3,1,1,4] -> Output: True
"""

from typing import List

def can_jump(nums: List[int]) -> bool:
    pass


if __name__ == "__main__":
    assert can_jump([2,3,1,1,4]) == True
    assert can_jump([3,2,1,0,4]) == False
    assert can_jump([0]) == True
    assert can_jump([1,0,1,0]) == False
    assert can_jump([1,1,1,1,1]) == True
    assert can_jump([2,0,0]) == True
    assert can_jump([0,1]) == False
    assert can_jump([5,4,3,2,1,0,0]) == False

    print("All tests passed.")
