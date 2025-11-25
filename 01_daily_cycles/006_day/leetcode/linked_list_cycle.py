# [ Name: Linked List Cycle ]  [ Category: linked_list ]  [ Topic: linked_list ]  [ Weight: 9 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/linked-list-cycle/ ]

"""
Given the head of a linked list, determine if the linked list has a cycle in it.
Return True if a cycle exists, otherwise return False.
Input: head node of a singly-linked list.
There are no duplicate node values in the list.
Example: For head = [3,2,0,-4] with last node pointing to node at position 1, output is True.
Constraints: Number of nodes is in the range [0, 10^4]. Node values are in [-10^5, 10^5].
"""

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pass

if __name__ == "__main__":
    # Helper to build a list with/without cycle
    def make_list(arr, pos):
        nodes = [ListNode(v) for v in arr]
        for i in range(1, len(nodes)):
            nodes[i-1].next = nodes[i]
        if nodes and pos != -1:
            nodes[-1].next = nodes[pos]
        return nodes[0] if nodes else None

    s = Solution()
    head = make_list([3,2,0,-4], 1)
    assert s.hasCycle(head) == True
    head = make_list([1,2], 0)
    assert s.hasCycle(head) == True
    head = make_list([1], -1)
    assert s.hasCycle(head) == False
    head = make_list([1,2,3,4,5], -1)
    assert s.hasCycle(head) == False
    head = make_list([], -1)
    assert s.hasCycle(head) == False
    head = make_list([1], 0)
    assert s.hasCycle(head) == True
    head = make_list([1,2,3], 2)
    assert s.hasCycle(head) == True
    head = make_list([1,2,3], -1)
    assert s.hasCycle(head) == False
