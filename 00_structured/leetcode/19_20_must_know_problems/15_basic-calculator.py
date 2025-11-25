# [ Name: Basic Calculator ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/basic-calculator/ ]

"""
Implement a basic calculator to evaluate a simple expression string.
The expression string may contain non-negative integers, '+', '-', '(', ')' and spaces.
Return the integer result of the evaluated expression.
You may assume the input is always valid and only contains the characters described.
Constraints: 1 <= len(s) <= 3 * 10^5
Example: Input: s = "1 + (2 - 3)" -> Output: 0
"""

def calculate(s: str) -> int:
    pass

if __name__ == "__main__":
    assert calculate("1 + 1") == 2
    assert calculate(" 2-1 + 2 ") == 3
    assert calculate("(1+(4+5+2)-3)+(6+8)") == 23
    assert calculate("1-(5)") == -4
    assert calculate("2147483647") == 2147483647
    assert calculate("0") == 0
    assert calculate("20-(2+3)-(4-5)") == 16
    assert calculate("10-(2-(3-(4-(5-(6-7)))))") == 3
    assert calculate("7") == 7