# [ Name: Binary Search — Binary Search on Answer ]  [ Category: binary_search ]  [ Topic: binary_search_answer_space ]  [ Weight: 5 ]

"""
Problem Description:
Given a monotonic predicate function and a search range [lo, hi], return the minimal integer x in [lo, hi] such that predicate(x) is True.
If predicate(x) is False for all x, return hi + 1.
Constraints:
- lo and hi are integers, lo <= hi
- predicate(x) returns a boolean and is monotonic: once True, always True for increasing x
Example:
If predicate(x) == (x >= 5), lo = 1, hi = 10, output is 5.
"""

def binary_search_answer(lo: int, hi: int, predicate) -> int:
    pass

if __name__ == "__main__":
    # Monotonic predicate: x >= 7
    assert binary_search_answer(1, 10, lambda x: x >= 7) == 7
    # Monotonic predicate: x > 10 (no solution)
    assert binary_search_answer(1, 10, lambda x: x > 10) == 11
    # Monotonic predicate: x % 2 == 0, first even in [4, 10]
    assert binary_search_answer(4, 10, lambda x: x % 2 == 0) == 4
    # Monotonic predicate: x >= 0, range [0,0], should return 0
    assert binary_search_answer(0, 0, lambda x: x >= 0) == 0
    # Monotonic predicate: x > 5, range [2,7], should return 6
    assert binary_search_answer(2, 7, lambda x: x > 5) == 6
    # Monotonic predicate: x==100, range [50,150], should return 100
    assert binary_search_answer(50, 150, lambda x: x == 100) == 100
    # Monotonic predicate: x >= -2, range [-5,0]
    assert binary_search_answer(-5, 0, lambda x: x >= -2) == -2
    # Monotonic predicate: x < 0 (never True for x >=0)
    assert binary_search_answer(0, 5, lambda x: x < 0) == 6

    print("All tests passed.")
