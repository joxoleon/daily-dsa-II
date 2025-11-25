# [ Name: DP — Fibonacci Bottom-Up ]  [ Category: dp ]  [ Topic: 1d_dp ]  [ Weight: 5 ]

"""
Problem Description:
Given an integer n, return the n-th number in the Fibonacci sequence (0-indexed).
The Fibonacci sequence is defined as follows: F(0) = 0, F(1) = 1, and F(i) = F(i-1) + F(i-2) for i > 1.
Return the computed integer.
Constraints:
- 0 <= n <= 40

Example:
Input: n = 4 -> Output: 3
"""


def fib(n: int) -> int:
    pass


if __name__ == "__main__":
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(4) == 3
    assert fib(10) == 55
    assert fib(20) == 6765
    assert fib(40) == 102334155

    print("All tests passed.")
