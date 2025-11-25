# [ Name: Populating Next Right Pointers in Each Node ]  [ Category: trees ]  [ Topic: trees ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/populating-next-right-pointers-in-each-node/ ]

"""
Given a perfect binary tree, populate each next pointer to point to its right adjacent node. 
If there is no right adjacent node, the next pointer should be set to None.
Input: The root node of a perfect binary tree.
Output: The same tree with updated next pointers.
Constraints: 1 <= number of nodes <= 2*10^4. Tree is perfect (all levels fully filled).
Example: Input: root = [1,2,3,4,5,6,7]
         Output next pointers: [1,#,2,3,#,4,5,6,7,#]
"""

from typing import Optional

class Node:
    def __init__(self, val: int = 0, left: 'Optional[Node]' = None, right: 'Optional[Node]' = None, next: 'Optional[Node]' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

def connect(root: Optional[Node]) -> Optional[Node]:
    pass

if __name__ == "__main__":
    # Helper to build perfect binary tree from list
    def build_perfect_binary_tree(values):
        if not values: return None
        nodes = [Node(v) if v is not None else None for v in values]
        n = len(values)
        for i in range(n):
            if nodes[i]:
                left_idx = 2*i+1
                right_idx = 2*i+2
                nodes[i].left = nodes[left_idx] if left_idx < n else None
                nodes[i].right = nodes[right_idx] if right_idx < n else None
        return nodes[0]

    # Helper to extract next pointers as list (level order, '#' per level)
    def extract_next_levels(root):
        result = []
        while root:
            node = root
            while node:
                result.append(node.val)
                node = node.next
            result.append('#')
            root = root.left if root else None
        return result

    # Test1: Basic 3-level tree
    root = build_perfect_binary_tree([1,2,3,4,5,6,7])
    assert extract_next_levels(connect(root)) == [1,'#',2,3,'#',4,5,6,7,'#']
    # Test2: Single node
    root = build_perfect_binary_tree([1])
    assert extract_next_levels(connect(root)) == [1,'#']
    # Test3: 2-level tree
    root = build_perfect_binary_tree([1,2,3])
    assert extract_next_levels(connect(root)) == [1,'#',2,3,'#']
    # Test4: 4-level tree
    root = build_perfect_binary_tree([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
    assert extract_next_levels(connect(root)) == [1,'#',2,3,'#',4,5,6,7,'#',8,9,10,11,12,13,14,15,'#']
    # Test5: None root
    root = build_perfect_binary_tree([])
    assert connect(root) is None
    # Test6: 5-level tree
    root = build_perfect_binary_tree(list(range(1,32)))
    expected = [1,'#',2,3,'#',4,5,6,7,'#',8,9,10,11,12,13,14,15,'#',16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,'#']
    assert extract_next_levels(connect(root)) == expected
    # Test7: Check pointers with duplicate values
    root = build_perfect_binary_tree([1,1,1,1,1,1,1])
    assert extract_next_levels(connect(root)) == [1,'#',1,1,'#',1,1,1,1,'#']
    # Test8: Minimal perfect two-level tree
    root = build_perfect_binary_tree([1,2,3])
    assert extract_next_levels(connect(root)) == [1,'#',2,3,'#']