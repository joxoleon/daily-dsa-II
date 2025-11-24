# [ Name: Top K Frequent Elements ]  [ Category: hashing ]  [ Topic: hashing ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/top-k-frequent-elements/ ]

"""
Given an integer array nums and an integer k, return the k most frequent elements.
You may return the answer in any order.
1 <= nums.length <= 10^5, 1 <= k <= the number of unique elements in nums
Elements in nums are integers in the range [-10^4, 10^4].
Example: nums = [1,1,1,2,2,3], k = 2 => Output: [1,2]
"""

from typing import List

def topKFrequent(nums: List[int], k: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert set(topKFrequent([1,1,1,2,2,3], 2)) == set([1,2])
    assert set(topKFrequent([1], 1)) == set([1])
    assert set(topKFrequent([4,4,4,5,5,6], 2)) == set([4,5])
    assert set(topKFrequent([1,2,2,3,3,3], 1)) == set([3])
    assert set(topKFrequent([5,6,5,7,8,6,8,8], 3)) == set([5,6,8])
    assert set(topKFrequent([-1,-1,-2,-2,-2,-3], 2)) == set([-1,-2])
    assert set(topKFrequent([0,0,0,0], 1)) == set([0])
    assert set(topKFrequent([99,2,99,3,2,3,3], 1)) == set([3])
