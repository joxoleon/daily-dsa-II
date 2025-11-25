# [ Name: Sliding Window — Fruit into Baskets ]  [ Category: arrays ]  [ Topic: sliding_window_k_distinct ]  [ Weight: 6 ]

"""
Problem Description:
You are given a list of integers representing fruit types in a row of trees.
Return the length of the longest subarray containing at most 2 distinct types of fruit.
Each tree produces exactly one type of fruit.
If there are fewer than 2 types, take as many as possible.

Constraints:
- 1 <= len(nums) <= 10^5
- 0 <= nums[i] <= 10^4

Example:
Input: [1,2,1,2,3] -> Output: 4
"""

from typing import List

def total_fruit(nums: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert total_fruit([1,2,1,2,3]) == 4
    assert total_fruit([1,2,3,2,2]) == 4
    assert total_fruit([0,1,2,2]) == 3
    assert total_fruit([1]) == 1
    assert total_fruit([1,1,1,1]) == 4
    assert total_fruit([1,2,3,4,5]) == 2
    assert total_fruit([0,1,2,2,3,3,1,1,2]) == 5
    assert total_fruit([2,2,3,3,2,2,1,1,1,1]) == 6

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
