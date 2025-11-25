# [ Name: Find All Anagrams in a String ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/find-all-anagrams-in-a-string/ ]

"""
Given two strings s and p, find all start indices of p's anagrams in s. Return the indices as a list.
s and p contain only lowercase English letters and may have different lengths.
Both strings' lengths are between 1 and 3 * 10^4.
Example: s = "cbaebabacd", p = "abc" returns [0, 6] as "cba" at 0 and "bac" at 6 are anagrams of "abc".
"""

from typing import List

def findAnagrams(s: str, p: str) -> List[int]:
    pass

if __name__ == "__main__":
    assert findAnagrams("cbaebabacd", "abc") == [0,6]
    assert findAnagrams("abab", "ab") == [0,1,2]
    assert findAnagrams("baa", "aa") == [1]
    assert findAnagrams("af", "be") == []
    assert findAnagrams("abc", "cba") == [0]
    assert findAnagrams("aaaaa", "aa") == [0,1,2,3]
    assert findAnagrams("abcdefg", "hij") == []
    assert findAnagrams("abbcacbabc", "abc") == [2,4,5,6]