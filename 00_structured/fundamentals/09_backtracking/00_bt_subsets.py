# [ Name: Backtracking — Generate Subsets ]  [ Category: backtracking ]  [ Topic: subsets ]  [ Weight: 7 ]

"""
Problem Description:
Given a list of distinct integers, return all possible subsets (the power set).
The solution set must not contain duplicate subsets, and elements within a subset should be in the same order as in the input.
Return a list of lists of integers representing all subsets.
If the input list is empty, return a list containing only the empty subset.

Constraints:
- 0 <= len(nums) <= 10
- All elements are unique.

Example:
Input: [1,2] -> Output: [[], [1], [2], [1,2]]
"""

from typing import List

def subsets(nums: List[int]) -> List[List[int]]:
    pass

if __name__ == "__main__":
    assert sorted([sorted(s) for s in subsets([])]) == sorted([[]])
    assert sorted([sorted(s) for s in subsets([1])]) == sorted([[], [1]])
    assert sorted([sorted(s) for s in subsets([1,2])]) == sorted([[], [1], [2], [1,2]])
    assert sorted([sorted(s) for s in subsets([0,1])]) == sorted([[], [0], [1], [0,1]])
    assert sorted([sorted(s) for s in subsets([1,2,3])]) == sorted([[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]])
    assert sorted([sorted(s) for s in subsets([4,5,6])]) == sorted([[], [4], [5], [6], [4,5], [4,6], [5,6], [4,5,6]])
    assert sorted([sorted(s) for s in subsets([7,8,9,10])]) == sorted([
        [], [7], [8], [9], [10],
        [7,8], [7,9], [7,10], [8,9], [8,10], [9,10],
        [7,8,9], [7,8,10], [7,9,10], [8,9,10],
        [7,8,9,10]
    ])
    assert sorted([sorted(s) for s in subsets([100, 200])]) == sorted([[], [100], [200], [100,200]])

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
