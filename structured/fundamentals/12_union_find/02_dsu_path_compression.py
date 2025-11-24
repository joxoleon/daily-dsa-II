# [ Name: Union-Find — Path Compression ]  [ Category: union_find ]  [ Topic: dsu_optimization ]  [ Weight: 9 ]

"""
Problem Description:
Implement a union-find (disjoint set) data structure with path compression.
Supports union(x, y) to merge the sets containing x and y, and find(x) to find the root of x.
Initialize with n elements labeled 0 to n-1.
Assume 1 <= n <= 10^5. Elements are integers in that range.
No duplicate unions guaranteed.

Example:
After union(1, 2) and union(2, 3), find(3) should return the same root as find(1).
"""

class UnionFind:
    def __init__(self, n: int):
        pass
    def find(self, x: int) -> int:
        pass
    def union(self, x: int, y: int) -> None:
        pass

if __name__ == "__main__":
    uf = UnionFind(5)
    uf.union(0, 1)
    assert uf.find(0) == uf.find(1)
    uf.union(2, 3)
    assert uf.find(2) == uf.find(3)
    assert uf.find(1) != uf.find(2)
    uf.union(1, 2)
    assert uf.find(0) == uf.find(2)
    uf.union(3, 4)
    assert uf.find(4) == uf.find(2)
    uf2 = UnionFind(2)
    assert uf2.find(0) != uf2.find(1)
    uf2.union(0, 1)
    assert uf2.find(0) == uf2.find(1)
    uf3 = UnionFind(1)
    assert uf3.find(0) == 0
    print("All tests passed.")
