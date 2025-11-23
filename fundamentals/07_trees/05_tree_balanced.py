# [ Name: Tree — Check if Balanced ]  [ Category: trees ]  [ Topic: dfs ]  [ Weight: 8 ]

"""
Problem Description:
Given the root of a binary tree, determine if the tree is height-balanced.
A binary tree is balanced if for every node, the heights of the left and right subtrees differ by no more than 1.
Return True if the tree is balanced, or False otherwise.

Constraints:
- Input: root node of a binary tree (0 <= number of nodes <= 10^4)
- Each node contains an integer value.

Example:
Input: root representing [3,9,20,null,null,15,7] -> Output: True
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: "Optional[TreeNode]" = None, right: "Optional[TreeNode]" = None):
        self.val = val
        self.left = left
        self.right = right

def is_balanced(root: Optional[TreeNode]) -> bool:
    pass

if __name__ == "__main__":
    # Utility: build trees for testing
    def build_tree(lst):
        if not lst: return None
        nodes = [TreeNode(x) if x is not None else None for x in lst]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    # Balanced trees
    assert is_balanced(build_tree([3,9,20,None,None,15,7])) == True
    assert is_balanced(build_tree([1,2,2,3,3,None,None,4,4])) == False
    assert is_balanced(build_tree([1])) == True
    assert is_balanced(build_tree([])) == True
    assert is_balanced(build_tree([1,2,2,3,None,None,3,4,None,None,4])) == False
    assert is_balanced(build_tree([1,2,2,3,None,None,3,4,None])) == False
    assert is_balanced(build_tree([1,2,3])) == True
    assert is_balanced(build_tree([1,2,None,3])) == False

    print("All tests passed.")
