# [ Name: Group Anagrams ]  [ Category: hashing ]  [ Topic: hashing ]  [ Weight: 10 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/group-anagrams/ ]

"""
Given an array of strings, group the anagrams together.
Return a list of grouped anagrams, where each group is a list of strings.
Each string consists of lowercase English letters.
All inputs will be in lowercase and the array length is at most 10^4.
Example: Input: ["eat","tea","tan","ate","nat","bat"]
Output: [["eat","tea","ate"],["tan","nat"],["bat"]]
"""

from typing import List

def groupAnagrams(strs: List[str]) -> List[List[str]]:
    pass

if __name__ == "__main__":
    assert sorted([sorted(g) for g in groupAnagrams(["eat","tea","tan","ate","nat","bat"])]) == sorted([["bat"],["nat","tan"],["ate","eat","tea"]])
    assert sorted([sorted(g) for g in groupAnagrams(["a"])]) == sorted([["a"]])
    assert sorted([sorted(g) for g in groupAnagrams([""])]) == sorted([[""]])
    assert sorted([sorted(g) for g in groupAnagrams(["abc","bca","cab","bac","acb","cba"])]) == sorted([["abc","bca","cab","bac","acb","cba"]])
    assert sorted([sorted(g) for g in groupAnagrams(["ab","ba","abc","acb","bac","bca","zzz","zz"])]) == sorted([["ab","ba"],["abc","acb","bac","bca"],["zzz"],["zz"]])
    assert sorted([sorted(g) for g in groupAnagrams(["aaaa","aaaa","bbbb","bbbb"])) == sorted([["aaaa","aaaa"],["bbbb","bbbb"]])
    assert sorted([sorted(g) for g in groupAnagrams(["listen","silent","enlists","google","inlets","banana"])]) == sorted([["listen","silent","inlets"],["enlists"],["google"],["banana"]])
    assert sorted([sorted(g) for g in groupAnagrams(["tab","bat","tba","eat","tea","ate","aet","eta"])]) == sorted([["tab","bat","tba"],["eat","tea","ate","aet","eta"]])
