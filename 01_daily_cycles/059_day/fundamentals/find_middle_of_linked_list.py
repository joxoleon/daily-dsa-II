# [ Name: Find Middle of Linked List ]  [ Category: linked_list ]  [ Topic: two_pointers ]  [ Weight: 6 ]

"""
Problem Description:
Given the head of a singly linked list, return the middle node.
If there are two middle nodes, return the second middle node.
Input: head node of a singly linked list (1 <= length <= 100)
Output: reference to the middle ListNode (not the value)
Example: For 1->2->3->4->5->null, return node with value 3.
Constraints: The list is non-empty.
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def middle_node(head: Optional[ListNode]) -> Optional[ListNode]:
    pass


if __name__ == "__main__":
    # Helper to make list from Python list
    def make_linked(lst):
        dummy = ListNode(0)
        cur = dummy
        for x in lst:
            cur.next = ListNode(x)
            cur = cur.next
        return dummy.next
    # Helper to get value at node
    def node_val(node):
        return node.val if node else None

    # Test 1: Odd length
    l1 = make_linked([1,2,3,4,5])
    assert node_val(middle_node(l1)) == 3
    # Test 2: Even length
    l2 = make_linked([1,2,3,4,5,6])
    assert node_val(middle_node(l2)) == 4
    # Test 3: Single element
    l3 = make_linked([7])
    assert node_val(middle_node(l3)) == 7
    # Test 4: Two elements
    l4 = make_linked([1,2])
    assert node_val(middle_node(l4)) == 2
    # Test 5: Three elements
    l5 = make_linked([4,9,5])
    assert node_val(middle_node(l5)) == 9
    # Test 6: Four elements
    l6 = make_linked([10,20,30,40])
    assert node_val(middle_node(l6)) == 30
    # Test 7: Five elements
    l7 = make_linked([8,7,6,5,4])
    assert node_val(middle_node(l7)) == 6
    # Test 8: Long list (length 8)
    l8 = make_linked([1,2,3,4,5,6,7,8])
    assert node_val(middle_node(l8)) == 5

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
