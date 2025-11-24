# [ Name: Kth Smallest Element in a BST ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/ ]

"""
Given the root of a binary search tree and an integer k, return the kth smallest value among all nodes' values in the BST.
Input: root node of BST, integer k (1 ≤ k ≤ n, where n is the number of nodes)
Output: kth smallest integer in the tree
BST property: left < node < right at each node
Example: For BST [3,1,4,null,2], k=1 → Output: 1
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int=0, left: 'Optional[TreeNode]'=None, right: 'Optional[TreeNode]'=None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    pass

if __name__ == "__main__":
    # Helper to build BST from level order list
    def build_bst(values):
        if not values: return None
        nodes = [TreeNode(val) if val is not None else None for val in values]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    root1 = build_bst([3,1,4,None,2])
    assert kthSmallest(root1, 1) == 1
    assert kthSmallest(root1, 2) == 2

    root2 = build_bst([5,3,6,2,4,None,None,1])
    assert kthSmallest(root2, 3) == 3
    assert kthSmallest(root2, 1) == 1

    root3 = build_bst([2,1,3])
    assert kthSmallest(root3, 2) == 2

    root4 = build_bst([1,None,2])
    assert kthSmallest(root4, 2) == 2

    root5 = build_bst([3,1,4,None,2])
    assert kthSmallest(root5, 3) == 3

    root6 = build_bst([5])
    assert kthSmallest(root6, 1) == 5

    root7 = build_bst([2,1])
    assert kthSmallest(root7, 2) == 2

    root8 = build_bst([1])
    assert kthSmallest(root8, 1) == 1