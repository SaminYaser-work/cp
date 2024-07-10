class Solution:

    def dfs(self, grid, i, j):
        if i not in range(self.rows) or j not in range(self.cols) or grid[i][j] == 0 or (i, j) in self.visited:
            return 0

        self.visited.add((i, j))

        return 1 + self.dfs(grid, i, j + 1) + self.dfs(grid, i, j-1) + self.dfs(grid, i+1, j) + self.dfs(grid, i-1, j)

    def maxAreaOfIsland(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        area = 0
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.visited = set()

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == 1:
                    area = max(self.dfs(grid, r, c), area)

        return area
