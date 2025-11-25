# [ Name: Implement strStr() ]  [ Category: strings ]  [ Topic: strings ]  [ Weight: 6 ]  [ Difficulty: Easy ]
# [ Link: https://leetcode.com/problems/implement-strstr/ ]

"""
Given two strings haystack and needle, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
If needle is an empty string, return 0.
0 <= haystack.length, needle.length <= 5 * 10^4
Both haystack and needle consist of only lowercase English characters.
Example: haystack = "hello", needle = "ll" returns 2.
"""

def strStr(haystack: str, needle: str) -> int:
    pass

if __name__ == "__main__":
    assert strStr("hello", "ll") == 2
    assert strStr("aaaaa", "bba") == -1
    assert strStr("", "") == 0
    assert strStr("a", "") == 0
    assert strStr("", "a") == -1
    assert strStr("mississippi", "issi") == 1
    assert strStr("leetcode", "leet") == 0
    assert strStr("leetcode", "code") == 4
