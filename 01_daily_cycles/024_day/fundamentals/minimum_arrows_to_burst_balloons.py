# [ Name: Minimum Arrows to Burst Balloons ]  [ Category: intervals ]  [ Topic: overlap_greedy ]  [ Weight: 6 ]

"""
Problem Description:
Given a list of intervals where each interval represents a balloon with horizontal diameter starting and ending at points[i][0] and points[i][1], find the minimum number of arrows required to burst all balloons. 
An arrow can be shot vertically at any position and bursts all balloons that intersect that position. 
Return the minimum number of arrows needed.

Constraints:
- Input: List[List[int]] with 0 <= len(points) <= 10^5, -10^9 <= points[i][0] <= points[i][1] <= 10^9
- Output: Integer (minimum arrows needed)
- If no balloons, return 0.

Example:
Input: [[1,6],[2,8],[7,12],[10,16]] -> Output: 2
"""

from typing import List

def find_min_arrow_shots(points: List[List[int]]) -> int:
    pass

if __name__ == "__main__":
    assert find_min_arrow_shots([[1,6],[2,8],[7,12],[10,16]]) == 2
    assert find_min_arrow_shots([[1,2],[3,4],[5,6],[7,8]]) == 4
    assert find_min_arrow_shots([[1,2],[2,3],[3,4],[4,5]]) == 2
    assert find_min_arrow_shots([]) == 0
    assert find_min_arrow_shots([[1,2]]) == 1
    assert find_min_arrow_shots([[1,10],[2,6],[7,12],[11,16]]) == 2
    assert find_min_arrow_shots([[1,5],[1,5],[1,5]]) == 1
    assert find_min_arrow_shots([[1,2],[2,3],[4,5],[6,7],[8,9]]) == 4

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
