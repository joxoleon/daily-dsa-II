# [ Name: Deque — Sliding Window Maximum ]  [ Category: stacks_and_queues ]  [ Topic: deque ]  [ Weight: 8 ]

"""
Problem Description:
Given a list of integers and an integer k, return a list of the maximum value in each sliding window of size k as it moves from left to right.
The window moves one position at a time.
Return an empty list if k is 0 or nums is empty.

Constraints:
- 1 <= len(nums) <= 10^5
- 1 <= k <= len(nums)
- k > 0

Example:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3 -> Output: [3,3,5,5,6,7]
"""

from typing import List

def sliding_window_max(nums: List[int], k: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert sliding_window_max([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert sliding_window_max([1], 1) == [1]
    assert sliding_window_max([9, 11], 2) == [11]
    assert sliding_window_max([4,2,12,3,8,7], 4) == [12,12,12]
    assert sliding_window_max([7,2,4], 2) == [7,4]
    assert sliding_window_max([5,5,5,5], 2) == [5,5,5]
    assert sliding_window_max([1,3,1,2,0,5], 3) == [3,3,2,5]
    assert sliding_window_max([1,2,3,4,5], 1) == [1,2,3,4,5]

    print("All tests passed.")
