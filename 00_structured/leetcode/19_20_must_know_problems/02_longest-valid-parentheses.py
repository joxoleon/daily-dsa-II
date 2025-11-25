# [ Name: Longest Valid Parentheses ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/longest-valid-parentheses/ ]

"""
Given a string s that contains only '(' and ')', return the length of the longest valid (well-formed) parentheses substring.
A valid parentheses substring is one where every opening '(' has a corresponding closing ')'.
Input: a string s of length up to 30,000.
Output: an integer representing the length of the longest valid substring.
Example: For s = "(()", the output is 2.
"""

def longestValidParentheses(s: str) -> int:
    pass

if __name__ == "__main__":
    assert longestValidParentheses("(()") == 2
    assert longestValidParentheses(")()())") == 4
    assert longestValidParentheses("") == 0
    assert longestValidParentheses("()(())") == 6
    assert longestValidParentheses("()(()") == 2
    assert longestValidParentheses("((()))") == 6
    assert longestValidParentheses(")()())()()(") == 4
    assert longestValidParentheses("())((())") == 4