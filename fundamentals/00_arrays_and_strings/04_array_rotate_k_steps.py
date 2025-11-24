# [ Name: Rotate Array by K Steps ]  [ Category: arrays ]  [ Topic: rotation ]  [ Weight: 7 ]

"""
Problem Description:
Given a list of integers, rotate the array to the right by k steps.
Return the rotated list as the result.
If k is 0 or the array is empty, return the original list.
k may be greater than the length of the array.
All input elements can be positive, negative, or zero.

Constraints:
- 0 <= len(nums) <= 10^5
- 0 <= k <= 10^9

Example:
Input: nums = [1,2,3,4,5], k = 2 -> Output: [4,5,1,2,3]
"""

from typing import List

def rotate(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if n == 0 or k % n == 0:
        return nums
    k %= n
    
    def rev(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1
    
    # Reverse the entire array
    rev(nums, 0, n - 1)
    # Reverse the first k elements
    rev(nums, 0, k - 1)
    # Reverse elements after k
    rev(nums, k, n - 1)
    return nums

if __name__ == "__main__":
    assert rotate([1,2,3,4,5], 2) == [4,5,1,2,3]
    assert rotate([1,2,3], 4) == [3,1,2]
    assert rotate([], 5) == []
    assert rotate([10,20,30], 0) == [10,20,30]
    assert rotate([1], 100) == [1]
    assert rotate([-1,-2,-3,0,1], 3) == [-3,0,1,-1,-2]
    assert rotate([5,6,7,8], 8) == [5,6,7,8]
    assert rotate([1,2], 3) == [2,1]
    print("All tests passed.")
