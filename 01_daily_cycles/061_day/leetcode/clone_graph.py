# [ Name: Clone Graph ]  [ Category: graphs ]  [ Topic: graphs ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/clone-graph/ ]

"""
Given a reference of a node in a connected undirected graph, create a deep copy of the graph. Each node contains an integer value and a list of neighbors. Return the cloned graph's node. The number of nodes is in the range [0, 100], and node values are unique in [1, 100].
Example: For a graph with adjacency [[2,4],[1,3],[2,4],[1,3]], if you start with Node 1, output the root node of the cloned graph with identical structure.
"""

from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, neighbors: Optional[List['Node']] = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node: 'Optional[Node]') -> 'Optional[Node]':
    pass

if __name__ == "__main__":
    # Simple node with no neighbors
    n1 = Node(1)
    clone = cloneGraph(n1)
    assert clone is not n1
    assert clone.val == 1
    assert clone.neighbors == []

    # Two connected nodes
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]
    clone = cloneGraph(n1)
    assert clone.val == 1
    assert len(clone.neighbors) == 1
    assert clone.neighbors[0].val == 2
    assert clone.neighbors[0].neighbors[0] is clone

    # Square graph
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n1.neighbors = [n2, n4]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2, n4]
    n4.neighbors = [n1, n3]
    clone = cloneGraph(n1)
    assert clone.val == 1
    assert sorted([n.val for n in clone.neighbors]) == [2,4]
    n2_clone = [n for n in clone.neighbors if n.val == 2][0]
    n4_clone = [n for n in clone.neighbors if n.val == 4][0]
    assert clone in n2_clone.neighbors
    assert n4_clone in clone.neighbors

    # Null input
    assert cloneGraph(None) is None

    # Single node, self loop
    n1 = Node(1)
    n1.neighbors = [n1]
    clone = cloneGraph(n1)
    assert clone is not n1
    assert len(clone.neighbors) == 1
    assert clone.neighbors[0] is clone

    # Line graph: 1-2-3
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.neighbors = [n2]
    n2.neighbors = [n1, n3]
    n3.neighbors = [n2]
    clone = cloneGraph(n1)
    assert clone.val == 1
    n2_clone = clone.neighbors[0]
    n3_clone = [n for n in n2_clone.neighbors if n != clone][0]
    assert n3_clone.val == 3
    assert n2_clone in n3_clone.neighbors

    # Disjoint 2-node cycle and check different objects
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2]
    n2.neighbors = [n1]
    clone1 = cloneGraph(n1)
    clone2 = cloneGraph(n2)
    assert clone1 is not n1 and clone2 is not n2
    assert clone1 != clone2

    # Node with two neighbors, both same
    n1 = Node(1)
    n2 = Node(2)
    n1.neighbors = [n2, n2]
    n2.neighbors = [n1]
    clone = cloneGraph(n1)
    assert clone.neighbors[0] is clone.neighbors[1]
    assert clone.neighbors[0].val == 2
    assert clone in clone.neighbors[0].neighbors
