# Use DFS to traverse in 2 horizontal and 2 vertical directions
# This will add all the parts of a island to the visited set
# Loop over all the grid elements. If a '1' is found its either a
# part of a new island or an already discovered island, which depends
# on if its in the visited set or not.

class Solution:
    def dfs(self, grid, i, j):
        if (
            (i, j) in self.visited
            or not 0 <= i < self.rows
            or not 0 <= j < self.cols
            or grid[i][j] == "0"
        ):
            return
        self.visited.add((i, j))
        dirs = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        for k, l in dirs:
            self.dfs(grid, k + i, l + j)

    def numIslands(self, grid) -> int:
        if not grid or not grid[0]:
            return 0

        ils = 0
        self.visited = set()
        self.rows = len(grid)
        self.cols = len(grid[0])

        for r in range(self.rows):
            for c in range(self.cols):
                if grid[r][c] == "1" and (r, c) not in self.visited:
                    ils += 1
                    self.dfs(grid, r, c)
        return ils
