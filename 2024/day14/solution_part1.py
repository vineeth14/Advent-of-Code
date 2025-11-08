# After 100 seconds, calculate each robot's final position with wraparound (mod 101x103).
# Divide grid into 4 quadrants (ignoring middle row/column at x=50, y=51).
# Safety factor = product of robot counts in each quadrant.
from process_input import get_input
from collections import defaultdict

robot_positions = get_input()

final_quads = defaultdict(list)


def process_positions(robot_position):
    coords, velocity = robot_position
    velocity = velocity
    x, y = coords
    v1, v2 = velocity

    x_coord = (x + v1 * 100) % 101
    y_coord = (y + v2 * 100) % 103

    if y_coord == 51 or x_coord == 50:
        return

    if x_coord < 50:  # Top half
        if y_coord < 51:
            final_quads[1].append((x_coord, y_coord))
        else:
            final_quads[2].append((x_coord, y_coord))
    else:
        if y_coord < 51:
            final_quads[3].append((x_coord, y_coord))
        else:
            final_quads[4].append((x_coord, y_coord))


for position in robot_positions:
    process_positions(position)

ans = 1
for v in final_quads.values():
    ans *= len(v)
print(ans)
