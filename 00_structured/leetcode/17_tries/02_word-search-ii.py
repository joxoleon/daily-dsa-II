# [ Name: Word Search II ]  [ Category: tries ]  [ Topic: tries ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/word-search-ii/ ]

"""
Given a 2D board of letters and a list of words, find all words that can be formed by letters of sequentially adjacent cells (vertically or horizontally). Each cell may only be used once per word.
Return the list of found words.
Constraints: 1 <= board dimensions <= 12, 1 <= number of words <= 3 * 10^3, 1 <= length of each word <= 10.
Example: Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], words = ["oath","pea","eat","rain"]
Output: ["oath","eat"]
"""

from typing import List

def findWords(board: List[List[str]], words: List[str]) -> List[str]:
    pass

if __name__ == "__main__":
    assert sorted(findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])) == ["eat","oath"]
    assert sorted(findWords([["a","b"],["c","d"]], ["abcb"])) == []
    assert sorted(findWords([["a","a"]], ["aaa"])) == []
    assert sorted(findWords([["a"]], ["a"])) == ["a"]
    assert sorted(findWords([["a","b"],["c","d"]], ["abcd","acdb","dbca","bacd"])) == []
    assert sorted(findWords([["o","a"],["e","t"]], ["oat","eat"])) == ["eat","oat"]
    assert sorted(findWords([["a","b","c"],["d","e","f"],["g","h","i"]], ["abc","def","ghi","aei","beh"])) == ["abc","def","ghi"]
    assert sorted(findWords([["s","e","e","n","e","w"],["t","m","r","i","v","a"],["o","b","s","i","b","d"],["w","m","y","s","e","n"],["l","t","s","n","s","a"],["i","e","z","l","g","n"]], ["news","seat","same","seen","web","zone"])) == ["news","seat","seen","web"]