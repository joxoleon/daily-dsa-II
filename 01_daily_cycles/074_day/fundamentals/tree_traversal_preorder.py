# [ Name: Tree Traversal — Preorder ]  [ Category: trees ]  [ Topic: dfs ]  [ Weight: 5 ]

"""
Problem Description:
Given the root of a binary tree, return the preorder traversal of its node values as a list.
Preorder traversal visits the root first, then the left subtree, then the right subtree.
If the tree is empty, return an empty list.

Constraints:
- The number of nodes in the tree is in the range [0, 10^4].
- Node values are integers.

Example:
Input: [1,null,2,3] -> Output: [1,2,3]
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def preorder_traversal(root: Optional[TreeNode]) -> List[int]:
    pass

if __name__ == "__main__":
    # 1. Empty tree
    assert preorder_traversal(None) == []
    # 2. Single node tree
    t = TreeNode(7)
    assert preorder_traversal(t) == [7]
    # 3. Tree:    1
    #            / \
    #           2   3
    t = TreeNode(1, TreeNode(2), TreeNode(3))
    assert preorder_traversal(t) == [1,2,3]
    # 4. Tree:    1
    #              \
    #               2
    #                \
    #                 3
    t = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert preorder_traversal(t) == [1,2,3]
    # 5. Tree:      4
    #             /   \
    #            2     5
    #           / \
    #          1   3
    t = TreeNode(4, TreeNode(2, TreeNode(1), TreeNode(3)), TreeNode(5))
    assert preorder_traversal(t) == [4,2,1,3,5]
    # 6. Tree:   7
    #           /
    #          6
    t = TreeNode(7, TreeNode(6))
    assert preorder_traversal(t) == [7,6]
    # 7. Tree:      8
    #                 \
    #                  9
    t = TreeNode(8, None, TreeNode(9))
    assert preorder_traversal(t) == [8,9]
    # 8. Tree:      10
    #             /    \
    #           20     30
    #          /      /  \
    #         40     50   60
    t = TreeNode(10, TreeNode(20, TreeNode(40)), TreeNode(30, TreeNode(50), TreeNode(60)))
    assert preorder_traversal(t) == [10,20,40,30,50,60]

    print("All tests passed.")
