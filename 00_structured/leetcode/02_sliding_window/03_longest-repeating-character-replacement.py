# [ Name: Longest Repeating Character Replacement ]  [ Category: sliding_window ]  [ Topic: sliding_window ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/longest-repeating-character-replacement/ ]

"""
Given a string s and an integer k, find the length of the longest substring where you can replace at most k characters so all characters become the same.
Return that maximum length.
1 <= s.length <= 10^5, s consists of uppercase English letters.
0 <= k <= s.length
Example: 
Input: s = "AABABBA", k = 1. Output: 4
"""

from typing import *

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        pass

if __name__ == "__main__":
    sol = Solution()
    assert sol.characterReplacement("AABABBA", 1) == 4
    assert sol.characterReplacement("ABAB", 2) == 4
    assert sol.characterReplacement("AAAA", 0) == 4
    assert sol.characterReplacement("ABCDE", 1) == 2
    assert sol.characterReplacement("AABABBA", 0) == 2
    assert sol.characterReplacement("A", 0) == 1
    assert sol.characterReplacement("BAAAB", 2) == 5
    assert sol.characterReplacement("ABBB", 2) == 4