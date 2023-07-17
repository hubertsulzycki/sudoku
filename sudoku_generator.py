import random

# grid=[[0,0,0,0,0,0,0,0,0] for _ in range(9)]
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
    # print("finished")
    # printg(grid)
    # print("\n")
    for row in grid:
        for number in row:
            if number==0:
                return False
    return True

def check_input(grid,row,col,value):
    # print("check")
    # printg(grid)
    # print("\n")
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


def clear_numbers(grid):

    spots_to_clear=[[x,y] for x in range(9) for y in range(9)]
    random.shuffle(spots_to_clear)
    clear_grid=[[0,0,0,0,0,0,0,0,0] for _ in range(9)]

    for i, value in enumerate(spots_to_clear):

        if i<50:
            clear_grid[value[0]][value[1]]=0

        else:
            clear_grid[value[0]][value[1]]=grid[value[0]][value[1]]

    return clear_grid, spots_to_clear

def generate_grid():

    grid=[[0,0,0,0,0,0,0,0,0] for _ in range(9)]

    while not is_grid_finished(grid):        
        fill_grid(grid)

    gaming_grid, values_to_check =clear_numbers(grid)  

    return grid, gaming_grid, values_to_check


def printg(grid):

    for row in grid:
        print(row)
    print("\n")







            

