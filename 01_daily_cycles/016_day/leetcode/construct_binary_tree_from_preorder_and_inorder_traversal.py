# [ Name: Construct Binary Tree from Preorder and Inorder Traversal ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/ ]

"""
Given two integer arrays preorder and inorder, return the binary tree constructed from those traversals. 
preorder and inorder are traversals of a binary tree containing unique values.
Constraints: 1 <= preorder.length == inorder.length <= 3000, values are unique.
Example: Given preorder = [3,9,20,15,7], inorder = [9,3,15,20,7], return the constructed binary tree with root value 3.
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    pass

if __name__ == "__main__":
    def serialize(root):
        if not root: return []
        from collections import deque
        out = []
        q = deque([root])
        while q:
            node = q.popleft()
            if node:
                out.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                out.append(None)
        while out and out[-1] is None:
            out.pop()
        return out

    assert serialize(buildTree([3,9,20,15,7],[9,3,15,20,7])) == [3,9,20,None,None,15,7]
    assert serialize(buildTree([1,2,3],[2,1,3])) == [1,2,3]
    assert serialize(buildTree([1,2],[2,1])) == [1,2]
    assert serialize(buildTree([1],[1])) == [1]
    assert serialize(buildTree([1,2,3,4],[4,3,2,1])) == [1,2,None,3,None,4]
    assert serialize(buildTree([2,1,3],[1,2,3])) == [2,1,3]
    assert serialize(buildTree([5,1,6,2],[1,5,2,6])) == [5,1,6,None,None,2]
    assert serialize(buildTree([4,2,1,3,6,5,7],[1,2,3,4,5,6,7])) == [4,2,6,1,3,5,7]
