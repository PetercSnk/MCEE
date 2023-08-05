# the aim of this class is to use and understand 1d and 2d arrays

# a 1-dimensional array is a single array ([x, y, z])
# a 2-dimensional array is where you have arrays within an array ([[x1, y1, z1], [x2, y2, z2]])

# lets first use a 1d array
# the checkered grid is 10 blocks across, so our 1d array only needs to contain 10 elements
# we will fill our array with 0s and 1s where a 1 will signal that a block should be placed
# the idea is to use the array to plot a constellation

# example 1d array:
# array_1d = [0, 0, 0, 1, 0, 1, 0, 1, 0, 0]

# our 1d array only needs one for loop and one if statement
# first move your pet forward, if the element was a 0 move to the next element, if the element was a 1 place GLOWSTONE behind your pet

# useful commands:
# agent.set_slot(1)                         # sets what slot your pet will use
# agent.set_item(BLOCK_NAME, COUNT, SLOT)   # sets a slot in your pet to a block
# agent.move(direction, number_of_blocks)   # moves your pet in a direction, x amount of blocks
# agent.place(DIRECTION)                    # places the selected slot in a direction
# directions are UP, DOWN, LEFT, RIGHT, FORWARD, and BACK

# write your code here

# agent.set_slot(1)
# agent.set_item(GLOWSTONE, 64, 1)
# for x in array_1d:
#     agent.move(FORWARD, 1)
#     if x == 1:
#         agent.place(BACK)

# if we want to use the whole checkered grid we need to use a 2d array
# the implementation is similar to the 1d array but we now need 2 for loops
# the first loop selects each list, the second loop selects each element in that list 