class Solution(object):
    def numIslands(self, grid):
        if not grid:
            return 0

        row = len(grid)
        col = len(grid[0])

        def capture(r, c):
            if r < 0 or c < 0 or r >= row or c >= col or grid[r][c] != '1':
                return
            grid[r][c] = '0'
            capture(r + 1, c)
            capture(r - 1, c)
            capture(r, c + 1)
            capture(r, c - 1)

        count = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == '1':
                    count += 1
                    capture(r, c)

        return count
