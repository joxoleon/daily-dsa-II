# [ Name: Minimum Window Substring ]  [ Category: sliding_window ]  [ Topic: sliding_window ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/minimum-window-substring/ ]

"""
Given two strings s and t, return the minimum window substring of s such that every character in t is included in the window. If no such substring exists, return an empty string. Both s and t consist of English letters. 1 <= len(s), len(t) <= 10^5. Example: For s = "ADOBECODEBANC", t = "ABC", the output is "BANC".
"""

from typing import Optional

def min_window(s: str, t: str) -> str:
    pass

if __name__ == "__main__":
    assert min_window("ADOBECODEBANC", "ABC") == "BANC"
    assert min_window("a", "a") == "a"
    assert min_window("a", "aa") == ""
    assert min_window("ab", "b") == "b"
    assert min_window("bba", "ab") == "ba"
    assert min_window("bcaac", "aac") == "aac"
    assert min_window("abcdebdde", "bde") == "bdde"
    assert min_window("aaaaaaaaaaaabbbbbcdd", "abcdd") == "abbbbbcdd"