# [ Name: Encode and Decode Strings ]  [ Category: extra_20_must_know ]  [ Topic: extra_20_must_know ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/encode-and-decode-strings/ ]

"""
Design an algorithm to encode a list of strings into a single string and decode it back to the original list.
You are given a list of strings as input and must implement 'encode' and 'decode' methods.
Each string in the list may be empty or contain any of the 256 valid ASCII characters.
Return type for encode is a single string, and decode restores the list of strings.
Example: Input: ["lint","code","love","you"] -> encode -> decode -> ["lint","code","love","you"]
"""


from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        pass

    def decode(self, s: str) -> List[str]:
        pass

if __name__ == "__main__":
    codec = Codec()
    assert codec.decode(codec.encode([])) == []
    assert codec.decode(codec.encode([""])) == [""]
    assert codec.decode(codec.encode(["abc"])) == ["abc"]
    assert codec.decode(codec.encode(["abc",""])) == ["abc",""]
    assert codec.decode(codec.encode(["","def"])) == ["","def"]
    assert codec.decode(codec.encode(["a","b","c"])) == ["a","b","c"]
    assert codec.decode(codec.encode(["|","||","|||"])) == ["|","||","|||"]
    assert codec.decode(codec.encode(["hello:world", "123", ""])) == ["hello:world","123",""]