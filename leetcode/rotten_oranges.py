class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        it = 0
        fresh = 0
        q = []

        # find all the rotten & fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append([r, c])

        # Start BFS from rotten oranges
        while q and fresh > 0:
            length = len(q)
            for i in range(length):
                r, c = q.pop(0)

                for i,j in directions:
                    k = r + i
                    l = c + j
                    if k in range(rows) and l in range(cols) and grid[k][l] == 1:
                        fresh -= 1
                        grid[k][l] = 2
                        q.append((k,l))

            it += 1

        return it if fresh == 0 else -1
