# [ Name: Design Add and Search Words Data Structure ]  [ Category: tries ]  [ Topic: tries ]  [ Weight: 10 ]  [ Difficulty: unknown ]
# [ Link: https://leetcode.com/problems/add-and-search-word-data-structure-design/ ]

"""
Design a data structure that supports adding new words and searching for words, where the search can contain the '.' wildcard character representing any letter. Implement the WordDictionary class with addWord(word: str) and search(word: str) methods. 
Constraints: 
- 1 <= word.length <= 25
- word consists of lowercase English letters and/or '.'
Example: After adding "bad", "dad", and "mad", search("b..") should return True.
"""

class WordDictionary:
    def __init__(self):
        pass

    def addWord(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

if __name__ == "__main__":
    wd = WordDictionary()
    wd.addWord("bad")
    wd.addWord("dad")
    wd.addWord("mad")
    assert wd.search("pad") == False
    assert wd.search("bad") == True
    assert wd.search(".ad") == True
    assert wd.search("b..") == True
    wd.addWord("baddy")
    assert wd.search("baddy") == True
    assert wd.search("ba..y") == True
    assert wd.search("b...y") == True
    assert wd.search(".....") == False
