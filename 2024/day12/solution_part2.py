"""
Day 12 Part 2: Garden Fencing with Bulk Discount

Key Insight: Number of sides = Number of corners in a polygon

Approach:
1. BFS to find all connected regions of same plant type
2. For each region, count corners (not perimeter like part 1)
3. Corner counting:
   - Each grid point can be surrounded by 0-4 cells from the region
   - Check each unique corner point only once (deduplicate!)
   - Count based on pattern of surrounding cells:
     * 0 or 4 cells: 0 corners (exterior or interior point)
     * 1 or 3 cells: 1 corner (outer/inner corner)
     * 2 cells diagonal: 2 corners (two regions touching diagonally)
     * 2 cells adjacent: 0 corners (just an edge)
4. Price = area × corners for each region
"""

from process_input import get_input
import collections

directions = [[0, 1], [1, 0], [-1, 0], [0, -1]]

grid = get_input()
rl, cl = len(grid), len(grid[0])
visited_plants = set()
q = collections.deque()
regions = []


def bfs(r, c):
    region_set = set()
    while q:
        r, c = q.popleft()
        if (r, c) in region_set:
            continue

        region_set.add((r, c))
        visited_plants.add((r, c))

        for dr, dc in directions:
            nr, nc = dr + r, dc + c
            if (
                nr in range(rl)
                and nc in range(cl)
                and (nr, nc) not in visited_plants
                and grid[nr][nc] == grid[r][c]
            ):
                q.append((nr, nc))

    return region_set


def check_top_left_corner(r, c, region_set):
    """Check if corner point (r,c) forms a corner based on 4 surrounding cells"""
    # Cells clockwise from upper-left: diag, top, current, left
    diag = (r-1, c-1) in region_set
    top = (r-1, c) in region_set
    curr = (r, c) in region_set
    left = (r, c-1) in region_set

    insides = [diag, top, curr, left]
    count = sum(insides)

    if count == 0 or count == 4:
        return 0
    elif count == 1 or count == 3:
        return 1
    else:  # count == 2
        if insides == [True, False, True, False] or insides == [False, True, False, True]:
            return 2  # Diagonal pattern
        else:
            return 0  # Adjacent pattern


def get_corner_candidates(r, c):
    """Get 4 corner points around cell (r,c)"""
    return [(r, c), (r, c+1), (r+1, c), (r+1, c+1)]


def count_region_corners(region_set):
    """Count corners by checking each unique corner point once"""
    corner_points = set()
    for r, c in region_set:
        for corner in get_corner_candidates(r, c):
            corner_points.add(corner)

    total = 0
    for r, c in corner_points:
        total += check_top_left_corner(r, c, region_set)

    return total


# Build all regions
for r in range(rl):
    for c in range(cl):
        if (r, c) not in visited_plants:
            q.append((r, c))
            region_set = bfs(r, c)
            regions.append(region_set)

# Process each region for corners
total = 0
for region_set in regions:
    area = len(region_set)
    corners = count_region_corners(region_set)
    price = area * corners
    print(f"Region: area={area}, sides={corners}, price={price}")
    total += price

print(f"\nTotal price: {total}")
