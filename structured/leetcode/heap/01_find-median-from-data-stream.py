# [ Name: Find Median from Data Stream ]  [ Category: heap ]  [ Topic: heap ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/find-median-from-data-stream/ ]

"""
Design a data structure that supports adding integers from a stream and retrieving the median element at any time.
Implement the following methods:
- addNum(int num): Adds a number to the data structure.
- findMedian(): Returns the median of all elements so far.
Assume at least one operation will be performed.
Example: ["MedianFinder","addNum","addNum","findMedian","addNum","findMedian"] [[],[1],[2],[],[3],[]] outputs [null,null,null,1.5,null,2.0]
"""

import heapq
from typing import List, Optional

class MedianFinder:
    def __init__(self):
        pass

    def addNum(self, num: int) -> None:
        pass

    def findMedian(self) -> float:
        pass

if __name__ == "__main__":
    mf = MedianFinder()
    mf.addNum(1)
    mf.addNum(2)
    assert mf.findMedian() == 1.5
    mf.addNum(3)
    assert mf.findMedian() == 2.0
    mf = MedianFinder()
    for n in [5,3,8,9,1,7]:
        mf.addNum(n)
    assert mf.findMedian() == 6.0
    mf = MedianFinder()
    mf.addNum(-1)
    assert mf.findMedian() == -1.0
    mf.addNum(-2)
    assert mf.findMedian() == -1.5
    mf.addNum(-3)
    assert mf.findMedian() == -2.0
    mf = MedianFinder()
    for n in [2,5,10,100,3]:
        mf.addNum(n)
    assert mf.findMedian() == 5.0
    mf = MedianFinder()
    for n in [1,2]:
        mf.addNum(n)
    assert abs(mf.findMedian() - 1.5) < 1e-9
    mf.addNum(3)
    assert abs(mf.findMedian() - 2.0) < 1e-9