# [ Name: Basic Calculator II ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/basic-calculator-ii/ ]

"""
Given a string s representing a basic mathematical expression with non-negative integers and operators (+, -, *, /), evaluate and return the result as an integer. 
Spaces may be present.
s contains only valid characters and is guaranteed to be a valid expression.
Division should truncate toward zero.
Example: Input: s = "3+2*2" Output: 7
"""

def calculate(s: str) -> int:
    pass

if __name__ == "__main__":
    assert calculate("3+2*2") == 7
    assert calculate(" 3/2 ") == 1
    assert calculate(" 3+5 / 2 ") == 5
    assert calculate("14-3/2") == 13
    assert calculate("42") == 42
    assert calculate("0-2147483647") == -2147483647
    assert calculate("1*2-3/4+5*6-7*8+9/10") == -24
    assert calculate("100+200*3/4-50") == 100