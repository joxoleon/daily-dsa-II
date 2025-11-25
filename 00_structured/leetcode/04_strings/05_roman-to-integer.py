# [ Name: Roman to Integer ]  [ Category: strings ]  [ Topic: strings ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/roman-to-integer/ ]

"""
Given a string representing a Roman numeral, convert it to an integer.
The input will be a valid Roman numeral in the range from 1 to 3999.
Return the integer value of the Roman numeral.
The input string uses characters 'I', 'V', 'X', 'L', 'C', 'D', and 'M'.
Example: Input: "MCMXCIV" Output: 1994
"""

def romanToInt(s: str) -> int:
    pass

if __name__ == "__main__":
    assert romanToInt("III") == 3
    assert romanToInt("IV") == 4
    assert romanToInt("IX") == 9
    assert romanToInt("LVIII") == 58
    assert romanToInt("MCMXCIV") == 1994
    assert romanToInt("CDXLIV") == 444
    assert romanToInt("MMM") == 3000
    assert romanToInt("DCCCXC") == 890