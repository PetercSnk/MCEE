# the aim of this class is to use and understand 1d and 2d arrays

# let's first use a 1d array
# a 1-dimensional array is a single array, [x, y, z]
# to get each element, only 1 for loop is needed

# use the following 1d array for task 1:

array_1d = [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]

# for each element in the array move forward
# if 0 do nothing, if 1 place glowstone behind
# teleport back to the start when you reach the end
# move first and place glowstone behind to not get stuck

# use the following commands:

# agent.set_slot(SLOT_NUM)                      # sets active slot to SLOT_NUM
# agent.set_item(BLOCK_NAME, COUNT, SLOT_NUM)   # puts n blocks in slot SLOT_NUM
# agent.move(DIRECTION, NUM_BLOCKS)             # moves a direction, n amount of blocks
# agent.place(DIRECTION)                        # places the active slot in direction
# start = world(-270, -28, 227)                 # start position
# agent.teleport(start, EAST)                   # teleports to start

# DIRECTIONS are UP, DOWN, LEFT, RIGHT, FORWARD, and BACK
# SLOT_NUM can be 1-27

# feel free to change the 1s and 0s in array_1d
# talk to Ranni to reset familiar and clear area

# write your code here for task 1:

agent.set_slot(1)
agent.set_item(GLOWSTONE, 64, 1)
for x in array_1d:
    agent.move(FORWARD, 1)
    if x == 1:
        agent.place(BACK)
start = world(-270, -28, 227)
agent.teleport(start, EAST)

# let's now try and use a 2d array
# a 2-dimensional array is an array within an array [[x1, y1, z1], [x2, y2, z2]]
# to get each element, 2 for loops are needed

# use one for loop to select each array
# use another for loop to select each element in the array
# for each element in the array move forward
# if 0 do nothing, if 1 place glowstone behind
# at the end of each array move to start of next row
# teleport back to the start once complete

# use the following 2d array
# don't change it as this is required to complete class

array_2d = [[1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]]  

# cut and paste your task 1 here, then edit for task 2:

agent.set_slot(1)
agent.set_item(GLOWSTONE, 64, 1)
for y in array_2d:
    for z in y:
        agent.move(FORWARD, 1)
        if z == 1:
            agent.place(BACK)
    agent.move(RIGHT, 1)
    agent.move(BACK, 10)
start = world(-270, -28, 227)
agent.teleport(start, EAST)