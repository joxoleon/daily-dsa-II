# [ Name: Valid Parentheses ]  [ Category: stack ]  [ Topic: stack ]  [ Weight: 10 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/valid-parentheses/ ]

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
Return True if all open brackets are closed by the same type and in correct order; otherwise return False.
s consists only of the above parentheses characters and is between 1 and 10,000 characters long.
Example: Input: s = "()[]{}" Output: True
"""

def isValid(s: str) -> bool:
    pass

if __name__ == "__main__":
    assert isValid("()") == True
    assert isValid("()[]{}") == True
    assert isValid("(]") == False
    assert isValid("([)]") == False
    assert isValid("{[]}") == True
    assert isValid("") == True
    assert isValid("((((") == False
    assert isValid("()()((()))") == True