# [ Name: Check if Two Strings Are Anagrams ]  [ Category: strings ]  [ Topic: hashing ]  [ Weight: 6 ]

"""
Problem Description:
Given two strings s and t, determine if t is an anagram of s.
An anagram is formed by rearranging the letters of a string to produce another word, using all original letters exactly once.
Return True if t is an anagram of s, otherwise return False.

Constraints:
- Input strings may contain lowercase English letters only (1 <= len(s), len(t) <= 10^5)
- Strings of different lengths cannot be anagrams.

Example:
Input: s = "listen", t = "silent" -> Output: True
"""

def is_anagram(s: str, t: str) -> bool:
    n = len(s)
    k = len(t)
    if n != k:
        return False
    cm = [0 for _ in range(26)]
    for i in range(n):
        char_s = ord(s[i]) - ord('a')
        char_t = ord(t[i]) - ord('a')
        cm[char_s] += 1
        cm[char_t] -= 1
    for i in range(0, 26):
        if cm[i] != 0:
            return False
    return True

if __name__ == "__main__":
    assert is_anagram("listen", "silent") == True
    assert is_anagram("anagram", "nagaram") == True
    assert is_anagram("rat", "car") == False
    assert is_anagram("a", "a") == True
    assert is_anagram("a", "b") == False
    assert is_anagram("abc", "ab") == False
    assert is_anagram("abcde", "edcba") == True
    assert is_anagram("dormitory", "dirtyroom") == True

    print("All tests passed.")
