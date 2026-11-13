#DSA 2 Question 3
#Kanza Mohammad Babar Naveed 

import random
def follow_instructions(instructions: list[str]) -> list[int]:

    index_visited = []
    #This recursive function will follow the given instructions for colors.
    def do_instructions(index):
        if index < 0 or index >= len(instructions):
            return
        index_visited.append(index)
        color = instructions[index]

        if color == "blue":
            #using the try block here to handle if there is no next blue
            try:
                next_blue = instructions.index("blue", index + 1)
                next_index = next_blue + 1
            except ValueError:
                return
        elif color == "red":
            next_index = 2 * index + 1
        elif color == "green":
            next_index = index + 1
            
        do_instructions(next_index)
        
    if instructions:
        do_instructions(0)
    return index_visited

# First test ---> using the given list.
instructions = ["blue", "green", "red", "blue", "green", "red"]
print("\nIndex visited ", follow_instructions(instructions))

# Second test ---> with two generated listst 
colors = ["blue", "red", "green"]

for second_test in range(2):
    instructions = [random.choice(colors) for _ in range(15)]

    print("\nGenerated list:- ", instructions)
    print("Visited indexes :-", follow_instructions(instructions))


