from process_input import get_input


grid = get_input()
rl, cl = len(grid), len(grid[0])

for r in range(rl):
    for c in range(cl):
        if grid[r][c] == "^":
            gr, gc = r, c


def is_loop(grid, gr, gc):
    visit = set()
    dr, dc = -1, 0

    while True:
        if gr + dr not in range(rl) or gc + dc not in range(cl):
            return False
        if grid[gr + dr][gc + dc] == "#":
            if (gr + dr, gc + dc, dr, dc) in visit:
                return True
            visit.add((gr + dr, gc + dc, dr, dc))
            dr, dc = dc, -dr
        else:
            gr, gc = gr + dr, gc + dc


def stuck_in_a_loop(grid, gr, gc):
    count = 0
    for r in range(rl):
        for c in range(cl):
            if grid[r][c] != ".":
                continue
            grid[r][c] = "#"
            if is_loop(grid, gr, gc):
                count += 1
            grid[r][c] = "."
    print(count)


stuck_in_a_loop(grid, gr, gc)
