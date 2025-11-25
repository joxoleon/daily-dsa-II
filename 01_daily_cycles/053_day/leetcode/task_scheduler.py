# [ Name: Task Scheduler ]  [ Category: heap ]  [ Topic: heap ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/task-scheduler/ ]

"""
Given a list of CPU tasks represented by uppercase letters and a non-negative cooling interval n,
return the least number of units of time that the CPU will take to finish all tasks.
The CPU must wait n intervals before repeating the same task.
Constraints: 1 <= tasks.length <= 10^4; 0 <= n <= 100.
Example: tasks = ["A","A","A","B","B","B"], n = 2 → Output: 8
"""

from typing import List

def leastInterval(tasks: List[str], n: int) -> int:
    pass

if __name__ == "__main__":
    assert leastInterval(["A","A","A","B","B","B"], 2) == 8
    assert leastInterval(["A","A","A","B","B","B"], 0) == 6
    assert leastInterval(["A","A","A","A","B","B","C","C"], 2) == 10
    assert leastInterval(["A","B","C","D","E","F"], 2) == 6
    assert leastInterval(["A","A","A","B","B","B"], 1) == 6
    assert leastInterval(["A","A","A","B","B","B"], 3) == 10
    assert leastInterval(["A"], 0) == 1
    assert leastInterval(["A","B","A"], 3) == 4