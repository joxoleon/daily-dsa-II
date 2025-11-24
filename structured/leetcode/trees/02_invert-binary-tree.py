# [ Name: Invert Binary Tree ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 8 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/invert-binary-tree/ ]

"""
Given the root of a binary tree, invert the tree, swapping every left and right child recursively. Return the root of the inverted tree.
Input: root node of a binary tree.
Output: the root node of the inverted tree.
Constraints: 0 <= number of nodes <= 100, -100 <= Node.val <= 100.
Example: Input: [4,2,7,1,3,6,9] Output: [4,7,2,9,6,3,1]
"""

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    pass

def serialize(root):
    # Helper: level order traversal to list, with None for missing nodes
    if not root:
        return []
    from collections import deque
    output = []
    q = deque([root])
    while q:
        node = q.popleft()
        if node:
            output.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            output.append(None)
    while output and output[-1] is None:
        output.pop()
    return output

def build_tree(lst):
    # Helper: build binary tree from list (level order), None allowed
    if not lst:
        return None
    from collections import deque
    root = TreeNode(lst[0])
    nodes = deque([root])
    idx = 1
    while nodes and idx < len(lst):
        node = nodes.popleft()
        if lst[idx] is not None:
            node.left = TreeNode(lst[idx])
            nodes.append(node.left)
        idx += 1
        if idx < len(lst) and lst[idx] is not None:
            node.right = TreeNode(lst[idx])
            nodes.append(node.right)
        idx += 1
    return root

if __name__ == "__main__":
    assert serialize(invertTree(None)) == []
    assert serialize(invertTree(build_tree([1]))) == [1]
    assert serialize(invertTree(build_tree([1,2]))) == [1,None,2]
    assert serialize(invertTree(build_tree([1,None,2]))) == [1,2]
    assert serialize(invertTree(build_tree([4,2,7,1,3,6,9]))) == [4,7,2,9,6,3,1]
    assert serialize(invertTree(build_tree([2,1,3]))) == [2,3,1]
    assert serialize(invertTree(build_tree([1,None,2,3]))) == [1,2,None,None,3]
    assert serialize(invertTree(build_tree([1,2,3,4,None,None,5]))) == [1,3,2,5,None,None,4]
