# [ Name: Sliding Window — Longest Substring Without Repeating Characters ]  [ Category: strings ]  [ Topic: sliding_window_hash ]  [ Weight: 8 ]

"""
Problem Description:
Given a string s, find the length of the longest substring without repeating characters.
Return the maximum length as an integer.
s consists of English letters, digits, symbols, and spaces.
Constraints: 0 <= len(s) <= 10^5
Example:
Input: "abcabcbb" -> Output: 3
"""

def length_of_longest_substring(s: str) -> int:
    pass


if __name__ == "__main__":
    assert length_of_longest_substring("") == 0
    assert length_of_longest_substring("a") == 1
    assert length_of_longest_substring("bbbbb") == 1
    assert length_of_longest_substring("abcabcbb") == 3
    assert length_of_longest_substring("pwwkew") == 3
    assert length_of_longest_substring("dvdf") == 3
    assert length_of_longest_substring(" ") == 1
    assert length_of_longest_substring("abcadefg") == 6

    print("All tests passed.")
