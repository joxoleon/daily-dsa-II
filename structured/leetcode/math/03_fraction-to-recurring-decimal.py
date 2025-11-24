# [ Name: Fraction to Recurring Decimal ]  [ Category: math ]  [ Topic: math ]  [ Weight: 6 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/fraction-to-recurring-decimal/ ]

"""
Given two integers numerator and denominator, return the fraction in decimal form as a string. If the fractional part is repeating, enclose the repeating part in parentheses. Both numerator and denominator can be negative. Output must not contain unnecessary leading zeros.  
Constraints: -2^31 <= numerator, denominator <= 2^31-1, denominator != 0.
Example: numerator = 2, denominator = 3 -> "0.(6)"
"""

from typing import *

class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        pass

if __name__ == "__main__":
    s = Solution()
    assert s.fractionToDecimal(1, 2) == "0.5"
    assert s.fractionToDecimal(2, 1) == "2"
    assert s.fractionToDecimal(2, 3) == "0.(6)"
    assert s.fractionToDecimal(4, 333) == "0.(012)"
    assert s.fractionToDecimal(1, 5) == "0.2"
    assert s.fractionToDecimal(-50, 8) == "-6.25"
    assert s.fractionToDecimal(7, -12) == "-0.58(3)"
    assert s.fractionToDecimal(-22, -2) == "11"