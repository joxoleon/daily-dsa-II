# [ Name: Gas Station ]  [ Category: greedy ]  [ Topic: greedy ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/gas-station/ ]

"""
Given two integer arrays gas and cost representing gas at each station and the gas required to travel to the next, find the starting gas station index to complete the circuit once. Return -1 if impossible.
Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Constraints: 1 <= gas.length <= 10^5, 0 <= gas[i], cost[i] <= 10^4. Only one solution exists if possible.
"""

from typing import List

def canCompleteCircuit(gas: List[int], cost: List[int]) -> int:
    pass

if __name__ == "__main__":
    assert canCompleteCircuit([1,2,3,4,5],[3,4,5,1,2]) == 3
    assert canCompleteCircuit([2,3,4],[3,4,3]) == -1
    assert canCompleteCircuit([5,1,2,3,4],[4,4,1,5,1]) == 4
    assert canCompleteCircuit([2,0,2,2,2],[1,1,1,1,1]) == 0
    assert canCompleteCircuit([3,3,4],[3,4,4]) == -1
    assert canCompleteCircuit([0,0,0],[0,0,0]) == 0
    assert canCompleteCircuit([2,3,4,5,6,7,8,9,10],[3,4,5,6,7,8,9,10,2]) == 8
    assert canCompleteCircuit([4,5,2,6,5,3],[3,2,7,3,2,9]) == 3