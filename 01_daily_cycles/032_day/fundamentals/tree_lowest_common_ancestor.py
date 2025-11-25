# [ Name: Tree — Lowest Common Ancestor ]  [ Category: trees ]  [ Topic: dfs ]  [ Weight: 9 ]

"""
Problem Description:
Given the root of a binary tree and two nodes p and q within the tree, return their lowest common ancestor (LCA).
The LCA is the deepest node that has both p and q as descendants (where a node can be a descendant of itself).
All node values are unique and both p and q will exist in the tree.

Constraints:
- 1 <= number of nodes <= 10^5

Example:
If p = 5 and q = 1 in the tree [3,5,1,6,2,0,8], output is 3.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def lowest_common_ancestor(root: Optional[TreeNode], p: TreeNode, q: TreeNode) -> TreeNode:
    pass

if __name__ == "__main__":
    # Tree:    3
    #        /   \
    #       5     1
    #      / \   / \
    #     6   2 0   8
    #        / \
    #       7   4
    n7 = TreeNode(7)
    n4 = TreeNode(4)
    n6 = TreeNode(6)
    n2 = TreeNode(2, n7, n4)
    n5 = TreeNode(5, n6, n2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n1 = TreeNode(1, n0, n8)
    root = TreeNode(3, n5, n1)

    # Main example
    assert lowest_common_ancestor(root, n5, n1) is root
    # LCA of 5 and 4 is 5
    assert lowest_common_ancestor(root, n5, n4) is n5
    # LCA of 6 and 4 is 5
    assert lowest_common_ancestor(root, n6, n4) is n5
    # LCA of 7 and 4 is 2
    assert lowest_common_ancestor(root, n7, n4) is n2
    # LCA of 0 and 8 is 1
    assert lowest_common_ancestor(root, n0, n8) is n1
    # LCA of 2 and 8 is root (3)
    assert lowest_common_ancestor(root, n2, n8) is root
    # LCA of 6 and 7 is 5
    assert lowest_common_ancestor(root, n6, n7) is n5
    # LCA of 3 and 4 is root (3)
    assert lowest_common_ancestor(root, root, n4) is root

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
