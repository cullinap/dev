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

# print_maze(maze)

def solve_maze(maze):
    if len(maze) < 1:
        return None
    if len(maze[0]) < 1:
        return None
    #print(string)
    return solve_maze_helper(maze, [], 0, 0)

iteration = 0

def solve_maze_helper(maze, solution, pos_row, pos_col):
    # first get size of the maze
    num_row = len(maze)
    num_col = len(maze[0])

    # print(pos_row, pos_col)

    # base case

    # if the robot already home? 
    if pos_row == num_row - 1 and pos_col == num_col - 1:
        print('finished', solution)
        return solution

    # if robot out of bounds
    if pos_row >= num_row or pos_col >= num_col:
        print('out of bounds', solution)
        return None

    # if robot on X obstacle
    if maze[pos_row][pos_col] == 'x':
        print('hit obstacle', solution)
        return None

    # recursive cases

    # try going right
    solution.append('r') 
    print('going to the right', solution)
    solution_right = solve_maze_helper(maze, solution, pos_row, pos_col + 1)

    # if you go right and it works
    if solution_right is not None:
        print('RIGHT', solution)
        return solution_right
    
    # if right does not work, backtrack and go down
    solution.pop()
    print('backing up', solution)
    solution.append('d')
    print('going down', solution)
    solution_down = solve_maze_helper(maze, solution, pos_row + 1,  pos_col)

    if solution_down is not None:
        print('DOWN', solution)
        return solution_down

    # if no solution backtrack
    print('backing up', solution)
    solution.pop()
    return None

solve_maze(maze)

"""
solve_maze(maze)
['d','d','r','r','d','r']
"""    










