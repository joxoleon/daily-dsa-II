# [ Name: Reorder List ]  [ Category: linked_list ]  [ Topic: linked_list ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/reorder-list/ ]

"""
Given the head of a singly linked list, reorder the list such that the nodes are arranged in the order: first node, last node, second node, second last node, and so on. 
Return nothing; modify the list in-place.
Constraints: 1 <= number of nodes <= 5 * 10^4, -1000 <= Node.val <= 1000
Input: head = [1,2,3,4]
Output: [1,4,2,3]
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        pass

def build_linked_list(lst):
    dummy = ListNode(0)
    curr = dummy
    for v in lst:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_list_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

if __name__ == "__main__":
    s = Solution()
    head = build_linked_list([1,2,3,4])
    s.reorderList(head)
    assert linked_list_to_list(head) == [1,4,2,3]
    head = build_linked_list([1,2,3,4,5])
    s.reorderList(head)
    assert linked_list_to_list(head) == [1,5,2,4,3]
    head = build_linked_list([1])
    s.reorderList(head)
    assert linked_list_to_list(head) == [1]
    head = build_linked_list([1,2])
    s.reorderList(head)
    assert linked_list_to_list(head) == [1,2]
    head = build_linked_list([1,2,3])
    s.reorderList(head)
    assert linked_list_to_list(head) == [1,3,2]
    head = build_linked_list([100,-100,0,10])
    s.reorderList(head)
    assert linked_list_to_list(head) == [100,10,-100,0]
    head = build_linked_list([7,8,9,10,11,12])
    s.reorderList(head)
    assert linked_list_to_list(head) == [7,12,8,11,9,10]
    head = build_linked_list([-1,2,-3,4,-5,6,-7])
    s.reorderList(head)
    assert linked_list_to_list(head) == [-1,-7,2,6,-3,4,-5]