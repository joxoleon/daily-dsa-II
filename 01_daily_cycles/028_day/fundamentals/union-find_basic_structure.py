# [ Name: Union-Find — Basic Structure ]  [ Category: union_find ]  [ Topic: dsu_core ]  [ Weight: 8 ]

"""
Problem Description:
Design a Union-Find (Disjoint Set Union) data structure to support `n` elements labeled 0 to n-1. 
Implement two methods: `find(x)` returns the root ancestor of element `x`, and the constructor initializes the structure for n elements (each in its own set).
Assume 1 <= n <= 10^4 and 0 <= x < n for all calls.
No unions or merges are required in this basic version.

Example:
If n=3, then find(1) should return 1.
"""

class UnionFind:
    def __init__(self, n: int):
        pass
    def find(self, x: int) -> int:
        pass

if __name__ == "__main__":
    uf = UnionFind(5)
    assert uf.find(0) == 0
    assert uf.find(1) == 1
    assert uf.find(2) == 2
    assert uf.find(3) == 3
    assert uf.find(4) == 4
    uf2 = UnionFind(1)
    assert uf2.find(0) == 0
    uf3 = UnionFind(2)
    assert uf3.find(0) == 0
    assert uf3.find(1) == 1
    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
