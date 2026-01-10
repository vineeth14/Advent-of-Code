import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DIRECTIONS = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

def get_input(filename = "input.txt"):
    filepath = os.path.join(BASE_DIR, filename)

    with open(filepath) as f:
        grid = [list(line.strip()) for line in f]
    return grid

def verify(r,c, grid):
    
    count = 0
    rl, cl = len(grid), len(grid[0])
    for dr, dc in DIRECTIONS:
        nr, nc = r+dr, c+dc
        if nr in range(rl) and nc in range(cl) and  grid[nr][nc] == "@":
            count += 1
    return count < 4

def solution():
    grid = get_input()
    rl, cl = len(grid), len(grid[0])
    total = 0
    for r in range(rl):
        for c in range(cl):
            if grid[r][c] == "@":
                if verify(r,c, grid):
                    total += 1
    return total

print(solution())



