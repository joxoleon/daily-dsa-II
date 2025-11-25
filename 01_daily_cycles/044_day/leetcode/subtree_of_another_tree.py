# [ Name: Subtree of Another Tree ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 8 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/subtree-of-another-tree/ ]

"""
Determine if one binary tree is a subtree of another.
Given two binary trees root and subRoot, return True if subRoot is a subtree of root.
A subtree of a binary tree is a tree consisting of a node and all its descendants in root.
Input: Two binary tree roots, root and subRoot.
Output: Boolean indicating if subRoot is a subtree of root.
Constraints: 1 <= number of nodes <= 2000, values are integers.
Example: root = [3,4,5,1,2], subRoot = [4,1,2] => True.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSubtree(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
    pass

if __name__ == "__main__":
    # Helper to build simple binary trees from list (None for empty)
    def build(values):
        if not values: return None
        nodes = [TreeNode(x) if x is not None else None for x in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    assert isSubtree(build([3,4,5,1,2]), build([4,1,2])) == True
    assert isSubtree(build([3,4,5,1,2,None,None,None,None,0]), build([4,1,2])) == False
    assert isSubtree(build([1,1]), build([1])) == True
    assert isSubtree(build([1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2]), build([1,2])) == True
    assert isSubtree(build([]), build([])) == True
    assert isSubtree(build([]), build([1])) == False
    assert isSubtree(build([1]), build([])) == True
    assert isSubtree(build([1,2,3,4,5,6,7]), build([3,6,7])) == True