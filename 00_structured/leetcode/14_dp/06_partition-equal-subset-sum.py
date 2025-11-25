# [ Name: Partition Equal Subset Sum ]  [ Category: dp ]  [ Topic: dp ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/partition-equal-subset-sum/ ]

"""
Given a list of positive integers nums, determine if it can be partitioned into two subsets so that the sum of elements in both subsets is equal.
Return True if such a partition exists, otherwise False.
Constraints: 1 <= len(nums) <= 200, 1 <= nums[i] <= 100.
Example: 
Input: nums = [1,5,11,5]
Output: True
"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        pass

if __name__ == "__main__":
    sol = Solution()
    assert sol.canPartition([1,5,11,5]) == True
    assert sol.canPartition([1,2,3,5]) == False
    assert sol.canPartition([2,2,3,5]) == False
    assert sol.canPartition([1,1]) == True
    assert sol.canPartition([1]) == False
    assert sol.canPartition([100,100]) == True
    assert sol.canPartition([23,13,11,7,6,5,5]) == True
    assert sol.canPartition([3,3,3,4,5]) == True