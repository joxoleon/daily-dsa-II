# [ Name: Stack — Min Stack (O(1) Min Retrieval) ]  [ Category: stacks_and_queues ]  [ Topic: design ]  [ Weight: 6 ]

"""
Problem Description:
Design a stack that, in addition to standard push and pop operations, supports retrieving the minimum element in constant time.
Your MinStack should support push(val), pop(), top(), and getMin() methods.
- push(val): Pushes val onto the stack.
- pop(): Removes the element on top of the stack.
- top(): Returns the top element.
- getMin(): Returns the minimum element currently in the stack.

Constraints:
- All operations must run in O(1) time.
- Assume all values are valid integers.
- Calls to pop(), top(), and getMin() are guaranteed to be valid (the stack is not empty when called).

Example:
push(-2), push(0), push(-3), getMin() -> -3
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
    s.push(-1)
    assert s.top() == -1
    assert s.getMin() == -2
    s.pop()
    assert s.top() == 0
    s.pop()
    assert s.top() == -2
    assert s.getMin() == -2
    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")