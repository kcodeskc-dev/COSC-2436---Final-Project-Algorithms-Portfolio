# TODO 1 — Implement calculate_total_value
def calculate_total_value(solution, items):
    total = 0
    for name in solution:
        for item_name, weight, value in items:
            if item_name == name:
                total += value
                break
    return total

# PART 2 — Fill the DP Grid
def knapsack(items, capacity):
    n = len(items)
    grid = [[[] for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        item_name, weight, value = items[i - 1]
        for w in range(1, capacity + 1):
            if weight > w:
                # TODO 2 — This item is too heavy; copy the cell directly above.
                grid[i][w] = grid[i - 1][w][:]
            else:
                # TODO 3 — Build the two candidate solutions
                include_solution = grid[i - 1][w - weight][:] + [item_name]
                exclude_solution = grid[i - 1][w][:]
                
                # TODO 4 — Compute each candidate's dollar value
                include_value = calculate_total_value(include_solution, items)
                exclude_value = calculate_total_value(exclude_solution, items)

                # TODO 5 — Store whichever solution has the higher value
                if include_value > exclude_value:
                    grid[i][w] = include_solution
                else:
                    grid[i][w] = exclude_solution

    return grid

# PART 3 — Pretty-print the grid
def display_grid(grid, items):
    n = len(items)
    cell_width = 12

    # TODO 6 — Build the header row of capacity numbers
    header = ""
    for w in range(1, len(grid[0])):
        header += "{:>{width}}".format(str(w), width=cell_width)

    print(" " * cell_width + header)

    for i in range(1, n + 1):
        # TODO 7 — Start each data row with the item name
        row = "{:<{width}}".format(items[i - 1][0], width=cell_width)

        for cell in grid[i][1:]:
            if cell:
                # TODO 8 — Format non-empty cell
                letters = "".join(name[0] for name in cell)
                value = calculate_total_value(cell, items)
                row += "{:>{width}}".format(f"${value}({letters})", width=cell_width)
            else:
                # TODO 9 — Empty cells take cell_width chars
                row += " " * cell_width

        print(row)

# PART 4 — Run it
items = [
    ("GUITAR", 1, 1500),
    ("STEREO", 4, 3000),
    ("LAPTOP", 3, 2000),
    ("iPHONE", 1, 2000),
    ("BOOK", 2, 100),
    ("GOLD BAR", 1, 30000),
]

capacity = 6

# TODO 10 — Call knapsack(items, capacity) and store the result in `grid`.
grid = knapsack(items, capacity)

# TODO 11 — Uncomment to display the finished grid.
display_grid(grid, items)
