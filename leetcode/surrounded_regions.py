from typing import List


# Find unsurrounded regions in the borders and run dfs on them to find other
# unsurrounded regions. The remaining are surrounded.
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])
        visited = set()

        def dfs(r,c):
            if r not in range(rows) or c not in range(cols) or (r,c) in visited or board[r][c] != 'O':
                return
            visited.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for r in [0, rows-1]:
            for c in range(cols):
                if board[r][c] == 'O':
                    dfs(r,c)
    
        for r in range(rows):
            for c in [0, cols-1]:
                if board[r][c] == 'O':
                    dfs(r,c)

        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited and board[r][c] == 'O':
                    board[r][c] = 'X'