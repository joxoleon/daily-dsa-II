# [ Name: Maximum Depth of Binary Tree ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 7 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/maximum-depth-of-binary-tree/ ]

"""
Given a binary tree, return its maximum depth.
The maximum depth is the number of nodes along the longest path from the root down to the farthest leaf node.
Input: root node of a binary tree (may be None).
Output: an integer representing the max depth.
Constraints: Number of nodes in the tree is [0, 10^4]; values are integers.
Example: For root = [3,9,20,null,null,15,7], output is 3.
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    pass

if __name__ == "__main__":
    # Test 1: Empty tree
    assert maxDepth(None) == 0
    # Test 2: Single node
    assert maxDepth(TreeNode(1)) == 1
    # Test 3: Root with two children
    assert maxDepth(TreeNode(1, TreeNode(2), TreeNode(3))) == 2
    # Test 4: Left skewed tree
    node = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))))
    assert maxDepth(node) == 4
    # Test 5: Right skewed tree
    node = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert maxDepth(node) == 3
    # Test 6: Full binary tree of depth 3
    node = TreeNode(1,
                    TreeNode(2, TreeNode(4), TreeNode(5)),
                    TreeNode(3, TreeNode(6), TreeNode(7)))
    assert maxDepth(node) == 3
    # Test 7: Imbalanced tree
    node = TreeNode(1, TreeNode(2, TreeNode(3, TreeNode(4))), TreeNode(5))
    assert maxDepth(node) == 4
    # Test 8: Tree with only left grandchildren
    node = TreeNode(1, TreeNode(2, TreeNode(4)), TreeNode(3))
    assert maxDepth(node) == 3