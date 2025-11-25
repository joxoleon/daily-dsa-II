# [ Name: DP — Longest Common Subsequence ]  [ Category: dp ]  [ Topic: 2d_dp ]  [ Weight: 9 ]

"""
Problem Description:
Given two strings, find the length of their longest common subsequence (LCS).
A subsequence is a sequence that appears in the same order, but not necessarily contiguously, in both strings.
Return the length of the LCS as an integer.

Constraints:
- 1 <= len(text1), len(text2) <= 1000
- Strings consist of lowercase English letters.

Example:
Input: text1 = "abcde", text2 = "ace" -> Output: 3
"""


def lcs(text1: str, text2: str) -> int:
    pass


if __name__ == "__main__":
    assert lcs("abcde", "ace") == 3
    assert lcs("abc", "abc") == 3
    assert lcs("abc", "def") == 0
    assert lcs("", "abc") == 0
    assert lcs("abc", "") == 0
    assert lcs("bl", "ybyl") == 2
    assert lcs("abcdefg", "bdfg") == 4
    assert lcs("abcde", "fghij") == 0

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
