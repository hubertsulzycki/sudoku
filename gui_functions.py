import sudoku_generator as sg


def fill_entries(entries,gaming_grid):
    for x in range(9):
        for y in range(9):
            if gaming_grid[x][y]!=0:
                entries[x][y].insert(0,f"{gaming_grid[x][y]}")
                entries[x][y].config(state="disabled", disabledbackground="lightgray", fg="red")