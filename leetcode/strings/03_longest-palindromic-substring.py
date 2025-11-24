# [ Name: Longest Palindromic Substring ]  [ Category: strings ]  [ Topic: strings ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/longest-palindromic-substring/ ]

"""
Given a string s, return the longest palindromic substring in s.
The input s consists of only digits and English letters, with length 1 to 1000.
The returned substring must be contiguous and can be any of the possible longest palindromes.
Example: For s = "babad", output could be "bab" or "aba".
"""

def longestPalindrome(s: str) -> str:
    pass

if __name__ == "__main__":
    assert longestPalindrome("babad") in {"bab", "aba"}
    assert longestPalindrome("cbbd") == "bb"
    assert longestPalindrome("a") == "a"
    assert longestPalindrome("ac") in {"a", "c"}
    assert longestPalindrome("racecar") == "racecar"
    assert longestPalindrome("abacdfgdcaba") in {"aba", "aca"}
    assert longestPalindrome("abcda") in {"a", "b", "c", "d"}
    assert longestPalindrome("aaaa") == "aaaa"