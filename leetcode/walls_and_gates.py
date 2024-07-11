from typing import List


class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = []

        # BFS helper function
        def bfs(i,j):
            if (
                not i in range(rows) or 
                not j in range(cols) or 
                (i,j) in visited 
                or grid[i][j] == -1
            ):
                return;
            visited.add((i,j))
            q.append([i,j])


        # Find all the gates
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r,c])
                    visited.add((r,c))
        
        # BFS from all the gates
        dist = 0
        while q:
            for i in range(len(q)):
                r,c = q.pop(0)
                grid[r][c] = dist
                bfs(r+1,c)
                bfs(r-1,c)
                bfs(r,c-1)
                bfs(r,c+1)
            dist += 1


