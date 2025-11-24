# [ Name: Add Two Numbers ]  [ Category: linked_list ]  [ Topic: linked_list ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/add-two-numbers/ ]

"""
Given two non-empty linked lists representing two non-negative integers in reverse order, add the two numbers and return the sum as a linked list. Each node contains a single digit. The inputs will not contain any leading zeros, except the number 0 itself.
Constraints: 1 <= list length <= 100, 0 <= Node.val <= 9.
Example: Input: l1 = [2,4,3], l2 = [5,6,4]  Output: [7,0,8]
"""

from typing import Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    pass

if __name__ == "__main__":
    def list_to_linked(lst):
        dummy = ListNode()
        cur = dummy
        for v in lst:
            cur.next = ListNode(v)
            cur = cur.next
        return dummy.next
    def linked_to_list(node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res
    assert linked_to_list(addTwoNumbers(list_to_linked([2,4,3]), list_to_linked([5,6,4]))) == [7,0,8]
    assert linked_to_list(addTwoNumbers(list_to_linked([0]), list_to_linked([0]))) == [0]
    assert linked_to_list(addTwoNumbers(list_to_linked([9,9,9,9,9,9,9]), list_to_linked([9,9,9,9]))) == [8,9,9,9,0,0,0,1]
    assert linked_to_list(addTwoNumbers(list_to_linked([1]), list_to_linked([9,9,9,9,9,9,9,9,9,9]))) == [0,0,0,0,0,0,0,0,0,0,1]
    assert linked_to_list(addTwoNumbers(list_to_linked([5]), list_to_linked([5]))) == [0,1]
    assert linked_to_list(addTwoNumbers(list_to_linked([1,8]), list_to_linked([0]))) == [1,8]
    assert linked_to_list(addTwoNumbers(list_to_linked([1,0,1]), list_to_linked([9,9,9]))) == [0,0,1,1]
    assert linked_to_list(addTwoNumbers(list_to_linked([9]), list_to_linked([1,9,9,9,9,9,9,9,9,9]))) == [0,0,0,0,0,0,0,0,0,0,1]