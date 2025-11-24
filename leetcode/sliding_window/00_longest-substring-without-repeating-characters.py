# [ Name: Longest Substring Without Repeating Characters ]  [ Category: sliding_window ]  [ Topic: sliding_window ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/ ]

"""
Given a string s, find the length of the longest substring without repeating characters.
Return an integer representing the maximum length.
Constraints: 0 <= len(s) <= 5 * 10^4; s consists of English letters, digits, symbols, and spaces.
Example: For input s = "abcabcbb", the output is 3 because "abc" is the longest substring without repeats.
"""

def lengthOfLongestSubstring(s: str) -> int:
    pass

if __name__ == "__main__":
    assert lengthOfLongestSubstring("abcabcbb") == 3
    assert lengthOfLongestSubstring("bbbbb") == 1
    assert lengthOfLongestSubstring("pwwkew") == 3
    assert lengthOfLongestSubstring("") == 0
    assert lengthOfLongestSubstring(" ") == 1
    assert lengthOfLongestSubstring("dvdf") == 3
    assert lengthOfLongestSubstring("anviaj") == 5
    assert lengthOfLongestSubstring("tmmzuxt") == 5