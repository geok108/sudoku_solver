import numpy as np

# Load sudokus
sudokus = np.load("sudokus.npy")
print("Shape of sudokus array:", sudokus.shape, "; Type of array values:", sudokus.dtype)

# Load solutions
solutions = np.load("solutions.npy")
print("Shape of solutions array:", solutions.shape, "; Type of array values:", solutions.dtype, "\n")

# Print the first sudoku...
print("Sudoku #1:")
print(sudokus[0], "\n")

# ...and its solution
print("Solution of Sudoku #1:")
print(solutions[0])


def sudoku_solver(sudoku):
    """
    Solves a Sudoku puzzle and returns its unique solution.

    Input
        sudoku : 9x9 numpy array of integers
            Empty cells are designated by 0.

    Output
        9x9 numpy array of integers
            It contains the solution, if there is one. If there is no solution, all array entries should be -1.
    """
   
    #calls the solver and checks whether the sudoku is solved or not
    if solver(sudoku):
        print("solved")
        print(sudoku)
        return sudoku
    else:
        #if the sudoku is unsolvable it fills all the squares with -1
        for row in range(0,9):
            for col in range(0,9):
                sudoku[row,col] = -1
        print("unsolvable")
        print(sudoku)
        return sudoku
        
            
def solver(sudoku):
    if is_completed(sudoku):
        return True
    for row in range(0,9):
        for col in range(0,9):
            if sudoku[row,col]==0:
                for value in range(1,10):
                    
                    #checks whether there are any collissions of the proposed value in row, col or block
                    if check_row(row, value, sudoku) \
                    and check_col(col, value, sudoku) \
                    and check_block(row, col, value, sudoku):
                            #assign value if there are no collissions
                            sudoku[row,col] = value
                            
                            
                            if is_completed(sudoku):
                                return True
                            #fill the rest of the array recursively
                            if solver(sudoku):
                                return True
                            
                            #assign zero and try again
                            sudoku[row,col] = 0 
                #if no value can be placed then do backtracking
                return False
  
#checks whether sudoku is completed
def is_completed(sudoku):
    
    for row in range(0,9):
        for col in range(0,9):
            if sudoku[row,col]==0 or sudoku[row,col]==-1:
                return False
    return True
 
#checks whether there are same values in row           
def check_row(row, value, sudoku):
     for i in range(0, len( sudoku ) ):
        if value == sudoku[row, i]:
            return False
     return True
           
#checks whether there are same values in column   
def check_col(col, value, sudoku):
    for i in range(0, len( sudoku ) ):
        if value == sudoku[i, col]:
            return False
    return True

#checks whether there are same values in 3x3 square
def check_block(row, col, value, sudoku):
    block_row = row - row % 3
    block_col = col - col % 3
    
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[block_row + i, block_col + j] == value:
                return False
    return True
