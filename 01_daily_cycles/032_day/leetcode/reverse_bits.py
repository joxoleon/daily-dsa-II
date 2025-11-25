# [ Name: Reverse Bits ]  [ Category: bit_manipulation ]  [ Topic: bit_manipulation ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/reverse-bits/ ]

"""
Given a 32-bit unsigned integer, reverse its bits and return the resulting integer.
Input: A single integer n representing a 32-bit unsigned value.
Output: The reversed-bits integer as a 32-bit unsigned result.
Constraints: 0 <= n <= 2^32 - 1
Example: Input: n = 43261596 Output: 964176192
"""

def reverseBits(n: int) -> int:
    pass

if __name__ == "__main__":
    assert reverseBits(43261596) == 964176192
    assert reverseBits(4294967293) == 3221225471
    assert reverseBits(0) == 0
    assert reverseBits(1) == 2147483648
    assert reverseBits(4294967295) == 4294967295
    assert reverseBits(2) == 1073741824
    assert reverseBits(12) == 805306368
    assert reverseBits(256) == 8388608