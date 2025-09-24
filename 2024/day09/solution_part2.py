from process_input import get_input

grid = get_input()


def find_unique_trailheads(grid):
    rl = len(grid)
    cl = len(grid[0])

    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def dfs(r, c, count):
        if grid[r][c] == 9:
            count += 1

        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if nc in range(cl) and nr in range(rl) and grid[nr][nc] == grid[r][c] + 1:
                count = dfs(nr, nc, count)
        return count

    total = 0
    for r in range(rl):
        for c in range(cl):
            if grid[r][c] == 0:
                total += dfs(r, c, 0)
    print(total)


find_unique_trailheads(grid)
