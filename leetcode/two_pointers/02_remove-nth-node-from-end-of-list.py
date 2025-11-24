# [ Name: Remove Nth Node From End of List ]  [ Category: two_pointers ]  [ Topic: two_pointers ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/ ]

"""
Given the head of a linked list, remove the nth node from the end and return its head.
Input: head (ListNode), n (int)
Output: ListNode (head of the modified list)
Constraints: 1 <= n <= length of list, 1 <= list length <= 30.
Example: head = [1,2,3,4,5], n = 2 ⇒ Output: [1,2,3,5]
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    pass

def build_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next

def list_to_pylist(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

if __name__ == "__main__":
    assert list_to_pylist(removeNthFromEnd(build_list([1,2,3,4,5]), 2)) == [1,2,3,5]
    assert list_to_pylist(removeNthFromEnd(build_list([1]), 1)) == []
    assert list_to_pylist(removeNthFromEnd(build_list([1,2]), 1)) == [1]
    assert list_to_pylist(removeNthFromEnd(build_list([1,2]), 2)) == [2]
    assert list_to_pylist(removeNthFromEnd(build_list([1,2,3]), 3)) == [2,3]
    assert list_to_pylist(removeNthFromEnd(build_list([1,2,3]), 2)) == [1,3]
    assert list_to_pylist(removeNthFromEnd(build_list([5,6,7,8]), 4)) == [6,7,8]
    assert list_to_pylist(removeNthFromEnd(build_list([9,9,9,9,9]), 1)) == [9,9,9,9]