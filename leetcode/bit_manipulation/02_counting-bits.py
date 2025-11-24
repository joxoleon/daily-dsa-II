# [ Name: Counting Bits ]  [ Category: bit_manipulation ]  [ Topic: bit_manipulation ]  [ Weight: 8 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/counting-bits/ ]

"""
Given a non-negative integer n, return an array answer where answer[i] is the number of 1's in the binary representation of i for each i in the range [0, n].
Input: integer n (0 <= n <= 10^5)
Output: List[int] of length n+1
Example:
Input: n = 5
Output: [0,1,1,2,1,2]
"""

from typing import List

def countBits(n: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert countBits(0) == [0]
    assert countBits(1) == [0,1]
    assert countBits(2) == [0,1,1]
    assert countBits(3) == [0,1,1,2]
    assert countBits(4) == [0,1,1,2,1]
    assert countBits(5) == [0,1,1,2,1,2]
    assert countBits(10) == [0,1,1,2,1,2,2,3,1,2,2]
    assert countBits(15) == [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3,4]
