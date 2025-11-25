# [ Name: DP — Edit Distance ]  [ Category: dp ]  [ Topic: 2d_dp ]  [ Weight: 9 ]

"""
Problem Description:
Given two strings s1 and s2, return the minimum number of operations required to convert s1 into s2.
Allowed operations are: insert a character, delete a character, or replace a character.
Return an integer indicating the least number of edits to transform s1 into s2.

Constraints:
- 0 <= len(s1), len(s2) <= 500
- s1 and s2 contain only lowercase English letters.

Example:
Input: s1 = "kitten", s2 = "sitting" -> Output: 3
"""

def edit_distance(s1: str, s2: str) -> int:
    pass

if __name__ == "__main__":
    assert edit_distance("kitten", "sitting") == 3
    assert edit_distance("", "") == 0
    assert edit_distance("a", "") == 1
    assert edit_distance("", "a") == 1
    assert edit_distance("abc", "yabc") == 1
    assert edit_distance("abcdef", "azced") == 3
    assert edit_distance("intention", "execution") == 5
    assert edit_distance("aaa", "aaa") == 0

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
