# [ Name: Generate Parentheses ]  [ Category: stack ]  [ Topic: stack ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/generate-parentheses/ ]

"""
Given n pairs of parentheses, generate all combinations of well-formed parentheses.
Input: An integer n (1 ≤ n ≤ 8).
Output: A list of all valid strings with n pairs of parentheses.
Each result must be unique and use exactly n '(' and n ')'.
Example: Input: n = 3, Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

from typing import List

def generateParenthesis(n: int) -> List[str]:
    pass

if __name__ == "__main__":
    assert sorted(generateParenthesis(1)) == ["()"]
    assert sorted(generateParenthesis(2)) == ["(())","()()"]
    assert sorted(generateParenthesis(3)) == ["((()))","(()())","(())()","()(())","()()()"]
    assert len(generateParenthesis(4)) == 14
    assert "(((())))" in generateParenthesis(4)
    assert "()()()()" in generateParenthesis(4)
    assert len(set(generateParenthesis(5))) == 42
    assert all(len(s) == 6 for s in generateParenthesis(3))
    assert all(s.count('(') == s.count(')') == 4 for s in generateParenthesis(4))