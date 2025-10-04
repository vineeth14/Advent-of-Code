from process_input import get_input


# for every 'X' you do a dfs in every direction counting each 'XMAS'
# the dfs is interesting, you keep track of direction and you call it for each direction in the for loop not in the dfs
def word_search(grid):
    rl, cl = len(grid), len(grid[0])
    word = "XMAS"

    def dfs(r, c, dr, dc, idx):
        if (
            r not in range(rl)
            or c not in range(cl)
            or idx > len(word) - 1
            or grid[r][c] != word[idx]
        ):
            return False
        if idx == len(word) - 1:
            return True
        return dfs(r + dr, c + dc, dr, dc, idx + 1)

    count = 0
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
                  (0, 1), (1, -1), (1, 0), (1, 1)]
    for r in range(rl):
        for c in range(cl):
            if grid[r][c] == "X":
                for dr, dc in directions:
                    if dfs(r, c, dr, dc, 0):
                        count += 1
    print(count)


grid = get_input()
word_search(grid)
