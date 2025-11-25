# [ Name: Zigzag Conversion ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 6 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/zigzag-conversion/ ]

"""
Convert a given string s to a zigzag pattern on a given number of rows, then read line by line to create a new string.
Input: s (1 <= len(s) <= 1000), numRows (1 <= numRows <= 1000)
Output: The string after zigzag conversion.
Example: Input: s = "PAYPALISHIRING", numRows = 3. Output: "PAHNAPLSIIGYIR"
"""

from typing import str

def convert(s: str, numRows: int) -> str:
    pass

if __name__ == "__main__":
    assert convert("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR"
    assert convert("PAYPALISHIRING", 4) == "PINALSIGYAHRPI"
    assert convert("A", 1) == "A"
    assert convert("ABC", 1) == "ABC"
    assert convert("ABCDE", 4) == "ABCED"
    assert convert("AB", 2) == "AB"
    assert convert("XYZ", 2) == "XZY"
    assert convert("HELLO", 3) == "HOELL"
