# [ Name: Remove Nth Node From End ]  [ Category: linked_list ]  [ Topic: two_pointers ]  [ Weight: 7 ]

"""
Problem Description:
Given the head of a singly-linked list, remove the nth node from the end and return its head.
If n is equal to the length of the list, remove the first node.
You may assume the list has at least one node and 1 <= n <= length of the list.

Constraints:
- The number of nodes in the list is in the range [1, 10^4].
- Only valid values for n will be given.

Example:
Input: head = [1,2,3,4,5], n = 2 -> Output: [1,2,3,5]
"""

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    # Helper to easily compare linked lists in asserts
    def __eq__(self, other):
        if not isinstance(other, ListNode):
            return False
        a, b = self, other
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return a is None and b is None

    # Helper to build from list for testing
    @staticmethod
    def from_list(lst):
        dummy = ListNode(0)
        cur = dummy
        for val in lst:
            cur.next = ListNode(val)
            cur = cur.next
        return dummy.next

    # Helper for output display in test result
    def to_list(self):
        vals = []
        curr = self
        while curr:
            vals.append(curr.val)
            curr = curr.next
        return vals


def remove_nth_from_end(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    pass


if __name__ == "__main__":
    # Remove 2nd node from end from [1,2,3,4,5] -> [1,2,3,5]
    assert remove_nth_from_end(ListNode.from_list([1,2,3,4,5]), 2) == ListNode.from_list([1,2,3,5])
    # Remove last node -> [1,2,3,4]
    assert remove_nth_from_end(ListNode.from_list([1,2,3,4,5]), 1) == ListNode.from_list([1,2,3,4])
    # Remove first node (n == len) [2,3,4,5]
    assert remove_nth_from_end(ListNode.from_list([1,2,3,4,5]), 5) == ListNode.from_list([2,3,4,5])
    # Single element, remove that node -> []
    assert remove_nth_from_end(ListNode.from_list([42]), 1) == None
    # Remove middle node [1,3]
    assert remove_nth_from_end(ListNode.from_list([1,2,3]), 2) == ListNode.from_list([1,3])
    # Remove last from two [1]
    assert remove_nth_from_end(ListNode.from_list([1,2]), 1) == ListNode.from_list([1])
    # Remove first from two [2]
    assert remove_nth_from_end(ListNode.from_list([1,2]), 2) == ListNode.from_list([2])
    # Remove 3rd from end in length 3 [2,3]
    assert remove_nth_from_end(ListNode.from_list([1,2,3]), 3) == ListNode.from_list([2,3])

    print("All tests passed.")
