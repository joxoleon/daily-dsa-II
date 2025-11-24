# [ Name: Coin Change ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/coin-change/ ]

"""
Given an integer array coins representing denominations and an integer amount,
return the fewest number of coins needed to make up the amount, or -1 if not possible.
Input: coins: List[int], amount: int. Output: int.
Constraints: 1 <= coins.length <= 12, 1 <= coins[i] <= 2*10^4, 0 <= amount <= 10^4.
Example: Input: coins = [1,2,5], amount = 11; Output: 3 (11 = 5 + 5 + 1)
"""

from typing import List

def coinChange(coins: List[int], amount: int) -> int:
    pass

if __name__ == "__main__":
    assert coinChange([1,2,5], 11) == 3
    assert coinChange([2], 3) == -1
    assert coinChange([1], 0) == 0
    assert coinChange([1], 2) == 2
    assert coinChange([2,5,10,1], 27) == 4
    assert coinChange([186,419,83,408], 6249) == 20
    assert coinChange([2], 0) == 0
    assert coinChange([3,7,405,436], 8839) == 25