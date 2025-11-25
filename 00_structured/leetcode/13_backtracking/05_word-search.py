# [ Name: Word Search ]  [ Category: backtracking ]  [ Topic: backtracking ]  [ Weight: 9 ]  [ Difficulty: Medium ]
# [ Link: https://leetcode.com/problems/word-search/ ]

"""
Given an m x n grid of characters board and a string word, determine if word exists in the grid.
You can move horizontally or vertically to adjacent cells, but you cannot use the same cell more than once.
Return True if the word can be formed, otherwise return False.
Constraints: 1 <= board.length, board[i].length <= 6; 1 <= word.length <= 15; board and word only contain uppercase and lowercase English letters.
Example: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" returns True.
"""

from typing import List

def exist(board: List[List[str]], word: str) -> bool:
    pass

if __name__ == "__main__":
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED") == True
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE") == True
    assert exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB") == False
    assert exist([["A"]], "A") == True
    assert exist([["A"]], "B") == False
    assert exist([["A","A","A","A"],["A","A","A","A"],["A","A","A","A"]], "AAAAAAAAAAAAA") == True
    assert exist([["A","B"],["C","D"]], "ACDB") == True
    assert exist([["A","B"],["C","D"]], "ABDC") == False