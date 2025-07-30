def count_xmas_shapes(grid):
    count = 0
    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            # Extract diagonals
            diag1 = grid[i][j] + grid[i+1][j+1] + grid[i+2][j+2]
            diag2 = grid[i][j+2] + grid[i+1][j+1] + grid[i+2][j]
            if diag1 in {"MAS", "SAM"} and diag2 in {"MAS", "SAM"}:
                count += 1
    return count

with open("lvl4.txt") as f:
    grid = [line.strip() for line in f]

print(count_xmas_shapes(grid))
