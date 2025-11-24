# [ Name: Binary Tree Maximum Path Sum ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/ ]

"""
Given a non-empty binary tree, find the maximum path sum.
A path is any sequence of nodes connected by edges, where each node appears at most once.
The path does not need to pass through the root.
Return an integer representing the maximum possible path sum.
Constraints: -10^4 <= Node.val <= 10^4, 1 <= number of nodes <= 3*10^4.
Example: Input: root = [1,2,3] → Output: 6
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        pass

def build_tree(nodes):
    if not nodes:
        return None
    tree = [TreeNode(val) if val is not None else None for val in nodes]
    kids = tree[::-1]
    root = kids.pop()
    for node in tree:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

if __name__ == "__main__":
    s = Solution()
    assert s.maxPathSum(build_tree([1,2,3])) == 6
    assert s.maxPathSum(build_tree([-10,9,20,None,None,15,7])) == 42
    assert s.maxPathSum(build_tree([2,-1])) == 2
    assert s.maxPathSum(build_tree([-3])) == -3
    assert s.maxPathSum(build_tree([1,-2,3])) == 4
    assert s.maxPathSum(build_tree([10,2,10,None,None,-20,-1])) == 22
    assert s.maxPathSum(build_tree([5,4,8,11,None,13,4,7,2,None,None,None,1])) == 48
    assert s.maxPathSum(build_tree([-1,-2,-3])) == -1