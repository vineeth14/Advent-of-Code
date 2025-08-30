from process_input import get_input

# This is why you can't track if the guard steps into the same wall with the same direction:-
# So, two different paths could hit the same wall cell from the same direction,
# but lead to different subsequent movement, meaning one might exit while the other loops.
# You’d mark them both the same and miss the distinction.

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
        visit.add((gr, gc, dr, dc))
        if dr + gr not in range(rl) or dc + gc not in range(cl):
            return False
        if grid[gr + dr][gc + dc] == "#":
            dr, dc = dc, -dr
        else:
            gr, gc = gr + dr, gc + dc
        if (gr, gc, dr, dc) in visit:
            return True


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
