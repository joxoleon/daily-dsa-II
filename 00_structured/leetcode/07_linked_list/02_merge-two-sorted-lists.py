# [ Name: Merge Two Sorted Lists ]  [ Category: linked_list ]  [ Topic: linked_list ]  [ Weight: 9 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/merge-two-sorted-lists/ ]

"""
Merge two sorted linked lists and return a new sorted linked list.
Input: Two singly-linked lists head1 and head2, both sorted in non-decreasing order.
Output: The head of a new linked list, also sorted in non-decreasing order.
Both input lists may be empty; returned list should also be empty if both lists are empty.
Constraints: 0 <= Number of nodes in each list <= 50; -100 <= Node value <= 100.
Example: Input: (1 -> 2 -> 4), (1 -> 3 -> 4) Output: 1 -> 1 -> 2 -> 3 -> 4 -> 4
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    pass

if __name__ == "__main__":
    def build_list(lst):
        dummy = ListNode()
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

    # Test cases
    l1 = build_list([1,2,4])
    l2 = build_list([1,3,4])
    merged = mergeTwoLists(l1, l2)
    assert to_list(merged) == [1,1,2,3,4,4]
    l1 = build_list([])
    l2 = build_list([])
    merged = mergeTwoLists(l1, l2)
    assert to_list(merged) == []
    l1 = build_list([])
    l2 = build_list([0])
    merged = mergeTwoLists(l1, l2)
    assert to_list(merged) == [0]
    l1 = build_list([2])
    l2 = build_list([])
    merged = mergeTwoLists(l1, l2)
    assert to_list(merged) == [2]
    l1 = build_list([1,3,5,7])
    l2 = build_list([2,4,6,8])
    merged = mergeTwoLists(l1, l2)
    assert to_list(merged) == [1,2,3,4,5,6,7,8]
    l1 = build_list([1,1,1])
    l2 = build_list([1,1,1])
    merged = mergeTwoLists(l1, l2)
    assert to_list(merged) == [1,1,1,1,1,1]
    l1 = build_list([-10,-5,0,5])
    l2 = build_list([-7,-3,2,8])
    merged = mergeTwoLists(l1, l2)
    assert to_list(merged) == [-10,-7,-5,-3,0,2,5,8]
    l1 = build_list([5,10])
    l2 = build_list([1,3,7,11])
    merged = mergeTwoLists(l1, l2)
    assert to_list(merged) == [1,3,5,7,10,11]