# [ Name: Reverse Linked List ]  [ Category: linked_list ]  [ Topic: linked_list ]  [ Weight: 10 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/reverse-linked-list/ ]

"""
Reverse a singly linked list.
Given the head node of a singly linked list, return the head of the reversed list.
Input: head as ListNode or None.
Output: head of reversed linked list.
Constraints: 0 <= number of nodes <= 5000. Node values are integers.
Example: Input: head = [1,2,3,4,5]; Output: [5,4,3,2,1]
"""

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    pass

def list_to_linked(lst):
    head = ListNode(0)
    curr = head
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return head.next

def linked_to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out

if __name__ == "__main__":
    assert linked_to_list(reverseList(list_to_linked([1,2,3,4,5]))) == [5,4,3,2,1]
    assert linked_to_list(reverseList(list_to_linked([1,2]))) == [2,1]
    assert linked_to_list(reverseList(list_to_linked([1]))) == [1]
    assert linked_to_list(reverseList(list_to_linked([]))) == []
    assert linked_to_list(reverseList(list_to_linked([7,3,9,4,2]))) == [2,4,9,3,7]
    assert linked_to_list(reverseList(list_to_linked([10,20,30,40]))) == [40,30,20,10]
    assert linked_to_list(reverseList(list_to_linked([-5,-10,-15]))) == [-15,-10,-5]
    assert linked_to_list(reverseList(list_to_linked([0]))) == [0]
