# lvl4.py
def read_grid(filename):
    with open(filename, "r") as f:
        return [line.strip() for line in f.readlines()]

def count_xmas(grid):
    rows = len(grid)
    cols = len(grid[0])
    word = "XMAS"
    word_len = len(word)
    total = 0

    # directions: (dy, dx)
    directions = [
        (0, 1),   
        (0, -1),  
        (1, 0),   
        (-1, 0),  
        (1, 1),   
        (-1, -1), 
        (1, -1),  
        (-1, 1),  
    ]

    for y in range(rows):
        for x in range(cols):
            for dy, dx in directions:
                match = True
                for i in range(word_len):
                    ny = y + i * dy
                    nx = x + i * dx
                    if not (0 <= ny < rows and 0 <= nx < cols):
                        match = False
                        break
                    if grid[ny][nx] != word[i]:
                        match = False
                        break
                if match:
                    total += 1
    return total

# --- main ---
grid = read_grid("lvl4.txt")
result = count_xmas(grid)
print(result)
