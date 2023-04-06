grid = [[6,7,5,3,0,4,2,0,1],
        [8,4,0,9,5,1,3,0,7],
        [0,0,9,0,0,0,8,0,5],
        [7,0,0,0,2,5,0,3,0],
        [0,0,6,0,0,0,0,0,4],
        [0,0,0,4,0,8,0,7,9],
        [0,6,3,0,4,9,0,0,0],
        [0,0,0,2,0,0,0,5,0],
        [4,2,0,0,0,0,0,0,3]]


def solve(grid):

    find = find_empty(grid)
    if not find:
        return True
    
    else:
        row,col = find
    
    for i in range(1,10):
        if valid(grid,i,(row,col)):
            grid[row][col] = i

            if solve(grid):
                return True
            
            grid[row][col] = 0

    return False
        






def valid(grid,num,pos):
    row,col = pos
    
    
    #check row
    for i in range(9):
        if grid[row][i] == num and col != i :
            return

    #check column 
    for i in range(9):
        if grid[i][col] == num and row != i :
            return
        
    #check square
    square_x = col // 3
    square_y = row  // 3
    
    for i in range(square_y*3,square_y*3+3):
        for j in range(square_x*3,square_x*3+3):
            if grid[i][j] == num and (i,j) != pos:
                return False   
     
    return True





def print_sudoku(grid):
    for i in range(9):

        if i ==3 or i ==6:
            print("--------------------")

        for j in range(9):
            if j%3 ==0:
                print("|",end="")
            if grid[i][j]==0:
                print(". ",end="")
            else:   
                print(grid[i][j],"",end="")
            
        print(" ")


def find_empty(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                return(i,j) #row, col
    return None

print_sudoku(grid)
solve(grid)
print("")
print("     A N S W E R")
print("")
print_sudoku(grid)