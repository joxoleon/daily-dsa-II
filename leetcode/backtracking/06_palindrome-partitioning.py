# [ Name: Palindrome Partitioning ]  [ Category: backtracking ]  [ Topic: backtracking ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/palindrome-partitioning/ ]

"""
Given a string s, partition s such that every substring in the partition is a palindrome. 
Return all possible palindrome partitioning of s as a list of lists of strings.
1 <= len(s) <= 16
Each character in s is a lowercase English letter.
Example: For s = "aab", return [["a","a","b"],["aa","b"]].
"""

from typing import List

def partition(s: str) -> List[List[str]]:
    pass

if __name__ == "__main__":
    assert sorted(partition("aab")) == sorted([["a","a","b"],["aa","b"]])
    assert partition("a") == [["a"]]
    assert sorted(partition("aaba")) == sorted([["a","a","b","a"],["a","aba"],["aa","b","a"]])
    assert partition("abc") == [["a","b","c"]]
    assert sorted(partition("aaa")) == sorted([["a","a","a"],["a","aa"],["aa","a"],["aaa"]])
    assert sorted(partition("abba")) == sorted([["a","b","b","a"],["a","bb","a"],["abba"]])
    assert sorted(partition("racecar")) == sorted([["r","a","c","e","c","a","r"],["r","a","cec","a","r"],["r","aceca","r"],["racecar"]])
    assert sorted(partition("noon")) == sorted([["n","o","o","n"],["n","oo","n"],["noon"]])
    assert sorted(partition("civic")) == sorted([["c","i","v","i","c"],["c","ivi","c"],["civic"]])
