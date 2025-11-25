# [ Name: Valid Palindrome II ]  [ Category: two_pointers ]  [ Topic: two_pointers ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/valid-palindrome-ii/ ]

"""
Given a string s, return True if it can be a palindrome after deleting at most one character.
s consists of lowercase English letters, 1 <= len(s) <= 10^5.
Example: For s = "abca", return True since removing 'b' or 'c' results in a palindrome.
"""

from typing import *

class Solution:
    def validPalindrome(self, s: str) -> bool:
        pass

if __name__ == "__main__":
    sol = Solution()
    assert sol.validPalindrome("aba") == True
    assert sol.validPalindrome("abca") == True
    assert sol.validPalindrome("abc") == False
    assert sol.validPalindrome("deeee") == True
    assert sol.validPalindrome("cbbcc") == True
    assert sol.validPalindrome("abcdefdba") == False
    assert sol.validPalindrome("a") == True
    assert sol.validPalindrome("abccbxa") == True