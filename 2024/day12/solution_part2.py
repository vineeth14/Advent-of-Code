from process_input import get_input
import collections

directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

grid = get_input()
rl, cl = len(grid), len(grid[0])
visit = set()
q = collections.deque()


def bfs(r, c, area):
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            visit.add((r, c))

            area += 1
            sides += cornerCount(r, c)
            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (
                    nr in range(rl)
                    and nc in range(cl)
                    and (nr, nc) not in visit
                    and grid[nr][nc] == grid[r][c]
                ):
                    q.append((nr, nc))
                    visit.add((nr, nc))
    return area


def isCorner(r, c):
    count = 4
    if grid


total = 0
for r in range(rl):
    for c in range(cl):
        if (r, c) not in visit:
            q.append((r, c))
print(total)
