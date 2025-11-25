# [ Name: Heap — Priority Scheduling ]  [ Category: heaps ]  [ Topic: priority_queue ]  [ Weight: 7 ]

"""
Problem Description:
Given a list of integer task priorities, return the order in which the tasks will be executed using a max-priority queue (highest priority first).
If two tasks share the same priority, execute the one with the lower original index first.
Return a list of indices representing the execution order.

Constraints:
- 1 <= len(tasks) <= 10^5
- Priorities are integers (can be negative or zero).
- Output should contain all indices from 0 to len(tasks) - 1 in scheduling order.

Example:
Input: [4, 1, 3] → Output: [0, 2, 1]
"""

from typing import List

def schedule_tasks(tasks: List[int]) -> List[int]:
    pass

if __name__ == "__main__":
    assert schedule_tasks([4, 1, 3]) == [0, 2, 1]
    assert schedule_tasks([1, 2, 3]) == [2, 1, 0]
    assert schedule_tasks([9]) == [0]
    assert schedule_tasks([-1, -2, -3]) == [0, 1, 2]
    assert schedule_tasks([5, 5, 1]) == [0, 1, 2]
    assert schedule_tasks([5, 5, 5]) == [0, 1, 2]
    assert schedule_tasks([0, 3, 2, 3]) == [1, 3, 2, 0]
    assert schedule_tasks([10, -1, 10, 0]) == [0, 2, 3, 1]

    print("All tests passed.")
