# [ Name: DP — Climbing Stairs ]  [ Category: dp ]  [ Topic: 1d_dp ]  [ Weight: 6 ]

"""
Problem Description:
Given a staircase with n steps, you can climb either 1 or 2 steps at a time.
Return the total number of distinct ways to reach the top of the staircase.
Input: integer n (number of steps), where 1 <= n <= 45.
Output: integer representing the number of ways to climb to the top.

Example:
Input: 3 -> Output: 3  (1+1+1, 1+2, 2+1)
"""


def climb_stairs(n: int) -> int:
    pass


if __name__ == "__main__":
    assert climb_stairs(1) == 1
    assert climb_stairs(2) == 2
    assert climb_stairs(3) == 3
    assert climb_stairs(4) == 5
    assert climb_stairs(5) == 8
    assert climb_stairs(10) == 89
    assert climb_stairs(20) == 10946
    assert climb_stairs(45) == 1836311903

    print("All tests passed.")
