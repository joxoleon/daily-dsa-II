# [ Name: Best Time to Buy and Sell Stock ]  [ Category: arrays ]  [ Topic: arrays ]  [ Weight: 9 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ ]

"""
Given an array of prices where prices[i] is the price of a stock on day i, return the maximum profit you can achieve from a single buy and sell. You must buy before you sell. If no profit is possible, return 0.
Constraints: 1 <= prices.length <= 10^5, 0 <= prices[i] <= 10^4.
Example: Input: prices = [7,1,5,3,6,4] Output: 5 (Buy at 1, sell at 6).
"""

from typing import List

def maxProfit(prices: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert maxProfit([7,1,5,3,6,4]) == 5
    assert maxProfit([7,6,4,3,1]) == 0
    assert maxProfit([2,4,1]) == 2
    assert maxProfit([1,2]) == 1
    assert maxProfit([2,1,2,1,0,1,2]) == 2
    assert maxProfit([1]) == 0
    assert maxProfit([3,2,6,5,0,3]) == 4
    assert maxProfit([1,4,2,7]) == 6