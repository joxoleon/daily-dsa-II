# [ Name: Decode Ways ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/decode-ways/ ]

"""
Given a string s containing only digits, return the total number of ways to decode it, where 'A' = "1", 'B' = "2", ..., 'Z' = "26".
Input: A string s representing a non-empty sequence of digits.
Output: An integer representing the number of possible decodings.
Constraints: 1 <= s.length <= 100; s contains only digits; s may contain '0'.
Example: Input: s = "226" Output: 3
"""

def numDecodings(s: str) -> int:
    pass

if __name__ == "__main__":
    assert numDecodings("12") == 2
    assert numDecodings("226") == 3
    assert numDecodings("06") == 0
    assert numDecodings("10") == 1
    assert numDecodings("27") == 1
    assert numDecodings("0") == 0
    assert numDecodings("11106") == 2
    assert numDecodings("1111111111") == 89