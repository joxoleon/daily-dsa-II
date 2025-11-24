# [ Name: Permutation in String ]  [ Category: sliding_window ]  [ Topic: sliding_window ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/permutation-in-string/ ]

"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.
You may only use each character in s1 once. Both s1 and s2 consist of lowercase English letters.
Constraints: 1 <= s1.length, s2.length <= 10^4.
Example: For s1 = "ab", s2 = "eidbaooo", return true (because "ba" is a substring of s2).
"""

def checkInclusion(s1: str, s2: str) -> bool:
    pass

if __name__ == "__main__":
    assert checkInclusion("ab", "eidbaooo") == True
    assert checkInclusion("ab", "eidboaoo") == False
    assert checkInclusion("adc", "dcda") == True
    assert checkInclusion("hello", "ooolleoooleh") == False
    assert checkInclusion("a", "a") == True
    assert checkInclusion("a", "b") == False
    assert checkInclusion("abc", "ccccbbbbaaaa") == False
    assert checkInclusion("xyz", "afdgzyxksldfm") == True