# [ Name: Monotonic Stack — Largest Rectangle in Histogram ]  [ Category: stacks_and_queues ]  [ Topic: monotonic_stack ]  [ Weight: 9 ]

"""
Problem Description:
Given a list of non-negative integers representing the heights of adjacent bars in a histogram, find the area of the largest rectangle that can be formed in the histogram.
Return the area as an integer.
Constraints:
- 1 <= len(heights) <= 10^5
- 0 <= heights[i] <= 10^4

Example:
Input: [2,1,5,6,2,3] -> Output: 10
"""

from typing import List

def largest_rectangle(heights: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert largest_rectangle([2,1,5,6,2,3]) == 10
    assert largest_rectangle([2,4]) == 4
    assert largest_rectangle([0,2,0]) == 2
    assert largest_rectangle([1]) == 1
    assert largest_rectangle([1,2,3,4,5]) == 9
    assert largest_rectangle([5,4,3,2,1]) == 9
    assert largest_rectangle([2,1,2]) == 3
    assert largest_rectangle([0,0,0,0]) == 0

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
