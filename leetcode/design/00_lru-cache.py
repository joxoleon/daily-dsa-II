# [ Name: LRU Cache ]  [ Category: design ]  [ Topic: design ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/lru-cache/ ]

"""
Design a Least Recently Used (LRU) cache that supports getting and setting key-value pairs in constant time.
The cache has a positive capacity and evicts the least recently used item when capacity is exceeded.
Implement the LRUCache class with these methods:
- LRUCache(int capacity): initializes the cache.
- get(int key): returns the value if present, else -1.
- put(int key, int value): inserts or updates the key.
Example: LRUCache(2); put(1,1); put(2,2); get(1) returns 1; put(3,3); get(2) returns -1.
Constraints: All keys and values are integers; 0 <= number of calls <= 3000; 0 <= key, value <= 10^4
"""

from typing import Optional

class LRUCache:
    def __init__(self, capacity: int):
        pass

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, value: int) -> None:
        pass

if __name__ == "__main__":
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4
    cache = LRUCache(1)
    cache.put(10, 5)
    assert cache.get(10) == 5
    cache.put(20, 6)
    assert cache.get(10) == -1
    assert cache.get(20) == 6
    cache = LRUCache(0)
    cache.put(5, 5)
    assert cache.get(5) == -1