# [ Name: Backtracking — Subsets With Duplicates ]  [ Category: backtracking ]  [ Topic: subsets ]  [ Weight: 8 ]

"""
Problem Description:
Given a list of integers that may contain duplicates, return all possible subsets (the power set).
The solution must not contain duplicate subsets; each subset should be unique.
Return the collection of subsets as a list of lists.

Constraints:
- 0 <= len(nums) <= 10
- Each integer in nums may appear more than once.
- Subsets can be returned in any order.

Example:
Input: [1,2,2] -> Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
"""

from typing import List

def subsets_with_dup(nums: List[int]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted([sorted(s) for s in subsets_with_dup([1,2,2])]) == sorted([[], [1], [1,2], [1,2,2], [2], [2,2]])
    assert sorted([sorted(s) for s in subsets_with_dup([])]) == sorted([[]])
    assert sorted([sorted(s) for s in subsets_with_dup([1])]) == sorted([[], [1]])
    assert sorted([sorted(s) for s in subsets_with_dup([2,2,2])]) == sorted([[], [2], [2,2], [2,2,2]])
    assert sorted([sorted(s) for s in subsets_with_dup([4,4,4,1,4])]) == sorted([[], [1], [4], [4,4], [4,4,4], [1,4], [1,4,4], [1,4,4,4], [4,4,4,4], [1,4,4,4,4]])
    assert sorted([sorted(s) for s in subsets_with_dup([0,1,2])]) == sorted([[], [0], [1], [2], [0,1], [0,2], [1,2], [0,1,2]])
    assert sorted([sorted(s) for s in subsets_with_dup([1,2,3,3])]) == sorted([[], [1], [2], [3], [1,2], [1,3], [2,3], [3,3], [1,2,3], [1,3,3], [2,3,3], [1,2,3,3]])
    assert sorted([sorted(s) for s in subsets_with_dup([9,7,7,9])]) == sorted([[], [7], [9], [7,7], [7,9], [9,9], [7,7,9], [7,9,9], [7,7,9,9]])

    print("All tests passed.")
