# [ Name: Union-Find — Union by Rank ]  [ Category: union_find ]  [ Topic: dsu_optimization ]  [ Weight: 7 ]

"""
Problem Description:
Implement a Union-Find (Disjoint Set Union) data structure with union by rank.
You are given an integer n, representing n elements (0 to n-1), and must support union(x, y) to connect two elements, and find(x) to determine the root of an element.
union(x, y) should return True if x and y were in different sets, or False if they were already connected.
Constraints:
- 1 <= n <= 10^4
- 0 <= x, y < n

Example:
uf = UnionFind(3); uf.union(0,1) -> True; uf.union(0,1) -> False
"""

class UnionFind:
    def __init__(self, n: int):
        pass
    def find(self, x: int) -> int:
        pass
    def union(self, x: int, y: int) -> bool:
        pass

if __name__ == "__main__":
    uf = UnionFind(5)
    assert uf.union(0, 1) == True
    assert uf.union(1, 2) == True
    assert uf.union(0, 2) == False
    assert uf.union(3, 4) == True
    assert uf.find(0) == uf.find(2)
    assert uf.find(3) != uf.find(0)
    assert uf.union(2, 4) == True
    assert uf.find(0) == uf.find(3)

    uf2 = UnionFind(1)
    assert uf2.union(0, 0) == False
    assert uf2.find(0) == 0

    uf3 = UnionFind(2)
    assert uf3.union(0, 1) == True
    assert uf3.union(0, 1) == False
    assert uf3.find(1) == uf3.find(0)

    from resources.progress.progress_tracker import mark_solved
    mark_solved(__file__)
    print("All tests passed.")
