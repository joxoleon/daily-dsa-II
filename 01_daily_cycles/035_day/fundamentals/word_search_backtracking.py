# [ Name: Word Search Backtracking ]  [ Category: grids ]  [ Topic: backtracking ]  [ Weight: 7 ]

"""
Problem Description:
Given a 2D board of characters and a word, check if the word exists in the board.
The word can be constructed from letters of sequentially adjacent cells, where "adjacent" cells are horizontally or vertically neighboring.
Each cell may only be used once per word.
Return True if the word exists, otherwise False.

Constraints:
- 1 <= len(word) <= 15
- 1 <= rows, cols <= 12
- Board contains only uppercase/lowercase English letters.

Example:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED" -> Output: True
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
    assert exist([["C","A","A"],["A","A","A"],["B","C","D"]], "AAB") == True
    assert exist([["A","B"],["C","D"]], "ACDB") == True
    assert exist([["A","B"],["C","D"]], "ABCD") == False
    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
