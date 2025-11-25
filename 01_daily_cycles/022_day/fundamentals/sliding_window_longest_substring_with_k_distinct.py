# [ Name: Sliding Window — Longest Substring with K Distinct ]  [ Category: strings ]  [ Topic: sliding_window_k_distinct ]  [ Weight: 7 ]

"""
Problem Description:
Given a string s and an integer k, return the length of the longest substring that contains at most k distinct characters.
If k is 0 or the string is empty, return 0.
Characters are case-sensitive.
Constraints: 0 <= k <= len(s) <= 10^5

Example:
Input: s = "eceba", k = 2 -> Output: 3  (The substring is "ece")
"""

def length_of_longest_k_distinct(s: str, k: int) -> int:
    pass


if __name__ == "__main__":
    assert length_of_longest_k_distinct("eceba", 2) == 3
    assert length_of_longest_k_distinct("aa", 1) == 2
    assert length_of_longest_k_distinct("a", 0) == 0
    assert length_of_longest_k_distinct("", 2) == 0
    assert length_of_longest_k_distinct("abaccc", 2) == 4
    assert length_of_longest_k_distinct("abcabcbb", 3) == 3
    assert length_of_longest_k_distinct("abcbbcabbca", 2) == 4
    assert length_of_longest_k_distinct("aaaaa", 1) == 5

    print("All tests passed.")
