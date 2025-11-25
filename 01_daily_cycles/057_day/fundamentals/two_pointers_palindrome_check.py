# [ Name: Two Pointers — Palindrome Check ]  [ Category: arrays ]  [ Topic: two_pointers ]  [ Weight: 8 ]

"""
Problem Description:
Given a list of integers, check if the list is a palindrome.
A palindrome reads the same forward and backward.
Return True if the input list is a palindrome, else return False.

Constraints:
- Input: List[int], length from 0 up to 10^5
- An empty list is considered a palindrome.

Example:
Input: [2, 4, 4, 2] -> Output: True
"""

from typing import List

def is_palindrome(nums: List[int]) -> bool:
    pass

if __name__ == "__main__":
    assert is_palindrome([1, 2, 2, 1]) == True
    assert is_palindrome([1, 2, 3, 4]) == False
    assert is_palindrome([]) == True
    assert is_palindrome([7]) == True
    assert is_palindrome([3, 4, 5, 4, 3]) == True
    assert is_palindrome([0, 0, 1, 0]) == False
    assert is_palindrome([5, 5, 5, 5]) == True
    assert is_palindrome([9, 2, 9, 9]) == False

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
