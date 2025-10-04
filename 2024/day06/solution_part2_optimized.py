from process_input import get_input


grid = get_input()
rl, cl = len(grid), len(grid[0])

for r in range(rl):
    for c in range(cl):
        if grid[r][c] == "^":
            gr, gc = r, c

# An obstacle can only create a loop if placed in guards original path
# First get the original path and add to set. Then only place obstacles if in path

guards_path = set()

dr, dc = -1, 0
r, c = gr, gc
while True:
    guards_path.add((r, c))
    if r + dr not in range(rl) or c + dc not in range(cl):
        break
    if grid[r + dr][c + dc] == "#":
        dr, dc = dc, -dr
    else:
        r = r + dr
        c = c + dc


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
            if (r, c) in guards_path:
                grid[r][c] = "#"
                if is_loop(grid, gr, gc):
                    count += 1
                grid[r][c] = "."
    print(count)


stuck_in_a_loop(grid, gr, gc)
