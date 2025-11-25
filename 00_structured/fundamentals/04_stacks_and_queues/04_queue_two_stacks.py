# [ Name: Queue Implemented Using Two Stacks ]  [ Category: stacks_and_queues ]  [ Topic: design ]  [ Weight: 5 ]

"""
Problem Description:
Design a queue using only two stacks. 
Implement the class MyQueue with methods to push an integer to the back, pop the front element, peek at the front, and check if the queue is empty.
All operations must emulate a standard queue (FIFO).
Input: sequence of push, pop, peek, and empty operations.
Output: return the expected value for pop, peek, and empty; push returns nothing.

Constraints:
- 1 <= number of operations <= 100
- 0 <= value pushed <= 10^9

Example:
push(1), push(2), peek() -> returns 1, pop() -> returns 1, empty() -> returns False
"""


class MyQueue:
    def __init__(self):
        pass
    def push(self, x: int) -> None:
        pass
    def pop(self) -> int:
        pass
    def peek(self) -> int:
        pass
    def empty(self) -> bool:
        pass


if __name__ == "__main__":
    q = MyQueue()
    q.push(1)
    q.push(2)
    assert q.peek() == 1
    assert q.pop() == 1
    assert not q.empty()
    assert q.pop() == 2
    assert q.empty()
    q.push(5)
    assert q.pop() == 5
    q.push(10)
    q.push(11)
    assert q.pop() == 10
    assert q.peek() == 11
    assert not q.empty()
    print("All tests passed.")