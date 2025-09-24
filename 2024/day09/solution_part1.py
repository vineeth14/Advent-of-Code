from process_input import get_input

grid = get_input()


def find_trailhead(grid):
    rl = len(grid)
    cl = len(grid[0])

    # trailheads = []

    directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

    def dfs(r, c, count, visit):
        if grid[r][c] == 9 and (r, c) not in visit:
            count += 1
            visit.add((r, c))

        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if nc in range(cl) and nr in range(rl) and grid[nr][nc] == grid[r][c] + 1:
                count = dfs(nr, nc, count, visit)
        return count

    total = 0
    for r in range(rl):
        for c in range(cl):
            if grid[r][c] == 0:
                visit = set()
                total += dfs(r, c, 0, visit)
            #    trailheads.append((r, c))
            #
    print(total)


find_trailhead(grid)
