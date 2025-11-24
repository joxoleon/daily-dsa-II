# [ Name: Validate Binary Search Tree ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/validate-binary-search-tree/ ]

"""
Determine if a given binary tree is a valid binary search tree (BST). A BST is defined as a binary tree in which the value of every node in the left subtree is less than the root’s value, and the value of every node in the right subtree is greater than the root’s value.
Input: root node of a binary tree.
Output: Boolean indicating if the tree is a valid BST.
Constraints: 0 <= Number of nodes <= 10^4; -2^31 <= Node value <= 2^31 - 1.
Example: Given root = [2,1,3], output is True.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    pass

if __name__ == "__main__":
    # Helper to build trees from list (None for empty)
    def build_tree(nodes):
        if not nodes: return None
        n = len(nodes)
        root = TreeNode(nodes[0]) if nodes[0] is not None else None
        queue = [root]
        i = 1
        while queue and i < n:
            curr = queue.pop(0)
            if curr:
                if i < n and nodes[i] is not None:
                    curr.left = TreeNode(nodes[i])
                queue.append(curr.left if i < n else None)
                i += 1
                if i < n and nodes[i] is not None:
                    curr.right = TreeNode(nodes[i])
                queue.append(curr.right if i < n else None)
                i += 1
        return root

    assert isValidBST(build_tree([2,1,3])) == True
    assert isValidBST(build_tree([5,1,4,None,None,3,6])) == False
    assert isValidBST(build_tree([])) == True
    assert isValidBST(build_tree([2147483647])) == True
    assert isValidBST(build_tree([10,5,15,None,None,6,20])) == False
    assert isValidBST(build_tree([1,1])) == False
    assert isValidBST(build_tree([3,None,30,10,None,None,15,None,45])) == False
    assert isValidBST(build_tree([0,None,-1])) == False