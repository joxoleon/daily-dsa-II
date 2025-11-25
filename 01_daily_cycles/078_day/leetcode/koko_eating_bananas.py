# [ Name: Koko Eating Bananas ]  [ Category: binary_search ]  [ Topic: binary_search ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/koko-eating-bananas/ ]

"""
Find the minimum integer speed K such that Koko can eat all the bananas in all piles within H hours.
Input: a list of integers piles, integer H.
Output: integer K (minimum eating speed).
Constraints: 1 <= piles.length <= 10^4, 1 <= piles[i] <= 10^9, piles and H are positive integers.
Example: Input: piles = [3,6,7,11], H = 8 -> Output: 4
"""

from typing import List

def minEatingSpeed(piles: List[int], H: int) -> int:
    pass

if __name__ == "__main__":
    assert minEatingSpeed([3,6,7,11], 8) == 4
    assert minEatingSpeed([30,11,23,4,20], 5) == 30
    assert minEatingSpeed([30,11,23,4,20], 6) == 23
    assert minEatingSpeed([1], 1) == 1
    assert minEatingSpeed([1000000000], 2) == 500000000
    assert minEatingSpeed([312884470], 968709470) == 1
    assert minEatingSpeed([805306368,805306368,805306368], 1000000000) == 3
    assert minEatingSpeed([6,7,11,29,33,44,58,99,100,111,123,144,198,200,210,304,501,700], 30) == 22