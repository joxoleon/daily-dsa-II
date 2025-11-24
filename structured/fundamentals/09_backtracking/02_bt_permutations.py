# [ Name: Backtracking — Permutations ]  [ Category: backtracking ]  [ Topic: permutations ]  [ Weight: 7 ]

"""
Problem Description:
Given a list of distinct integers, return all possible permutations.
Each permutation must contain every integer exactly once and can be in any order.
Return the result as a list of lists, with each inner list representing a valid permutation.

Constraints:
- 1 <= len(nums) <= 6
- Each integer in nums is unique.

Example:
Input: [1, 2, 3] -> Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
"""

from typing import List

def permutations(nums: List[int]) -> List[List[int]]:
    pass


if __name__ == "__main__":
    assert sorted(permutations([1])) == [[1]]
    assert sorted(permutations([1,2])) == sorted([[1,2],[2,1]])
    assert len(permutations([1,2,3])) == 6
    assert all(sorted(p) == sorted([1,2,3]) for p in permutations([1,2,3]))
    assert sorted(permutations([0, 1])) == sorted([[0,1],[1,0]])
    assert len(permutations([4, 5, 6, 7])) == 24
    assert [1,3,2] in permutations([1,2,3])
    assert all(len(p) == 4 for p in permutations([9,8,7,6]))
    print("All tests passed.")
