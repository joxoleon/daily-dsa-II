# [ Name: Hand of Straights ]  [ Category: greedy ]  [ Topic: greedy ]  [ Weight: 7 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/hand-of-straights/ ]

"""
Given an array hand of integers representing cards, and an integer groupSize, determine if it is possible to rearrange the cards into groups of groupSize consecutive cards.
Return True if it is possible, else return False.
1 <= hand.length <= 10^4, 1 <= groupSize <= hand.length
Each card is an integer in the range [0, 10^9].
Example: hand = [1,2,3,6,2,3,4,7,8], groupSize = 3 -> True
"""

from typing import List

def isNStraightHand(hand: List[int], groupSize: int) -> bool:
    pass

if __name__ == "__main__":
    assert isNStraightHand([1,2,3,6,2,3,4,7,8], 3) == True
    assert isNStraightHand([1,2,3,4,5], 4) == False
    assert isNStraightHand([1,2,3,4,5,6], 3) == True
    assert isNStraightHand([8,10,12], 3) == False
    assert isNStraightHand([1,1,2,2,3,3], 3) == True
    assert isNStraightHand([1], 1) == True
    assert isNStraightHand([3,3,2,2,1,1], 3) == True
    assert isNStraightHand([1,2,3,4], 2) == True
