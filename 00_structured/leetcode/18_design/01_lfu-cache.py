# [ Name: LFU Cache ]  [ Category: design ]  [ Topic: design ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/lfu-cache/ ]

"""
Design and implement a data structure for Least Frequently Used (LFU) cache with the following operations: get(key) and put(key, value).
The cache should remove the least frequently used key if the capacity is reached before inserting a new key.
Both operations must be provided in O(1) average time complexity.
Capacity will be a positive integer.
Example: 
Input: ["LFUCache","put","put","get","put","get","get","put","get","get","get"], [[2], [1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]
Output: [null,null,null,1,null,-1,3,null,-1,3,4]
"""

from typing import Optional

class LFUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass

if __name__ == "__main__":
    cache = LFUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    assert cache.get(3) == 3
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    cache2 = LFUCache(0)
    cache2.put(0, 0)
    assert cache2.get(0) == -1