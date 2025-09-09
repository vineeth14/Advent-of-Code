from collections import defaultdict
from process_input import get_input

grid = get_input()
rl, cl = len(grid), len(grid[0])

antennas = defaultdict(list)

for r in range(rl):
    for c in range(cl):
        if grid[r][c] != ".":
            antennas[grid[r][c]].append((r, c))

#  The key insight is that antinodes form by extending the line between two antennas. Think of it as: if you have two points and draw a line through them, the
#  antinodes are at equal distances on either side, making the original antennas the "middle third" of a larger line segment.


def find_antinode(antennas_positions):
    antinodes = set()

    for i in range(len(antennas_positions)):
        for j in range(i + 1, len(antennas_positions)):
            r1, c1 = antennas_positions[i]
            r2, c2 = antennas_positions[j]

            # calculating vector
            dr = r2 - r1
            dc = c2 - c1

            antinode1 = (r1 - dr, c1 - dc)
            antinode2 = (r2 + dr, c2 + dc)

            antinodes.add(antinode1)
            antinodes.add(antinode2)

    return antinodes


def resonant_freq(antennas):
    all_antinodes = set()

    for node, positions in antennas.items():
        if len(positions) >= 2:
            all_antinodes.update(find_antinode(positions))

    res = set()
    for antinode in all_antinodes:
        r, c = antinode
        if r in range(rl) and c in range(cl):
            res.add((r, c))

    return print(len(res))


resonant_freq(antennas)
