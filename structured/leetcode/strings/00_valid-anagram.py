# [ Name: Valid Anagram ]  [ Category: strings ]  [ Topic: strings ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/valid-anagram/ ]

"""
Given two strings s and t, determine if t is an anagram of s. 
An anagram is formed by rearranging the letters of a word to produce a new word with the same letters with the same frequency.
Both strings consist of lowercase English letters and have lengths up to 5 * 10^4.
Return True if t is an anagram of s, else return False.
Example: s = "anagram", t = "nagaram" → True
"""

def isAnagram(s: str, t: str) -> bool:
    pass

if __name__ == "__main__":
    assert isAnagram("anagram", "nagaram") == True
    assert isAnagram("rat", "car") == False
    assert isAnagram("a", "a") == True
    assert isAnagram("ab", "ba") == True
    assert isAnagram("abcd", "abc") == False
    assert isAnagram("aa", "bb") == False
    assert isAnagram("", "") == True
    assert isAnagram("listen", "silent") == True