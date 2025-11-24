# [ Name: Hash Map — Character Frequency Counter ]  [ Category: strings ]  [ Topic: hashmap_frequency ]  [ Weight: 3 ]

"""
Problem Description:
Given a non-empty string s, compute the frequency of each character present in the string.
Return the result as a dictionary mapping each character to its count.
All inputs will contain only lowercase and/or uppercase English letters.
The output dictionary should include all unique characters in s.
Constraint: 1 <= len(s) <= 10^4

Example:
Input: "aabbc" -> Output: {'a': 2, 'b': 2, 'c': 1}
"""

from typing import Dict

def char_frequency(s: str) -> Dict[str, int]:
    pass

if __name__ == "__main__":
    assert char_frequency("aabbc") == {'a': 2, 'b': 2, 'c': 1}
    assert char_frequency("abcABC") == {'a':1, 'b':1, 'c':1, 'A':1, 'B':1, 'C':1}
    assert char_frequency("a") == {'a': 1}
    assert char_frequency("AAAaaa") == {'A': 3, 'a': 3}
    assert char_frequency("xyzzyx") == {'x':2,'y':2,'z':2}
    assert char_frequency("Z") == {'Z':1}
    assert char_frequency("mississippi") == {'m':1,'i':4,'s':4,'p':2}
    assert char_frequency("HelloWorld") == {'H':1,'e':1,'l':3,'o':2,'W':1,'r':1,'d':1}
    print("All tests passed.")
