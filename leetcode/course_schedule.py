from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {i:[] for i in range(numCourses)}
        visited = set()

        for c, p in prerequisites:
            m[c].append(p)

        def dfs(c):
            if c in visited:
                return False

            
            if len(m[c]) == 0:
                return True

            visited.add(c)
            for p in m[c]:
                if not dfs(p):
                    return False
            visited.remove(c)
            m[c] = []
            return True
             

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
            
        
