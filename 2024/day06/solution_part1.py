from process_input import get_input

grid = get_input()
rl, cl = len(grid), len(grid[0])

# if the direction causes you to go out of bounds that change a flag
# if you come across an obstacle chnage the direction to be 90 degrees

count = [0]
for r in range(rl):
    for c in range(cl):
        if grid[r][c] == "^":
            gr, gc = r, c

visit = set()

dr, dc = -1, 0
r, c = gr, gc
while True:
    visit.add((r, c))
    if r + dr not in range(rl) or c + dc not in range(cl):
        break
    if grid[r + dr][c + dc] == "#":
        dr, dc = dc, -dr
    r = r + dr
    c = c + dc
print(len(visit))
