# [ Name: Evaluate Reverse Polish Notation ]  [ Category: stack ]  [ Topic: stack ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/evaluate-reverse-polish-notation/ ]

"""
Given a list of strings representing an arithmetic expression in Reverse Polish Notation (RPN), evaluate the expression and return the result as an integer.
Each operand may be an integer, and each operator is either '+', '-', '*', or '/'.
1 <= tokens.length <= 10^4
Operands are always valid, and division between two integers should truncate toward zero.
Example: Input: tokens = ["2","1","+","3","*"], Output: 9
"""

from typing import List

def evalRPN(tokens: List[str]) -> int:
    pass

if __name__ == "__main__":
    assert evalRPN(["2","1","+","3","*"]) == 9
    assert evalRPN(["4","13","5","/","+"]) == 6
    assert evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]) == 22
    assert evalRPN(["3","4","+"]) == 7
    assert evalRPN(["5","-3","/"]) == -1
    assert evalRPN(["0","3","/"]) == 0
    assert evalRPN(["100","200","+","2","/","5","*","7","+"]) == 757
    assert evalRPN(["7"]) == 7