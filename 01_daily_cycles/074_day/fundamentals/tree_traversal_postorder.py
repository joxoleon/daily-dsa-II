# [ Name: Tree Traversal — Postorder ]  [ Category: trees ]  [ Topic: dfs ]  [ Weight: 5 ]

"""
Problem Description:
Given the root of a binary tree, return the postorder traversal of its nodes' values as a list.
Postorder traversal visits the left subtree, then the right subtree, then the node itself.
The input tree may be empty, in which case return an empty list.

Constraints:
- The number of nodes is in the range [0, 10^4].
- Node values are integers.

Example:
Input: [1,null,2,3]  Output: [3,2,1]
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: 'Optional[TreeNode]' = None, right: 'Optional[TreeNode]' = None):
        self.val = val
        self.left = left
        self.right = right

def postorder_traversal(root: Optional[TreeNode]) -> List[int]:
    pass

if __name__ == "__main__":
    # Test 1: Empty tree
    assert postorder_traversal(None) == []
    # Test 2: Single node
    root = TreeNode(5)
    assert postorder_traversal(root) == [5]
    # Test 3: Left-skewed tree (3 -> 2 -> 1)
    root = TreeNode(3, TreeNode(2, TreeNode(1)))
    assert postorder_traversal(root) == [1,2,3]
    # Test 4: Right-skewed tree (1 -> 2 -> 3)
    root = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert postorder_traversal(root) == [3,2,1]
    # Test 5: Complete binary tree
    root = TreeNode(1, TreeNode(2), TreeNode(3))
    assert postorder_traversal(root) == [2,3,1]
    # Test 6: Full tree with both children at multiple levels
    root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
    assert postorder_traversal(root) == [4,5,2,3,1]
    # Test 7: Unbalanced tree (mix of left and right)
    root = TreeNode(1, TreeNode(2, None, TreeNode(4)), TreeNode(3))
    assert postorder_traversal(root) == [4,2,3,1]
    # Test 8: Example from description [1,null,2,3]
    r = TreeNode(1)
    r.right = TreeNode(2)
    r.right.left = TreeNode(3)
    assert postorder_traversal(r) == [3,2,1]

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
