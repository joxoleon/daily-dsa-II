# [ Name: DP — House Robber ]  [ Category: dp ]  [ Topic: 1d_dp ]  [ Weight: 7 ]

"""
Problem Description:
Given a list of non-negative integers representing the amount of money in each house, determine the maximum amount you can rob tonight without robbing two adjacent houses.
Return the maximum amount that can be robbed.

Constraints:
- Input: list of non-negative integers (0 <= len(nums) <= 10^4, 0 <= nums[i] <= 10^4)
- You cannot rob two directly adjacent houses.
- If the list is empty, return 0.

Example:
Input: [2, 7, 9, 3, 1] -> Output: 12
"""

from typing import List

def house_robber(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert house_robber([2, 7, 9, 3, 1]) == 12
    assert house_robber([1, 2, 3, 1]) == 4
    assert house_robber([2, 1, 1, 2]) == 4
    assert house_robber([]) == 0
    assert house_robber([0, 0, 0]) == 0
    assert house_robber([10]) == 10
    assert house_robber([4, 1, 2, 9, 1]) == 13
    assert house_robber([100, 1, 1, 100]) == 200

    print("All tests passed.")
