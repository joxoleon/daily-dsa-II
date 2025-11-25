# [ Name: Tree Traversal — Inorder ]  [ Category: trees ]  [ Topic: dfs ]  [ Weight: 5 ]

"""
Problem Description:
Given the root node of a binary tree, return the inorder traversal of its nodes' values as a list.
The binary tree may be empty; in this case, return an empty list.
Nodes may have only one child or none.
Constraints:
- 0 <= number of nodes <= 10^4

Example:
Input: root = [1, None, 2, 3] -> Output: [1, 3, 2]
"""

from typing import List, Optional

class TreeNode:
    def __init__(self, x: int, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = x
        self.left = left
        self.right = right

def inorder_traversal(root: Optional[TreeNode]) -> List[int]:
    pass

if __name__ == "__main__":
    # Helper to build trees quickly
    def node(x, l=None, r=None): return TreeNode(x, l, r)

    # Test 1: Empty tree
    assert inorder_traversal(None) == []
    # Test 2: Single node
    assert inorder_traversal(node(1)) == [1]
    # Test 3: Only left child
    assert inorder_traversal(node(2, node(1))) == [1,2]
    # Test 4: Only right child
    assert inorder_traversal(node(2, None, node(3))) == [2,3]
    # Test 5: Balanced tree
    t = node(2, node(1), node(3))
    assert inorder_traversal(t) == [1,2,3]
    # Test 6: Skewed left
    t = node(4, node(3, node(2, node(1))))
    assert inorder_traversal(t) == [1,2,3,4]
    # Test 7: Skewed right
    t = node(1, None, node(2, None, node(3)))
    assert inorder_traversal(t) == [1,2,3]
    # Test 8: Tree from example
    t = node(1, None, node(2, node(3)))
    assert inorder_traversal(t) == [1,3,2]

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")