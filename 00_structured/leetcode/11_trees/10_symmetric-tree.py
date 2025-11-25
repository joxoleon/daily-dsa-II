# [ Name: Symmetric Tree ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 8 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/symmetric-tree/ ]

"""
Given the root of a binary tree, determine if it is a mirror of itself (symmetric around its center).
Input: root node of a binary tree.
Output: True if the tree is symmetric, False otherwise.
Constraints: 1 <= number of nodes <= 1000; -100 <= Node.val <= 100.
Example: If root = [1,2,2,3,4,4,3], output is True.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: Optional[TreeNode]) -> bool:
    pass

if __name__ == "__main__":
    # Helper to build tree from list
    def build_tree(lst):
        if not lst: return None
        nodes = [TreeNode(val) if val is not None else None for val in lst]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    assert isSymmetric(build_tree([1,2,2,3,4,4,3])) == True
    assert isSymmetric(build_tree([1,2,2,None,3,None,3])) == False
    assert isSymmetric(build_tree([1])) == True
    assert isSymmetric(build_tree([1,2,2,3,None,None,3])) == True
    assert isSymmetric(build_tree([1,2,2,3,None,None,4])) == False
    assert isSymmetric(build_tree([1,2,2,2,None,2])) == False
    assert isSymmetric(build_tree([1,2,2,None,3,3])) == True
    assert isSymmetric(build_tree([1,2,2,3,4,4,5])) == False