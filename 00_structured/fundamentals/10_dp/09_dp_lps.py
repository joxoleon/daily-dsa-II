# [ Name: DP — Longest Palindromic Subsequence ]  [ Category: dp ]  [ Topic: 2d_dp ]  [ Weight: 8 ]

"""
Problem Description:
Given a string s, find the length of its longest palindromic subsequence.
A subsequence is a sequence obtained by deleting any number of characters without changing the order of the remaining characters.
Return an integer representing the maximal length of such a palindromic subsequence.

Constraints:
- 1 <= len(s) <= 1000
- s consists only of lowercase English letters.

Example:
Input: "bbbab" -> Output: 4
"""

def longest_palindromic_subsequence(s: str) -> int:
    pass


if __name__ == "__main__":
    assert longest_palindromic_subsequence("bbbab") == 4
    assert longest_palindromic_subsequence("cbbd") == 2
    assert longest_palindromic_subsequence("a") == 1
    assert longest_palindromic_subsequence("abcde") == 1
    assert longest_palindromic_subsequence("agbdba") == 5
    assert longest_palindromic_subsequence("aaaaa") == 5
    assert longest_palindromic_subsequence("abacdfgdcaba") == 5
    assert longest_palindromic_subsequence("racecar") == 7

    print("All tests passed.")
