# [ Name: Reverse Linked List ]  [ Category: linked_list ]  [ Topic: classic ]  [ Weight: 8 ]

"""
Problem Description:
Given the head of a singly linked list, reverse the list and return the new head.
The input is the head node of a singly linked list, which may be empty.
Return the head of the reversed linked list, or None for an empty list.

Constraints:
- 0 <= number of nodes <= 10^4

Example:
Input: 1 -> 2 -> 3 -> None  Output: 3 -> 2 -> 1 -> None
"""

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def reverse_list(head: Optional[ListNode]) -> Optional[ListNode]:
    pass

if __name__ == "__main__":
    def from_list(lst):
        dummy = ListNode(0)
        curr = dummy
        for val in lst:
            curr.next = ListNode(val)
            curr = curr.next
        return dummy.next

    def to_list(node):
        out = []
        while node:
            out.append(node.val)
            node = node.next
        return out

    a = from_list([])
    assert to_list(reverse_list(a)) == []

    a = from_list([1])
    assert to_list(reverse_list(a)) == [1]

    a = from_list([1, 2])
    assert to_list(reverse_list(a)) == [2, 1]

    a = from_list([1, 2, 3])
    assert to_list(reverse_list(a)) == [3, 2, 1]

    a = from_list([1, 2, 3, 4, 5])
    assert to_list(reverse_list(a)) == [5, 4, 3, 2, 1]

    a = from_list([2, 1])
    assert to_list(reverse_list(a)) == [1, 2]

    a = from_list([10, 20, 30, 40])
    assert to_list(reverse_list(a)) == [40, 30, 20, 10]

    a = from_list([7])
    assert to_list(reverse_list(a)) == [7]

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
