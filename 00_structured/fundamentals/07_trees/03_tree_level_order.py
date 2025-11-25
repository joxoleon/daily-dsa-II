# [ Name: Tree Traversal — Level Order BFS ]  [ Category: trees ]  [ Topic: bfs ]  [ Weight: 6 ]

"""
Problem Description:
Given the root of a binary tree, return its level order traversal as a list of lists.
Each sublist should contain the values of the nodes at each depth from top to bottom.
If the tree is empty, return an empty list.

Constraints:
- Tree nodes have integer values.
- 0 <= number of nodes <= 10^4.

Example:
Input: root = [3,9,20,None,None,15,7] -> Output: [[3], [9, 20], [15, 7]]
"""

from typing import Optional, List

class TreeNode:
    def __init__(self, val: int = 0, left: Optional['TreeNode'] = None, right: Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right

def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    # Utility function for Tree construction from list (BFS style)
    def build_tree(lst):
        if not lst: return None
        nodes = [TreeNode(val) if val is not None else None for val in lst]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids: node.left = kids.pop()
                if kids: node.right = kids.pop()
        return root

    assert level_order(build_tree([3,9,20,None,None,15,7])) == [[3],[9,20],[15,7]]
    assert level_order(build_tree([])) == []
    assert level_order(build_tree([1])) == [[1]]
    assert level_order(build_tree([1,2,3,4,5,None,7])) == [[1],[2,3],[4,5,7]]
    assert level_order(build_tree([2,None,3,None,4,None,5])) == [[2],[3],[4],[5]]
    assert level_order(build_tree([10,20,30,40,50,60,70])) == [[10],[20,30],[40,50,60,70]]
    assert level_order(build_tree([8,6,None,5,None,4])) == [[8],[6],[5],[4]]
    assert level_order(build_tree([1,None,2,3,None,None,4])) == [[1],[2],[3],[4]]

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
