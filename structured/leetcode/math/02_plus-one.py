# [ Name: Plus One ]  [ Category: math ]  [ Topic: math ]  [ Weight: 5 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/plus-one/ ]

"""
Given a non-empty array of decimal digits representing a non-negative integer, increment one to the integer.
The digits are stored so that the most significant digit is at the head of the list.
Input: List[int] digits
Output: List[int] after incrementing by one
1 <= len(digits) <= 100
Each element in digits is between 0 and 9.
Example: Input: digits = [1,2,3], Output: [1,2,4]
"""

from typing import List

def plusOne(digits: List[int]) -> List[int]:
    pass

if __name__ == "__main__":
    assert plusOne([1,2,3]) == [1,2,4]
    assert plusOne([4,3,2,1]) == [4,3,2,2]
    assert plusOne([0]) == [1]
    assert plusOne([9]) == [1,0]
    assert plusOne([9,9,9]) == [1,0,0,0]
    assert plusOne([2,9,9]) == [3,0,0]
    assert plusOne([6,7,9]) == [6,8,0]
    assert plusOne([8,9,9,9]) == [9,0,0,0]