# [ Name: Sliding Window Maximum ]  [ Category: sliding_window ]  [ Topic: sliding_window ]  [ Weight: 9 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/sliding-window-maximum/ ]

"""
Given an array of integers nums and an integer k, return the maximum value in each sliding window of size k.
Return the result as a list of integers.
Constraints: 1 <= nums.length <= 10^5, -10^9 <= nums[i] <= 10^9, 1 <= k <= nums.length.
Example: Input: nums = [1,3,-1,-3,5,3,6,7], k = 3; Output: [3,3,5,5,6,7]
"""

from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    pass

if __name__ == "__main__":
    assert maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]
    assert maxSlidingWindow([1], 1) == [1]
    assert maxSlidingWindow([9, 8, 7, 6, 5], 2) == [9,8,7,6]
    assert maxSlidingWindow([4,2,12,3,8,0,2], 4) == [12,12,12,8]
    assert maxSlidingWindow([7,2,4], 2) == [7,4]
    assert maxSlidingWindow([1,2,3,4,5,6], 3) == [3,4,5,6]
    assert maxSlidingWindow([100,200,-300,400], 2) == [200,200,400]
    assert maxSlidingWindow([1,-1], 1) == [1,-1]
