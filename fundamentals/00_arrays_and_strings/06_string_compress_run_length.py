# [ Name: Simple Run-Length Encoding ]  [ Category: strings ]  [ Topic: compression ]  [ Weight: 5 ]

"""
Problem Description:
Given a string s, return its run-length encoding as a new string.
In run-length encoding, consecutive duplicate characters are replaced with a single character followed by the number of repetitions.
The input string contains only lowercase English letters and may be empty.
Return an empty string if s is empty.

Constraints:
- 0 <= len(s) <= 10^5

Example:
Input: "aaabbc" -> Output: "a3b2c1"
"""

def rle_compress(s: str) -> str:
    if not s:
        return ""
    res = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            res.append(s[i - 1])
            res.append(str(count))
            count = 1
    res.append(s[-1])
    res.append(str(count))
    return "".join(res)
    

if __name__ == "__main__":
    assert rle_compress("aaabbc") == "a3b2c1"
    assert rle_compress("") == ""
    assert rle_compress("abcd") == "a1b1c1d1"
    assert rle_compress("a") == "a1"
    assert rle_compress("aaaaa") == "a5"
    assert rle_compress("aabbbaa") == "a2b3a2"
    assert rle_compress("zzzzzzzz") == "z8"
    assert rle_compress("xyxyzz") == "x1y1x1y1z2"

    print("All tests passed.")