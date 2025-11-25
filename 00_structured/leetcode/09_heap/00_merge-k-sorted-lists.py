# [ Name: Merge k Sorted Lists ]  [ Category: heap ]  [ Topic: heap ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/merge-k-sorted-lists/ ]

"""
Merge k sorted linked lists and return it as one sorted linked list.
Input: a list of ListNode objects, each representing the head of a sorted linked list.
Output: the head node of a single sorted linked list.
Constraints: k ranges from 0 to 10^4; each list has 0 to 500 nodes; node values are between -10^4 and 10^4.
Example: Input: lists = [[1,4,5],[1,3,4],[2,6]]; Output: [1,1,2,3,4,4,5,6]
"""

from typing import List, Optional

class ListNode:
    def __init__(self, val: int = 0, next: Optional['ListNode'] = None):
        self.val = val
        self.next = next
    def __eq__(self, other):
        a, b = self, other
        while a and b:
            if a.val != b.val:
                return False
            a, b = a.next, b.next
        return a is None and b is None
    def __repr__(self):
        vals = []
        node = self
        while node:
            vals.append(str(node.val))
            node = node.next
        return "[" + ",".join(vals) + "]"

def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    pass

def build_linked_list(lst):
    head = ListNode(0)
    curr = head
    for val in lst:
        curr.next = ListNode(val)
        curr = curr.next
    return head.next

def linked_list_to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

if __name__ == "__main__":
    assert mergeKLists([]) == None
    assert mergeKLists([None]) == None
    assert mergeKLists([build_linked_list([]), build_linked_list([])]) == None
    assert linked_list_to_list(mergeKLists([build_linked_list([1,4,5]), build_linked_list([1,3,4]), build_linked_list([2,6])])) == [1,1,2,3,4,4,5,6]
    assert linked_list_to_list(mergeKLists([build_linked_list([1]), build_linked_list([0])])) == [0,1]
    assert linked_list_to_list(mergeKLists([build_linked_list([2,3,7]), build_linked_list([1,2,3]), build_linked_list([5])])) == [1,2,2,3,3,5,7]
    assert linked_list_to_list(mergeKLists([build_linked_list([1,2,3])])) == [1,2,3]
    assert linked_list_to_list(mergeKLists([build_linked_list([]), build_linked_list([1]), build_linked_list([]), build_linked_list([0,2])])) == [0,1,2]
