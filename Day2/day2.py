import math
import numpy as np
import pandas as pd

# Part 1:
def execute_commands_part1(initial_position=[0,0,0],commands=[]):
    current_position = initial_position
    for command in commands:
        if command[0] == 'forward':
            current_position[0] += int(command[1])
        elif command[0] == 'backward':
            current_position[0] -= int(command[1])
        elif command[0] == 'up':
            current_position[1] -= int(command[1])
        elif command[0] == 'down':
            current_position[1] += int(command[1])
        else:
            pass
        print(current_position)
    return current_position

# Part 2
def execute_commands_part2(initial_position=[0,0,0],commands=[]):
    current_position = initial_position
    for command in commands:
        if command[0] == 'forward':                                           # forward X does two things
            current_position[0] += int(command[1])                            # increases horizontal by X
            # Added this line for part 2, and expanded the position list size to account for 'aim' tracking
            current_position[1] += int(current_position[2]) * int(command[1]) # increases depth by aim multiplied by X
        elif command[0] == 'backward':
            current_position[0] -= int(command[1]) # horizontal
        elif command[0] == 'up':
            current_position[2] -= int(command[1]) # up X decreases your aim by X
        elif command[0] == 'down':
            current_position[2] += int(command[1]) # down X increases your aim by X
        else:
            pass
        print(current_position)
    return current_position

###############################################################
# ----------------------------------------------------------- #
###############################################################


# Get input data
#filepath = ".\Day2\input.txt"
filepath = ".\Day2\sample.txt"
commands = open(filepath).read().split("\n")
commands = [command.split(" ") for command in commands]
pos = [0,0,0]

# Part 1a: Using standard Python
pos = execute_commands_part1(pos, commands)
ans = math.prod(pos[:-1])
print(ans)
'''
# Part 1b: Using numpy / pandas
commands_df = pd.read_csv(filepath, delimiter=" ",header=None)
mask = (commands_df[0] == 'backward') | (commands_df[0] == 'up') 
commands_df.loc[mask,1] = -1*commands_df[1]
change_map = {'forward':'horizontal', 'backward':'horizontal', 'down':'vertical','up':'vertical'}
commands_df[0] = commands_df[0].map(change_map)
ans2 = math.prod(commands_df.groupby([0]).sum()[1].values) 
print(ans2)
'''
# Part 2:
pos = [0,0,0]
pos = execute_commands_part2(pos, commands)
ans = math.prod(pos[:-1])
print(ans)