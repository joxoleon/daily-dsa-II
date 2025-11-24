# [ Name: Lowest Common Ancestor of a BST ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/ ]

"""
Given the root of a binary search tree and two nodes, p and q, return their lowest common ancestor node. The lowest common ancestor is the lowest node in the BST that has both p and q as descendants (including itself). Each node contains a unique integer value. Assume all TreeNode values are unique and both p and q exist in the BST.
Example: For root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8, output is 6.
Constraints: 2 <= Number of nodes <= 10^5
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    pass

if __name__ == "__main__":
    # Helper to build tree from list
    def build_bst_from_list(vals):
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

    tree1 = build_bst_from_list([6,2,8,0,4,7,9,None,None,3,5])
    p = tree1.left  # 2
    q = tree1.right # 8
    assert lowestCommonAncestor(tree1, p, q) == tree1

    tree2 = build_bst_from_list([6,2,8,0,4,7,9,None,None,3,5])
    p = tree2.left  # 2
    q = tree2.left.right.right # 5
    assert lowestCommonAncestor(tree2, p, q) == tree2.left

    tree3 = build_bst_from_list([2,1])
    p = tree3      # 2
    q = tree3.left # 1
    assert lowestCommonAncestor(tree3, p, q) == tree3

    tree4 = build_bst_from_list([5,3,6,2,4,None,None,1])
    p = tree4.left.left   # 2
    q = tree4.left        # 3
    assert lowestCommonAncestor(tree4, p, q) == tree4.left

    tree5 = build_bst_from_list([5,3,6,2,4,None,None,1])
    p = tree5.left.left.left  # 1
    q = tree5.left.right      # 4
    assert lowestCommonAncestor(tree5, p, q) == tree5.left

    tree6 = build_bst_from_list([6,2,8,0,4,7,9,None,None,3,5])
    p = tree6.right.left # 7
    q = tree6.right      # 8
    assert lowestCommonAncestor(tree6, p, q) == tree6.right

    tree7 = build_bst_from_list([2,1])
    p = tree7
    q = tree7
    assert lowestCommonAncestor(tree7, p, q) == tree7

    tree8 = build_bst_from_list([37,-34,-48,None,-100,-100,48,None,None,None,None,-54,None,-71,-22,None,None,None,8])
    p = tree8.left.right.right # -22
    q = tree8.left.right.left  # -71
    assert lowestCommonAncestor(tree8, p, q) == tree8.left.right