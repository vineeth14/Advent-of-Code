from process_input import get_input
import collections

directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

grid = get_input()
rl, cl = len(grid), len(grid[0])
visit = set()
q = collections.deque()


def bfs(r, c, area, peri):
    while q:
        for i in range(len(q)):
            r, c = q.popleft()
            visit.add((r, c))

            area += 1
            peri += calc_peri(r, c)
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
    return area, peri


def calc_peri(r, c):
    peri = 0
    for dr, dc in directions:
        nr, nc = dr + r, dc + c
        if nr not in range(rl):
            peri += 1
            continue
        if nc not in range(cl):
            peri += 1
            continue
        if grid[r][c] != grid[nr][nc]:
            print(grid[r][c], r, c, peri)
            peri += 1
    return peri


total = 0
for r in range(rl):
    for c in range(cl):
        if (r, c) not in visit:
            q.append((r, c))
            area, peri = bfs(r, c, 0, 0)
            print(area, peri, grid[r][c])
            total += area * peri
print(total)
