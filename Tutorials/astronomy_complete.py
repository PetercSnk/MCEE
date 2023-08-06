# the aim of this class is to use and understand 1d and 2d arrays

# a 1-dimensional array is a single array ([x, y, z])
# a 2-dimensional array is where you have arrays within an array ([[x1, y1, z1], [x2, y2, z2]])

# lets first use a 1d array
# the checkered grid is 10 blocks across, so our 1d array only needs to contain 10 elements
# we will fill our array with 0s and 1s where a 1 will signal that a block should be placed
# the idea is to use the array to plot a constellation

# our 1d array only needs one for loop and one if statement
# first move your pet FORWARD, if the element was a 0 move to the next element, if the element was a 1 place GLOWSTONE behind your pet
# we want to move our pet FORWARD initially as it'll get stuck if we place the block then move

# useful commands:
# world(x, y, z)                            # specifies a position in the world
# agent.teleport(position, direction)       # teleports your pet to a position facing NORTH, SOUTH, EAST or WEST
# agent.set_slot(1)                         # sets what slot your pet will use
# agent.set_item(BLOCK_NAME, COUNT, SLOT)   # sets a slot in your pet to a block
# agent.move(direction, number_of_blocks)   # moves your pet in a direction, x amount of blocks
# agent.place(DIRECTION)                    # places the selected slot in a direction
# directions are UP, DOWN, LEFT, RIGHT, FORWARD, and BACK
# the location you will want your pet to start at is x = -270, y = -28, z = 227, facing east

# set your pet up at the start
# set a slot and make it GLOWSTONE
# for each element in the 1d array move FORWARD
# if it is a 1 place GLOWSTONE behind your pet

# example 1d array below

array_1d = [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]

# write your code here

start = world(-270, -28, 227)
agent.teleport(start, EAST)
agent.set_slot(1)
agent.set_item(GLOWSTONE, 64, 1)
for element in array_1d:
    agent.move(FORWARD, 1)
    if element == 1:
        agent.place(BACK)

# if we want to use the whole checkered grid we need to use a 2d array
# the implementation is similar to the 1d array but we now need 2 for loops
# the first loop selects each array, the second loop selects each element in each array

# set your pet up at the start
# set a slot and make it GLOWSTONE
# use one for loop to select each array and one for loop to select each element
# for each element in each array move FORWARD
# if it is a 1 place GLOWSTONE behind your pet
# after completing a full loop of each array move your pet to the start of the next row

# to complete the lesson your pet will need to successfully plot the 2d array below

array_2d = [[0, 0, 0, 1, 0, 1, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]    

# write your code here

start = world(-270, -28, 227)
agent.teleport(start, EAST)
agent.set_slot(1)
agent.set_item(GLOWSTONE, 64, 1)
for array in array_2d:
    for element in array:
        agent.move(FORWARD, 1)
        if element == 1:
            agent.place(BACK)
    agent.move(RIGHT, 1)
    agent.move(BACK, 10)