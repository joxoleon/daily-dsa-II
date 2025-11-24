# [ Name: Pow(x, n) ]  [ Category: math ]  [ Topic: math ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/powx-n/ ]

"""
Implement a function to calculate x raised to the power n (i.e., x^n).
Input: a floating-point number x and an integer n (can be negative, zero, or positive).
Output: a floating-point number representing the result.
Constraints: -100.0 < x < 100.0, -2^31 <= n <= 2^31 - 1.
Example: Input: x = 2.00000, n = 10; Output: 1024.00000
"""

def myPow(x: float, n: int) -> float:
    pass

if __name__ == "__main__":
    assert abs(myPow(2.00000, 10) - 1024.00000) < 1e-5
    assert abs(myPow(2.10000, 3) - 9.26100) < 1e-5
    assert abs(myPow(2.00000, -2) - 0.25000) < 1e-5
    assert abs(myPow(1.00000, 123456) - 1.00000) < 1e-5
    assert abs(myPow(-2.00000, 3) - (-8.00000)) < 1e-5
    assert abs(myPow(0.00001, 2147483647)) < 1e-5
    assert abs(myPow(2.00000, 0) - 1.00000) < 1e-5
    assert abs(myPow(-1.00000, 2147483647) - (-1.00000)) < 1e-5