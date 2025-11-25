# [ Name: Difference Array — Efficient Range Updates ]  [ Category: arrays ]  [ Topic: difference_array ]  [ Weight: 5 ]

"""
Problem Description:
Given an integer n and a list of updates, apply each update to an initially zero array of size n.
Each update is a list [start, end, inc] and means to increment every element nums[i] for start <= i <= end by inc.
Return the final modified array after applying all updates.

Constraints:
- 1 <= n <= 10^5
- 0 <= start <= end < n
- -10^4 <= inc <= 10^4
- 0 <= number of updates <= 10^5

Example:
Input: n = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]] -> Output: [-2,0,3,5,3]
"""

from typing import List

def apply_range_updates(n: int, updates: List[List[int]]) -> List[int]:
    pass

if __name__ == "__main__":
    assert apply_range_updates(5, [[1,3,2],[2,4,3],[0,2,-2]]) == [-2,0,3,5,3]
    assert apply_range_updates(3, [[0,2,3]]) == [3,3,3]
    assert apply_range_updates(4, []) == [0,0,0,0]
    assert apply_range_updates(6, [[0,5,1]]) == [1,1,1,1,1,1]
    assert apply_range_updates(2, [[0,1,5],[0,0,-3]]) == [2,5]
    assert apply_range_updates(7, [[2,4,100],[0,3,-50]]) == [-50,-50,50,50,100,0,0]
    assert apply_range_updates(1, [[0,0,7]]) == [7]
    assert apply_range_updates(10, [[3,7,2],[2,5,-1],[0,9,1]]) == [1,1,0,2,2,2,3,3,1,1]
    print("All tests passed.")
