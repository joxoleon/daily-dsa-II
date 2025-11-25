# [ Name: Sqrt(x) ]  [ Category: math ]  [ Topic: math ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/sqrtx/ ]

"""
Given a non-negative integer x, compute and return the integer square root of x.
The returned value should be the greatest integer less than or equal to the true square root.
Input: a single integer x (0 <= x <= 2^31-1)
Output: integer, the truncated square root of x.
Example: Input: x = 8; Output: 2
"""

from typing import *

class Solution:
    def mySqrt(self, x: int) -> int:
        pass

if __name__ == "__main__":
    sol = Solution()
    assert sol.mySqrt(0) == 0
    assert sol.mySqrt(1) == 1
    assert sol.mySqrt(2) == 1
    assert sol.mySqrt(3) == 1
    assert sol.mySqrt(4) == 2
    assert sol.mySqrt(8) == 2
    assert sol.mySqrt(16) == 4
    assert sol.mySqrt(2147395599) == 46339