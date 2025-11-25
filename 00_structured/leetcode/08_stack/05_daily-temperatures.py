# [ Name: Daily Temperatures ]  [ Category: stack ]  [ Topic: stack ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/daily-temperatures/ ]

"""
Given a list of daily temperatures, return a list where for each day, the value is how many days you would have to wait until a warmer temperature. 
If there is no future day for which this is possible, put 0 instead.
Constraints:
- 1 <= len(temperatures) <= 10^5
- 30 <= temperatures[i] <= 100
Example: Input: [73,74,75,71,69,72,76,73] Output: [1,1,4,2,1,1,0,0]
"""

from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    pass

if __name__ == "__main__":
    assert dailyTemperatures([73,74,75,71,69,72,76,73]) == [1,1,4,2,1,1,0,0]
    assert dailyTemperatures([30,40,50,60]) == [1,1,1,0]
    assert dailyTemperatures([30,60,90]) == [1,1,0]
    assert dailyTemperatures([90,80,70,60]) == [0,0,0,0]
    assert dailyTemperatures([70]) == [0]
    assert dailyTemperatures([70,71,70,69,72]) == [1,3,2,1,0]
    assert dailyTemperatures([80,80,80,80]) == [0,0,0,0]
    assert dailyTemperatures([65,68,62,70,75,64,63,76]) == [1,2,1,1,3,1,1,0]
