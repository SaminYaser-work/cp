from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        set1, set2 = set(), set()

        def dfs(i, j, visited, prev):
            if (i not in range(rows) or j not in range(cols) or heights[i][j] < prev or (i,j) in visited):
                return
            visited.add((i,j))
            dirs = [[0,1],[0,-1],[1,0],[-1,0]]

            for r,c in dirs:
                dfs(i+r,j+c,visited,heights[i][j])

        for c in range(cols):
            dfs(0, c, set1, heights[0][c])
            dfs(rows-1, c, set2, heights[rows-1][c])

        for r in range(rows):
            dfs(r, 0, set1, heights[r][0])
            dfs(r, cols-1, set2, heights[r][cols-1])

        return set1 & set2
