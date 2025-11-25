# [ Name: Remove Duplicates from Sorted List ]  [ Category: linked_list ]  [ Topic: linked_list ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/remove-duplicates-from-sorted-list/ ]

"""
Given the head of a sorted linked list, remove all duplicates such that each element appears only once. 
Return the linked list sorted as well.
Constraints: The number of nodes in the list is in the range [0, 300]; -100 <= Node.val <= 100.
Example: Input: head = [1,1,2]; Output: [1,2]
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: Optional[ListNode]) -> Optional[ListNode]:
    pass

if __name__ == "__main__":
    def to_list(node):
        res = []
        while node:
            res.append(node.val)
            node = node.next
        return res
    def make_list(lst):
        dummy = ListNode()
        curr = dummy
        for x in lst:
            curr.next = ListNode(x)
            curr = curr.next
        return dummy.next

    assert to_list(deleteDuplicates(make_list([1,1,2]))) == [1,2]
    assert to_list(deleteDuplicates(make_list([1,1,2,3,3]))) == [1,2,3]
    assert to_list(deleteDuplicates(make_list([]))) == []
    assert to_list(deleteDuplicates(make_list([1]))) == [1]
    assert to_list(deleteDuplicates(make_list([1,1,1,1,1]))) == [1]
    assert to_list(deleteDuplicates(make_list([1,2,3,4,5]))) == [1,2,3,4,5]
    assert to_list(deleteDuplicates(make_list([-1,0,0,2,2,3]))) == [-1,0,2,3]
    assert to_list(deleteDuplicates(make_list([2,2,2,3,3,4,4,5,5,5,5,6,7,7]))) == [2,3,4,5,6,7]
