# [ Name: Copy List with Random Pointer ]  [ Category: linked_list ]  [ Topic: linked_list ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/copy-list-with-random-pointer/ ]

"""
Given the head of a linked list where each node contains an integer value and a random pointer to any node or null,
return a deep copy of the list. The new list should have the same structure and values, but none of the original nodes.
head is the only input; return the head of the copied list.
Constraints: 0 <= number of nodes <= 1000. Node values are -10000 to 10000.
Example: If head = [7,null],[13,0],[11,4],[10,2],[1,0], output should be a copied list with the same sequence and random pointers.
"""

from typing import Optional

class Node:
    def __init__(self, val: int, next: 'Optional[Node]' = None, random: 'Optional[Node]' = None):
        self.val = val
        self.next = next
        self.random = random

def copyRandomList(head: 'Optional[Node]') -> 'Optional[Node]':
    pass

if __name__ == "__main__":
    # Helper function to build a list from a list of (val, random_index)
    def build_list(nodes):
        if not nodes:
            return None
        node_objs = [Node(val) for val, _ in nodes]
        for idx, (val, rand_idx) in enumerate(nodes):
            if idx < len(nodes) - 1:
                node_objs[idx].next = node_objs[idx+1]
            if rand_idx is not None:
                node_objs[idx].random = node_objs[rand_idx]
        return node_objs[0]

    # Helper function to serialize a linked list to a tuple of (val, random_index)
    def serialize(head):
        result = []
        node_to_index = {}
        cur = head
        idx = 0
        while cur:
            node_to_index[cur] = idx
            cur = cur.next
            idx += 1
        cur = head
        while cur:
            random_idx = node_to_index[cur.random] if cur.random else None
            result.append((cur.val, random_idx))
            cur = cur.next
        return result

    # Test 1: Single node, no random
    l1 = build_list([(1, None)])
    r1 = copyRandomList(l1)
    assert serialize(r1) == [(1, None)]

    # Test 2: Single node, random to self
    l2 = build_list([(2,0)])
    r2 = copyRandomList(l2)
    assert serialize(r2) == [(2,0)]

    # Test 3: Two nodes, linear, no randoms
    l3 = build_list([(1, None), (2, None)])
    r3 = copyRandomList(l3)
    assert serialize(r3) == [(1, None), (2, None)]

    # Test 4: Two nodes, random points ahead
    l4 = build_list([(9, 1), (5, None)])
    r4 = copyRandomList(l4)
    assert serialize(r4) == [(9, 1), (5, None)]

    # Test 5: Two nodes, random in circle
    l5 = build_list([(3, 1), (4, 0)])
    r5 = copyRandomList(l5)
    assert serialize(r5) == [(3,1),(4,0)]

    # Test 6: Three nodes, mixed randoms
    l6 = build_list([(7, None), (8,0), (9,1)])
    r6 = copyRandomList(l6)
    assert serialize(r6) == [(7,None),(8,0),(9,1)]

    # Test 7: Null input
    r7 = copyRandomList(None)
    assert r7 is None

    # Test 8: Four nodes, all randoms to self
    l8 = build_list([(2,0),(3,1),(4,2),(5,3)])
    r8 = copyRandomList(l8)
    assert serialize(r8) == [(2,0),(3,1),(4,2),(5,3)]