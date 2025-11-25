# [ Name: Merge Two Sorted Linked Lists ]  [ Category: linked_list ]  [ Topic: merge ]  [ Weight: 7 ]

"""
Problem Description:
Given the heads of two sorted singly linked lists, merge them into one sorted linked list.
Return the head of the merged sorted list.
If either input list is empty, return the non-empty list.
Constraints:
- The input lists are sorted in non-decreasing order.
- The number of nodes in each list is in the range [0, 100].
Example:
Input: l1 = 1->2->4, l2 = 1->3->4; Output: 1->1->2->3->4->4
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    pass

def build_linked_list(values):
    head = current = None
    for v in values:
        node = ListNode(v)
        if not head:
            head = node
        else:
            current.next = node
        current = node
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

if __name__ == "__main__":
    l1 = build_linked_list([1,2,4])
    l2 = build_linked_list([1,3,4])
    merged = merge_lists(l1, l2)
    assert linked_list_to_list(merged) == [1,1,2,3,4,4]

    l1 = build_linked_list([])
    l2 = build_linked_list([0])
    merged = merge_lists(l1, l2)
    assert linked_list_to_list(merged) == [0]

    l1 = build_linked_list([2,5,7])
    l2 = build_linked_list([1,6,8])
    merged = merge_lists(l1, l2)
    assert linked_list_to_list(merged) == [1,2,5,6,7,8]

    l1 = build_linked_list([])
    l2 = build_linked_list([])
    merged = merge_lists(l1, l2)
    assert linked_list_to_list(merged) == []

    l1 = build_linked_list([1])
    l2 = build_linked_list([1])
    merged = merge_lists(l1, l2)
    assert linked_list_to_list(merged) == [1,1]

    l1 = build_linked_list([3,4,5])
    l2 = build_linked_list([1,2])
    merged = merge_lists(l1, l2)
    assert linked_list_to_list(merged) == [1,2,3,4,5]

    l1 = build_linked_list([0,2,2])
    l2 = build_linked_list([1,1,3])
    merged = merge_lists(l1, l2)
    assert linked_list_to_list(merged) == [0,1,1,2,2,3]

    l1 = build_linked_list([-10,-5,3])
    l2 = build_linked_list([-6,-2,7])
    merged = merge_lists(l1, l2)
    assert linked_list_to_list(merged) == [-10,-6,-5,-2,3,7]

    print("All tests passed.")
