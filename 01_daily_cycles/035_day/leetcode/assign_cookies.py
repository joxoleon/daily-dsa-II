# [ Name: Assign Cookies ]  [ Category: greedy ]  [ Topic: greedy ]  [ Weight: 5 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/assign-cookies/ ]

"""
Given two integer arrays g and s representing the greed factor of each child and the sizes of cookies, assign cookies so that as many children as possible are content. Each child i is content if they are given a cookie of size >= g[i]. Each cookie can be given to at most one child.
Return the maximum number of content children.
Constraints: 1 <= g.length, s.length <= 3 * 10^4, 1 <= g[i], s[i] <= 2^31 - 1.
Example: Input: g = [1,2,3], s = [1,1] -> Output: 1
"""

from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        pass

if __name__ == "__main__":
    sol = Solution()
    assert sol.findContentChildren([1,2,3],[1,1]) == 1
    assert sol.findContentChildren([1,2],[1,2,3]) == 2
    assert sol.findContentChildren([10,9,8,7],[5,6,7,8]) == 2
    assert sol.findContentChildren([1,2,3],[3]) == 1
    assert sol.findContentChildren([1,2,3],[1,2,3]) == 3
    assert sol.findContentChildren([2,3,4],[1,1,1]) == 0
    assert sol.findContentChildren([1,2,3,4],[2,2,2,2]) == 2
    assert sol.findContentChildren([],[]) == 0