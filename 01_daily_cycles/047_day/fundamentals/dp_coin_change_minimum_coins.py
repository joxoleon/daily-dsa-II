# [ Name: DP — Coin Change (Minimum Coins) ]  [ Category: dp ]  [ Topic: 1d_dp ]  [ Weight: 8 ]

"""
Problem Description:
You are given a list of coin denominations and an integer amount.
Return the minimum number of coins needed to make up that amount.
If it is not possible to make the amount with the given coins, return -1.

Constraints:
- 1 <= len(coins) <= 12
- 1 <= coins[i] <= 2*10^4
- 0 <= amount <= 10^4

Example:
Input: coins = [1,2,5], amount = 11 -> Output: 3  (11 = 5 + 5 + 1)
"""

from typing import List

def coin_change(coins: List[int], amount: int) -> int:
    pass

if __name__ == "__main__":
    assert coin_change([1,2,5], 11) == 3
    assert coin_change([2], 3) == -1
    assert coin_change([1], 0) == 0
    assert coin_change([1], 2) == 2
    assert coin_change([5,10,25], 30) == 2
    assert coin_change([2,4,6], 7) == -1
    assert coin_change([1,3,4], 6) == 2
    assert coin_change([7,14], 49) == 4
    print("All tests passed.")
