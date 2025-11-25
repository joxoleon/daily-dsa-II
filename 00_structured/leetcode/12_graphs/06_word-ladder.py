# [ Name: Word Ladder ]  [ Category: graphs ]  [ Topic: graphs ]  [ Weight: 10 ]  [ Difficulty: Hard ]
# [ Link: https://leetcode.com/problems/word-ladder/ ]

"""
Given two words, beginWord and endWord, and a list of words wordList, find the shortest transformation sequence length from beginWord to endWord. Each transformation must change exactly one letter and all words must be in wordList. Return 0 if no such sequence exists.
Inputs: beginWord (str), endWord (str), wordList (List[str])
Output: int (shortest transformation length)
Constraints: 1 <= beginWord.length == endWord.length <= 10, 1 <= wordList.length <= 5000
Example: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"] -> Output: 5
"""

from typing import List

def ladderLength(beginWord: str, endWord: str, wordList: List[str]) -> int:
    pass

if __name__ == "__main__":
    assert ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]) == 5
    assert ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]) == 0
    assert ladderLength("a", "c", ["a","b","c"]) == 2
    assert ladderLength("game", "thee", ["fame","gave","gale","gate","thee"]) == 0
    assert ladderLength("lost", "cost", ["most","fost","lost","cost","host"]) == 2
    assert ladderLength("red", "tax", ["ted","tex","red","tax","tad","den","rex","pee"]) == 4
    assert ladderLength("a", "c", ["a","b","c","d"]) == 2
    assert ladderLength("hot", "dog", ["hot","dog"]) == 0