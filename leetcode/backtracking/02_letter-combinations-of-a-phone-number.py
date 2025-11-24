# [ Name: Letter Combinations of a Phone Number ]  [ Category: backtracking ]  [ Topic: backtracking ]  [ Weight: 8 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/letter-combinations-of-a-phone-number/ ]

"""
Given a string containing digits from 2-9, return all possible letter combinations that the number could represent based on a phone keypad mapping. 
Input: digits string (length 0–4). 
Output: List of non-empty letter combinations.
Constraints: 0 <= len(digits) <= 4, digits contain only '2' to '9'.
Example: Input: "23" Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

from typing import List

def letterCombinations(digits: str) -> List[str]:
    pass

if __name__ == "__main__":
    assert letterCombinations("23") == ["ad","ae","af","bd","be","bf","cd","ce","cf"]
    assert letterCombinations("") == []
    assert letterCombinations("2") == ["a","b","c"]
    assert letterCombinations("9") == ["w","x","y","z"]
    assert set(letterCombinations("7")) == set(["p","q","r","s"])
    assert set(letterCombinations("79")) == set([
        "pw","px","py","pz","qw","qx","qy","qz",
        "rw","rx","ry","rz","sw","sx","sy","sz"
    ])
    assert set(letterCombinations("234")) == set([
        "adg","adh","adi","aeg","aeh","aei","afg","afh","afi",
        "bdg","bdh","bdi","beg","beh","bei","bfg","bfh","bfi",
        "cdg","cdh","cdi","ceg","ceh","cei","cfg","cfh","cfi"
    ])
    assert letterCombinations("4") == ["g","h","i"]