# [ Name: Longest Common Prefix ]  [ Category: strings ]  [ Topic: strings ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/longest-common-prefix/ ]

"""
Given an array of strings, find the longest common prefix among them.
Return the longest common prefix string, or an empty string if there is none.
Input: List of strings with length between 1 and 200.
Each string contains only lowercase English letters.
Example: Input: ["flower","flow","flight"] Output: "fl"
"""

from typing import List

def longestCommonPrefix(strs: List[str]) -> str:
    pass

if __name__ == "__main__":
    assert longestCommonPrefix(["flower","flow","flight"]) == "fl"
    assert longestCommonPrefix(["dog","racecar","car"]) == ""
    assert longestCommonPrefix(["interview","interval","integrate"]) == "int"
    assert longestCommonPrefix(["a"]) == "a"
    assert longestCommonPrefix(["aaa","aaa","aaa"]) == "aaa"
    assert longestCommonPrefix(["","b"]) == ""
    assert longestCommonPrefix(["ab","a"]) == "a"
    assert longestCommonPrefix(["abc","def"]) == ""