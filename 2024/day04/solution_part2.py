from process_input import get_input


def word_search_mas(grid):
    rl, cl = len(grid), len(grid[0])

    def dfs(r, c):
        diag1 = grid[r - 1][c - 1] + "A" + grid[r + 1][c + 1]
        diag2 = grid[r + 1][c - 1] + "A" + grid[r - 1][c + 1]
        count = 0

        if (diag1 == "MAS" or diag1 == "SAM") and (diag2 == "MAS" or diag2 == "SAM"):
            count += 1
        return count

    total = 0
    for r in range(1, rl - 1):
        for c in range(1, cl - 1):
            if grid[r][c] == "A":
                total += dfs(r, c)
    print(total)


grid = get_input()
word_search_mas(grid)
