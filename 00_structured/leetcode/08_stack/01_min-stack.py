# [ Name: Min Stack ]  [ Category: stack ]  [ Topic: stack ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/min-stack/ ]

"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time. 
Implement the MinStack class with methods to perform these operations. 
All operations should run in O(1) time.
Constraints: Up to 3 * 10^4 operations.
Example: 
MinStack minStack = MinStack(); minStack.push(-2); minStack.push(0); minStack.push(-3); minStack.getMin(); // returns -3; minStack.pop(); minStack.top(); // returns 0; minStack.getMin(); // returns -2
"""

class MinStack:
    def __init__(self):
        pass
    def push(self, val: int) -> None:
        pass
    def pop(self) -> None:
        pass
    def top(self) -> int:
        pass
    def getMin(self) -> int:
        pass

if __name__ == "__main__":
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    assert s.getMin() == -3
    s.pop()
    assert s.top() == 0
    assert s.getMin() == -2
    s.push(-4)
    assert s.getMin() == -4
    s.push(1)
    s.pop()
    assert s.top() == -4
    assert s.getMin() == -4
    s.pop()
    assert s.getMin() == -2