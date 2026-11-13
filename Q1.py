#DSA2, Question 1
#Kanza Mohammad Babar Naveed

import random
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# loading maze image
maze_image = mpimg.imread("maze.png")

# Creating 21x21 grid 
maze = np.zeros((21, 21), dtype=int)

#pixel dimension 
cell_height = maze_image.shape[0] // 21
cell_width = maze_image.shape[1] // 21

# taking the centre pixel 
for row in range(21):
    for col in range(21):
        pixel = maze_image[row * cell_height + cell_height // 2,col * cell_width + cell_width // 2]

        if pixel[0] > 0.5:
            maze[row,col] = 0  # 0 represents white
        else:
            maze[row,col] = 1  # 1 is for black i.e. wall

# Representing maze as 0s and 1s in output terminal
print("Maze grid (0 = clear path, 1 = wall):")
for row in maze:
    print(" ".join(str(cell) for cell in row))

# Maze visualization through matplotlib 
plt.figure(figsize=(6,6))
plt.imshow(maze, cmap="binary")
plt.title("21 x 21 Maze Grid")
plt.xticks(range(21))
plt.yticks(range(21))
plt.show()


# Find the entrance and exit
Entrance = (0, int(np.where(maze[0] == 0)[0][0]))
Exit = (20, int(np.where(maze[20] == 0)[0][0]))
print("Entrance position:", Entrance)
print("Exit position:", Exit)

# Possible movements: down, right, left and up
moves = {"down": (1, 0),"right": (0, 1),"left":(0, -1),"up":(-1, 0)}

maze[1,1]

# Checking if a position is a valid path
def Check_movement__is_valid(position):
    row, col= position
    # Checking  the boundaries
    if row <0 or row >=21 or col <0 or col >=21:
        return False
    # Checking if the square is a wall
    if maze[row, col] == 1:
        return False
    return True


#**************Functions for Algorithms******************

#Function for Las Vegas algorithm 
def las_vegas_algorithm():
    current =Entrance
    visited_las ={current}
    walk =[current]
    steps = 0

    # Continue until exit is found or 200 steps are completed
    while current != Exit and steps< 200:

        possible_moves =[]
        # Check all four allowed directions
        for change in moves.values():
            new_position = (
                current[0] + change[0],
                current[1] + change[1])

            if Check_movement__is_valid(new_position):
                possible_moves.append(new_position)

        # Randomly choose a valid direction
        current  = random.choice(possible_moves)
        walk.append(current)
        visited_las.add(current)
        steps  += 1

    # Check if the exit was reached
    success = current== Exit

    return success,  walk, visited_las, steps


# For backtracking, Store all visited positions
visited = np.zeros((21, 21), dtype=bool)

# Store the successful route
path = []

# function for Backtracking algorithm
def backtracking_algorithm(position):

    # Save current square as visited
    row, col = position
    visited[row, col] = True
    path.append(position)

    # Check if  exit reacched
    if position ==Exit:
        return True

    # Try each direction in our chosen order
    for direction, change in moves.items():

        new_position = (position[0] + change[0],position[1] + change[1])

        # Move only if the square is valid and unvisited
        if Check_movement__is_valid(new_position) and not visited[new_position]:
            if backtracking_algorithm(new_position):
                return True
    # If path did not work,  go backwards
    path.pop()
    return False


#**************Asking User and Running the program******************

#Ask user which algorithm they want
print("\n ********* MAZE SOLVER PROGRAM DSA2 Question 1 ***********")
print("1 = Las Vegas")
print("2 = Backtracking")

chosen_algorithm = input("Choose an algorithm (1 or 2): ").strip()

# Run based on selection
if chosen_algorithm == "1":
    print("You chose Las Vegas!! Let's gooo")
    success, walk, visited_las, steps = las_vegas_algorithm()
    if success:
        print("Exit found!")
    else:
        print("Exit not found within 200 steps.")

    print("Total steps:", steps)
    print("Unique squares visited:", len(visited_las))

    # Creating Las Vegas visualisation
    display_lasVegas = np.ones((21, 21, 3))
    display_lasVegas[maze ==1] = [0, 0, 0]

    for row, col in visited_las:
        display_lasVegas[row, col] = [0.55, 0.36, 0.96]

    if success:
        for row, col in walk:
            display_lasVegas[row, col] = [0.2, 0.8, 0.60]

    display_lasVegas[Entrance] = [0.22, 0.74, 0.97]
    display_lasVegas[Exit] = [1, 1, 0]

    plt.figure(figsize=(8,8))
    plt.imshow(display_lasVegas)
    plt.title("Las Vegas")
    plt.xticks(range(21))
    plt.yticks(range(21))
    plt.show()


elif chosen_algorithm == "2":
    print("\n You chose Backtracking! Let's Goooo")

    # remove previous results to avoid errors 
    visited[:] = False
    path.clear()
    success = backtracking_algorithm(Entrance)
    
    if success:
        print("Maze solved successfully!")
        print("Successful path: ", path)
    else:
        print("Solution not Found.")

    print("Total visited squares: ", np.sum(visited))

    # Creating Backtracking visualisation
    display = np.ones((21, 21,3))
    display[maze == 1] = [0, 0, 0]
    display[visited] = [0.55, 0.36, 0.96]

    for row, col in path:
        display[row, col] = [0.2, 0.8, 0.2]

    display[Entrance
            ] = [1, 0, 0]
    display[Exit] = [1, 1, 0]
    plt.figure(figsize=(8, 8))
    plt.imshow(display)
    plt.title("Backtracking Visual Visited Squares and Final Path")
    plt.xticks(range(21))
    plt.yticks(range(21))
    plt.show()

else:
    print("Choice is not Valid. Please enter 1 or 2.")


#**************Testing 10,000 runs ******************

total_runs = 10000

# Testing Backtracking 10000 times
backtracking_successes = 0

for i in range(total_runs):
    # Reset the visited squares and path
    visited[:] = False
    path.clear()
    if backtracking_algorithm(Entrance):
        backtracking_successes += 1

backtracking_rate = (backtracking_successes / total_runs) * 100


# Test Las Vegas 10000 times 
las_vegas_successes = 0
for i in range(total_runs):
    success, walk, visited_las, steps = las_vegas_algorithm()
    if success:
        las_vegas_successes += 1

las_vegas_rate = (las_vegas_successes/total_runs) * 100


# Display results
print("*********||||||||SUCCESS RATE COMPARISON ||||||||*********\n")
print("Total runs for both programs = \n", total_runs)

print("Backtracking Successful runs= ", backtracking_successes)
print("Backtracking Success rate= \n ", backtracking_rate, "%")


print("Las Vegas Successful runs=", las_vegas_successes)
print("Las Vegas Success rate=", las_vegas_rate, "%")



