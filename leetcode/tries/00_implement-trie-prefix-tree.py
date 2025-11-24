# [ Name: Implement Trie ]  [ Category: tries ]  [ Topic: tries ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/implement-trie-prefix-tree/ ]

"""
Design a Trie (prefix tree) with insert, search, and startsWith methods.
Implement the following:
- insert(word): Inserts a word into the trie.
- search(word): Returns true if the word is in the trie.
- startsWith(prefix): Returns true if there is any word with the given prefix.
Constraints: word and prefix consist of lowercase English letters, max length per operation ≤ 2000.
Example: insert("apple"), search("apple") → True, search("app") → False, startsWith("app") → True
"""

class Trie:

    def __init__(self):
        pass

    def insert(self, word: str) -> None:
        pass

    def search(self, word: str) -> bool:
        pass

    def startsWith(self, prefix: str) -> bool:
        pass

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    assert trie.search("apple") == True
    assert trie.search("app") == False
    assert trie.startsWith("app") == True
    trie.insert("app")
    assert trie.search("app") == True
    trie.insert("banana")
    assert trie.search("banana") == True
    assert trie.startsWith("ban") == True
    assert trie.startsWith("bana") == True
    assert trie.startsWith("band") == False