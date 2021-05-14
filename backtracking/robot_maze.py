# base cases
# if the robot is home the return current solution
# if robot is out of bounds no solution
# if robot on X obstacle no solution

# recursive cases
# solve for the subproblem if the robot goes right
# return the solution if the sub problem is solvable
# if not backtrack
# solve for the subproblem if the roboto goes down
# return the solution if the sub problem is solvable
# if not backtrack

# states
# maze
# pos of robot
# solution

maze = [[",",".",".","."],
        [",","x","x","x"],
        [".",".",",","x"],
        ["x","x",",","."]]

def print_maze(maze):
    for row in maze:
        row_print = ""
        for value in row:
            row_print += value + " "
        print(row_print)    

print_maze(maze)

def solve_maze(maze):
    return

def solve_maze_helper(maze, solution, pos_row, pos_col):
    # first get size of the maze
    num_row = len(maze)
    num_col = len(maze[0])

    # base case

    # if the robot already home? 
    if pos_row == num_row - 1 and pos_col == num_col - 1:
        return solution

    # if robot out of bounds
    if pos_row >= num_row or pos_col >= num_col:
        return None

    # if robot on X obstacle
    if maze[pos_row][pos_col] == 'x':
        return None

    # recursive cases


solve_maze_helper(maze, 0, 0, 0)    


"""
solve_maze(maze)
['d','d','r','r','d','r']
"""    










