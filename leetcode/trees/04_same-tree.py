# [ Name: Same Tree ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/same-tree/ ]

"""
Given two binary trees, determine if they are structurally identical and have the same node values.
Input: root nodes of two binary trees, p and q.
Output: Return True if the trees are the same, otherwise False.
Constraints: 0 <= number of nodes <= 100; Node values are integers.
Example: For p = [1,2,3] and q = [1,2,3], output is True.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    pass

def build_tree(lst):
    if not lst:
        return None
    nodes = [None if val is None else TreeNode(val) for val in lst]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    assert isSameTree(build_tree([1,2,3]), build_tree([1,2,3])) == True
    assert isSameTree(build_tree([1,2]), build_tree([1,None,2])) == False
    assert isSameTree(build_tree([1,2,1]), build_tree([1,1,2])) == False
    assert isSameTree(build_tree([]), build_tree([])) == True
    assert isSameTree(build_tree([1]), build_tree([])) == False
    assert isSameTree(build_tree([1,None,2,3]), build_tree([1,None,2,3])) == True
    assert isSameTree(build_tree([1,2,3,None,None,4]), build_tree([1,2,3,None,None,4])) == True
    assert isSameTree(build_tree([1,2,3]), build_tree([1,2])) == False