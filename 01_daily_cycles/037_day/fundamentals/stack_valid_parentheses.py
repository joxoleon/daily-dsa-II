# [ Name: Stack — Valid Parentheses ]  [ Category: stacks_and_queues ]  [ Topic: basic_stack ]  [ Weight: 7 ]

"""
Problem Description:
Given a string containing only the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if all open brackets are closed by the same type of brackets, and in the correct order.
Return True if the string is valid, otherwise return False.

Constraints:
- 0 <= len(s) <= 10^4
- Input contains only the characters (), {}, []

Example:
Input: s = "({[]})" -> Output: True
"""

def is_valid_parentheses(s: str) -> bool:
    pass

if __name__ == "__main__":
    assert is_valid_parentheses("") == True
    assert is_valid_parentheses("()") == True
    assert is_valid_parentheses("([{}])") == True
    assert is_valid_parentheses("({[}])") == False
    assert is_valid_parentheses("(((())))") == True
    assert is_valid_parentheses("(()") == False
    assert is_valid_parentheses("{[]}") == True
    assert is_valid_parentheses("{[}]") == False

    print("All tests passed.")