# [ Name: Climbing Stairs ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/climbing-stairs/ ]

"""
You are climbing a staircase with n steps. Each time you can climb either 1 or 2 steps.
Given the total number of steps n, return the number of distinct ways to reach the top.
1 <= n <= 45
Example: Input: n = 3. Output: 3. (ways: 1+1+1, 1+2, 2+1)
"""

def climbStairs(n: int) -> int:
    pass

if __name__ == "__main__":
    assert climbStairs(2) == 2
    assert climbStairs(3) == 3
    assert climbStairs(4) == 5
    assert climbStairs(5) == 8
    assert climbStairs(1) == 1
    assert climbStairs(10) == 89
    assert climbStairs(20) == 10946
    assert climbStairs(15) == 987