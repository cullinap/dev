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

def solve_maze_helper(maze, sol, pos_row, pos_col):
    # first get size of the maze
    num_rows = len(maze)
    num_cols = len(maze[0])

    print(num_rows, num_cols)

    # fi the robot already home? 

solve_maze_helper(maze, 0, 0, 0)    


"""
solve_maze(maze)
['d','d','r','r','d','r']
"""    










