class Solution(object):
    def solveNQueens(self, n):
        result = []
        grid = []
        placed = []
        for i in range(0, n):
            grid.append([0] * n)
            placed.append(["."] * n)

        def check(i, j):
            x, y = i, j
            # check column upwards
            while x >= 0:
                if grid[x][y] == 1:
                    return False
                x -= 1

            x, y = i, j
            # check left diagonal
            while x >= 0 and y >= 0:
                if grid[x][y] == 1:
                    return False
                x -= 1
                y -= 1

            x, y = i, j
            # check right diagonal
            while x >= 0 and y < n:
                if grid[x][y] == 1:
                    return False
                x -= 1
                y += 1

            return True

        def run(idx):
            if idx == n:
                result.append(["".join(r) for r in placed[:]])
                return

            for j in range(0, n):
                if check(idx, j):
                    grid[idx][j] = 1
                    placed[idx][j] = "Q"
                    run(idx + 1)
                    placed[idx][j] = "."
                    grid[idx][j] = 0

        run(0)
        return result