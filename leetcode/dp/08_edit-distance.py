# [ Name: Edit Distance ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/edit-distance/ ]

"""
Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2. Each operation is either insert a character, delete a character, or replace a character.
Both strings have lengths between 0 and 500.
Example: word1 = "horse", word2 = "ros" returns 3.
"""

def minDistance(word1: str, word2: str) -> int:
    pass

if __name__ == "__main__":
    assert minDistance("horse", "ros") == 3
    assert minDistance("intention", "execution") == 5
    assert minDistance("", "") == 0
    assert minDistance("a", "") == 1
    assert minDistance("", "abc") == 3
    assert minDistance("abc", "abc") == 0
    assert minDistance("abc", "yabd") == 2
    assert minDistance("kitten", "sitting") == 3