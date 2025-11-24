# [ Name: DP — Count Palindromic Substrings ]  [ Category: dp ]  [ Topic: 2d_dp ]  [ Weight: 7 ]

"""
Problem Description:
Given a string s, count the total number of palindromic substrings in s.
A substring is palindromic if it reads the same forwards and backwards.
Return the count as an integer.

Constraints:
- 1 <= len(s) <= 1000
- s consists of lowercase English letters only.

Example:
Input: "aaa" -> Output: 6
"""


def count_palindromic_substrings(s: str) -> int:
    pass


if __name__ == "__main__":
    assert count_palindromic_substrings("aaa") == 6
    assert count_palindromic_substrings("abc") == 3
    assert count_palindromic_substrings("racecar") == 10
    assert count_palindromic_substrings("a") == 1
    assert count_palindromic_substrings("abba") == 6
    assert count_palindromic_substrings("abcd") == 4
    assert count_palindromic_substrings("noon") == 6
    assert count_palindromic_substrings("level") == 7

    print("All tests passed.")
