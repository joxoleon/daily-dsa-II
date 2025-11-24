# [ Name: Valid Palindrome ]  [ Category: strings ]  [ Topic: strings ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/valid-palindrome/ ]

"""
Given a string s, determine if it is a palindrome, considering only alphanumeric characters and ignoring case.
Return True if s is a palindrome, False otherwise.
0 <= len(s) <= 2 * 10^5.
The string may contain spaces, symbols, or digits.
Example: Input: "A man, a plan, a canal: Panama"  Output: True
"""

def isPalindrome(s: str) -> bool:
    pass

if __name__ == "__main__":
    assert isPalindrome("A man, a plan, a canal: Panama") == True
    assert isPalindrome("race a car") == False
    assert isPalindrome("") == True
    assert isPalindrome(" ") == True
    assert isPalindrome("0P") == False
    assert isPalindrome("ab@a") == True
    assert isPalindrome("No lemon, no melon") == True
    assert isPalindrome("ab") == False