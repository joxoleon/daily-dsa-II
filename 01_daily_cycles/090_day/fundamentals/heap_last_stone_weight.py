# [ Name: Heap — Last Stone Weight ]  [ Category: heaps ]  [ Topic: max_heap ]  [ Weight: 6 ]

"""
Problem Description:
You are given a list of integers representing the weights of stones.
Each turn, smash the two heaviest stones together: if they are the same, both are destroyed; if not, the heavier reduces by the lighter and the lighter is destroyed.
Continue until at most one stone remains.
Return the weight of the last stone left, or 0 if no stones remain.

Constraints:
- 1 <= len(stones) <= 30
- Each stone's weight: 1 <= stones[i] <= 1000

Example:
Input: [2,7,4,1,8,1] -> Output: 1
"""

from typing import List

def last_stone_weight(stones: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert last_stone_weight([2, 7, 4, 1, 8, 1]) == 1
    assert last_stone_weight([1, 1]) == 0
    assert last_stone_weight([1]) == 1
    assert last_stone_weight([10, 4, 2, 10]) == 2
    assert last_stone_weight([3, 7, 2]) == 2
    assert last_stone_weight([5, 5, 5, 5]) == 0
    assert last_stone_weight([31, 26, 33, 21, 40]) == 5
    assert last_stone_weight([9, 3, 2, 10]) == 0

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
