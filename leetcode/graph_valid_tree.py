from typing import List


# A graph is a tree if its fully connected and has no cycles
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        adj = {i: [] for i in range(n)}
        for e1, e2 in edges:
            adj[e1].append(e2)
            adj[e2].append(e1)

        visited = set()

        def dfs(e, prev):
            if e in visited:
                return False

            visited.add(e)
            for a in adj[e]:
                if a == prev:
                    continue
                if not dfs(a, e):
                    return False
            return True

        return dfs(0, -99) and len(visited) == n
