# [ Name: Word Break ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/word-break/ ]

"""
Given a string s and a list of words wordDict, determine if s can be segmented into a space-separated sequence of one or more words in wordDict.
s is a non-empty string containing only lowercase English letters.
wordDict contains distinct non-empty strings.
Return True if possible, otherwise False.
Example: s = "leetcode", wordDict = ["leet", "code"] => True
"""

from typing import List

def wordBreak(s: str, wordDict: List[str]) -> bool:
    pass

if __name__ == "__main__":
    assert wordBreak("leetcode", ["leet", "code"]) == True
    assert wordBreak("applepenapple", ["apple", "pen"]) == True
    assert wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) == False
    assert wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == True
    assert wordBreak("a", ["a"]) == True
    assert wordBreak("b", ["a"]) == False
    assert wordBreak("cars", ["car", "ca", "rs"]) == True
    assert wordBreak("aaaaaaa", ["aaaa", "aaa"]) == False