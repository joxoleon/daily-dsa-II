# [ Name: Russian Doll Envelopes ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 9 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/russian-doll-envelopes/ ]

"""
Given a list of envelopes represented as pairs of integers [width, height], return the maximum number of envelopes you can Russian doll (put one inside another). Each envelope can fit into another if both width and height are strictly less. Input: envelopes as List[List[int]]. Output: int. Constraints: 1 <= len(envelopes) <= 10^5, 1 <= width, height <= 10^5. Example: Input: [[5,4],[6,4],[6,7],[2,3]] Output: 3.
"""

from typing import List

def maxEnvelopes(envelopes: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]) == 3
    assert maxEnvelopes([[1,1]]) == 1
    assert maxEnvelopes([[1,1],[1,1],[1,1]]) == 1
    assert maxEnvelopes([[4,5],[4,6],[6,7],[2,3],[1,1]]) == 4
    assert maxEnvelopes([[2,100],[3,200],[4,300],[5,500],[5,400],[5,250],[6,370],[6,360],[7,380]]) == 5
    assert maxEnvelopes([]) == 0
    assert maxEnvelopes([[5,4],[6,4],[6,7],[2,3],[7,8],[8,9]]) == 5
    assert maxEnvelopes([[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]) == 3