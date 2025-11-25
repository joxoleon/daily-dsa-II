# [ Name: Regular Expression Matching ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/regular-expression-matching/ ]

"""
Given strings s and p, determine if s matches the regular expression p.
p can contain '.' (matches any character) and '*' (matches zero or more of the preceding element).
Return True if the entire string s matches p; otherwise, False.
Constraints: 1 <= len(s), len(p) <= 20; s and p contain only lowercase letters, '.', or '*'.
Example: s = "aab", p = "c*a*b" returns True.
"""

from typing import List

def isMatch(s: str, p: str) -> bool:
    pass

if __name__ == "__main__":
    assert isMatch("aa", "a") == False
    assert isMatch("aa", "a*") == True
    assert isMatch("ab", ".*") == True
    assert isMatch("aab", "c*a*b") == True
    assert isMatch("mississippi", "mis*is*p*.") == False
    assert isMatch("mississippi", "mis*is*ip*.") == True
    assert isMatch("ab", ".*c") == False
    assert isMatch("aaa", "ab*a*c*a") == True