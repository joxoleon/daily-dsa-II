# [ Name: Number of 1 Bits ]  [ Category: bit_manipulation ]  [ Topic: bit_manipulation ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/number-of-1-bits/ ]

"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (its Hamming weight).
Input: an unsigned integer as a 32-bit integer.
Output: integer representing the count of '1' bits.
Constraints: The input is a 32-bit unsigned integer.
Example: Input: n = 11 (binary 00000000000000000000000000001011) Output: 3
"""

class Solution:
    def hammingWeight(self, n: int) -> int:
        pass

if __name__ == "__main__":
    sol = Solution()
    assert sol.hammingWeight(0b00000000000000000000000000000000) == 0
    assert sol.hammingWeight(0b00000000000000000000000000000001) == 1
    assert sol.hammingWeight(0b00000000000000000000000000001011) == 3
    assert sol.hammingWeight(0b00000000000000000000000010000000) == 1
    assert sol.hammingWeight(0b11111111111111111111111111111101) == 31
    assert sol.hammingWeight(0b00000000000000000000000000011111) == 5
    assert sol.hammingWeight(0b11111111111111111111111111111111) == 32
    assert sol.hammingWeight(0b01010101010101010101010101010101) == 16