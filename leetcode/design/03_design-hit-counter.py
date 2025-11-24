# [ Name: Design Hit Counter ]  [ Category: design ]  [ Topic: design ]  [ Weight: 6 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/design-hit-counter/ ]

"""
Design a hit counter that counts the number of hits received in the past 5 minutes (300 seconds). 
Implement two methods: hit(timestamp) records a hit at a given timestamp, and getHits(timestamp) returns the number of hits in the past 5 minutes including the current timestamp.
Timestamps are in seconds and come in monotonically increasing order.
1 <= timestamp <= 2*10^9.
Example: After 3 hits at timestamps 1, 2, 3, and getHits(4) returns 3.
"""

from typing import List

class HitCounter:
    def __init__(self):
        pass
    def hit(self, timestamp: int) -> None:
        pass
    def getHits(self, timestamp: int) -> int:
        pass

if __name__ == "__main__":
    hc = HitCounter()
    hc.hit(1)
    hc.hit(2)
    hc.hit(3)
    assert hc.getHits(4) == 3
    hc.hit(300)
    assert hc.getHits(300) == 4
    assert hc.getHits(301) == 3
    hc2 = HitCounter()
    hc2.hit(100)
    hc2.hit(200)
    hc2.hit(300)
    assert hc2.getHits(300) == 3
    assert hc2.getHits(399) == 3
    assert hc2.getHits(400) == 2
    hc2.hit(401)
    assert hc2.getHits(401) == 3