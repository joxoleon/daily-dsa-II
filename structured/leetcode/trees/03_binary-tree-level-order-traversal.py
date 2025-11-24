# [ Name: Binary Tree Level Order Traversal ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/binary-tree-level-order-traversal/ ]

"""
Given the root of a binary tree, return the level order traversal of its nodes' values as a list of lists.
Input: root node of the binary tree.
Output: List of lists, where each sublist contains values at that tree level from left to right.
Constraints: 0 <= number of nodes <= 2000, -1000 <= Node.val <= 1000
Example: For a tree [3,9,20,null,null,15,7], output [[3],[9,20],[15,7]]
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    # Helper for test tree construction
    def build_tree(vals):
        if not vals:
            return None
        nodes = [TreeNode(v) if v is not None else None for v in vals]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    tree1 = build_tree([3,9,20,None,None,15,7])
    assert levelOrder(tree1) == [[3],[9,20],[15,7]]
    tree2 = build_tree([1])
    assert levelOrder(tree2) == [[1]]
    tree3 = build_tree([])
    assert levelOrder(tree3) == []
    tree4 = build_tree([1,2,3,4,None,None,5])
    assert levelOrder(tree4) == [[1],[2,3],[4,5]]
    tree5 = build_tree([1,None,2,3])
    assert levelOrder(tree5) == [[1],[2],[3]]
    tree6 = build_tree([1,2])
    assert levelOrder(tree6) == [[1],[2]]
    tree7 = build_tree([1,2,3,4,5,6,7])
    assert levelOrder(tree7) == [[1],[2,3],[4,5,6,7]]
    tree8 = build_tree([1,2,None,3,4])
    assert levelOrder(tree8) == [[1],[2],[3,4]]
