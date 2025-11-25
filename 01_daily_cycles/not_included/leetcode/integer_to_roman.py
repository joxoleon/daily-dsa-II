# [ Name: Integer to Roman ]  [ Category: strings ]  [ Topic: strings ]  [ Weight: 6 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/integer-to-roman/ ]

"""
Given an integer, convert it to a Roman numeral.
- Input: integer num, 1 <= num <= 3999.
- Output: string representing the Roman numeral of num.
- All inputs are guaranteed to be within range.
Example: Input: num = 1994, Output: "MCMXCIV"
"""

def intToRoman(num: int) -> str:
    pass

if __name__ == "__main__":
    assert intToRoman(3) == "III"
    assert intToRoman(4) == "IV"
    assert intToRoman(9) == "IX"
    assert intToRoman(58) == "LVIII"
    assert intToRoman(1994) == "MCMXCIV"
    assert intToRoman(1) == "I"
    assert intToRoman(3999) == "MMMCMXCIX"
    assert intToRoman(44) == "XLIV"
    assert intToRoman(399) == "CCCXCIX"
