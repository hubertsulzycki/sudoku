import random

# grid=[[0,0,0,0,0,0,0,0,0] for _ in range(10)]
grid=[]
grid.append([0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0])
grid.append([0,0,0,0,0,0,0,0,0])

def is_grid_finished(grid):
    for row in grid:
        for number in row:
            if number==0:
                return False
    return True

def check_input(grid,row,col,value):
    
    #row
    if value in grid[row]:
        #print("r")
        return False
        
    #col
    for r in grid:
        if r[col]==value:
            #print("c")
            return False

    #3x3 square
    square_array=[]
    if row<3:
        if col<3:
            square_array=[grid[x][y] for x in range(0,3) for y in range(0,3)]
        elif col<6:
            square_array=[grid[x][y] for x in range(0,3) for y in range(3,6)]
        else:
            square_array=[grid[x][y] for x in range(0,3) for y in range(6,9)]
    elif row<6:
        if col<3:
            square_array=[grid[x][y] for x in range(3,6) for y in range(0,3)]
        elif col<6:
            square_array=[grid[x][y] for x in range(3,6) for y in range(3,6)]
        else:
            square_array=[grid[x][y] for x in range(3,6) for y in range(6,9)]
    else:
        if col<3:
            square_array=[grid[x][y] for x in range(6,9) for y in range(0,3)]
        elif col<6:
            square_array=[grid[x][y] for x in range(6,9) for y in range(3,6)]
        else:
            square_array=[grid[x][y] for x in range(6,9) for y in range(6,9)]

    if value in square_array:
        #print("s")
        return False

    return True

def reset_grid(grid):
    for row in range(9):
        for col in range(9):
            grid[row][col]=0

def fill_grid(grid):
    reset_grid(grid)
    insertable_values=[1,2,3,4,5,6,7,8,9]
    for row in range(9):
        for col in range(9):
            random.shuffle(insertable_values)
            for value in insertable_values:
                if check_input(grid,row,col,value):
                    grid[row][col]=value
                    break

def generate_grid(grid):
    while not is_grid_finished(grid):
        fill_grid(grid)      

def printg(grid):
    for row in grid:
        print(row)
    print("--------------")

printg(grid)
generate_grid(grid)
printg(grid)

            

