# [ Name: Tree — Maximum Depth ]  [ Category: trees ]  [ Topic: dfs ]  [ Weight: 7 ]

"""
Problem Description:
Given the root of a binary tree, return its maximum depth.
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.
If the tree is empty, return 0.

Constraints:
- The number of nodes is in the range [0, 10^4].
- The value of each node is an integer.

Example:
Input: root = [3,9,20,null,null,15,7] -> Output: 3
"""

from typing import Optional

class TreeNode:
    def __init__(self, val: int, left: 'Optional[TreeNode]'=None, right: 'Optional[TreeNode]'=None):
        self.val = val
        self.left = left
        self.right = right

def max_depth(root: Optional[TreeNode]) -> int:
    pass

if __name__ == "__main__":
    # Helper function to build tree from list, for testing
    def build_tree(lst):
        if not lst:
            return None
        nodes = [TreeNode(x) if x is not None else None for x in lst]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    assert max_depth(None) == 0
    assert max_depth(build_tree([1])) == 1
    assert max_depth(build_tree([1,2])) == 2
    assert max_depth(build_tree([1,2,3])) == 2
    assert max_depth(build_tree([3,9,20,None,None,15,7])) == 3
    assert max_depth(build_tree([1,None,2,None,3,None,4])) == 4
    assert max_depth(build_tree([1,2,2,3,3,None,None,4,4])) == 4
    assert max_depth(build_tree([1,2,3,4,None,None,5,None,6])) == 4

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
