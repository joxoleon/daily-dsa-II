# [ Name: Cycle Detection (Floyd's Algorithm) ]  [ Category: linked_list ]  [ Topic: cycle ]  [ Weight: 9 ]

"""
Problem Description:
Given the head of a singly linked list, determine if the list has a cycle.
Return True if there is a cycle, otherwise return False.
The linked list nodes have a value and a next pointer, which may point to None or any node ahead.
Input: head of the linked list (may be None).
Constraints:
- 0 <= number of nodes <= 10^4
- Each node's value is an integer.

Example:
Input: 1 -> 2 -> 3 -> 2 (cycle back to node with value 2) => Output: True
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head: Optional[ListNode]) -> bool:
    pass

if __name__ == "__main__":
    # Test 1: No nodes (empty list)
    assert has_cycle(None) == False
    # Test 2: Single node, no cycle
    n1 = ListNode(1)
    assert has_cycle(n1) == False
    # Test 3: Single node pointing to itself (cycle)
    n1 = ListNode(2)
    n1.next = n1
    assert has_cycle(n1) == True
    # Test 4: Two nodes, no cycle
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    assert has_cycle(n1) == False
    # Test 5: Two nodes, cycle (second points to first)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n2.next = n1
    assert has_cycle(n1) == True
    # Test 6: Three nodes, no cycle
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    assert has_cycle(n1) == False
    # Test 7: Three nodes, last points to middle (cycle)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n2
    assert has_cycle(n1) == True
    # Test 8: Four nodes, last points to head (cycle)
    n1 = ListNode(3)
    n2 = ListNode(4)
    n3 = ListNode(5)
    n4 = ListNode(6)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n1
    assert has_cycle(n1) == True

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
