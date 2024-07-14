from typing import List


# Topological sort. Early exit if cycle is detected
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {i: [] for i in range(numCourses)}

        for c, p in prerequisites:
            adj[c].append(p)

        visited, cycle = set(), set()
        res = []

        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True

            cycle.add(c)
            for p in adj[c]:
                if dfs(p) == False:
                    return False
            cycle.remove(c)
            visited.add(c)
            res.append(c)

        for i in range(numCourses):
            if dfs(i) == False:
                return []

        return res
