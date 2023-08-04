# the aim of this class is to use and understand linear search

# linear search involves searching through an array one value at a time until a chosen value is found

# example:
# let's say our array is [0, 1, 11, 6, 2], and our chosen value is 6
# we need to visit each element in our array until we find the value 6
# comparing the first element 0 to 6 is not a match
# when the values don't match you move onto the next element and make another comparison
# when a match is made you simply stop the process

# in this case our array will be the different coloured wool blocks on the floor
# and you will choose a coloured wool block that has the ingredient you need on it

# using your pet you will need to traverse the coloured wool blocks and inspect and compare
# them to your chosen coloured wool block
# when a match is made retrieve the ingredient from the container and return your pet to the start

# first get your pet to traverse each coloured wool block and return to the start when it reaches the last one
# useful commands:
# pos(x, y, z) - specifies a position in the world
# agent.move(direction, number_of_blocks) - moves your pet in a direction, x amount of blocks
# directions are UP, DOWN, LEFT, RIGHT, FORWARD, and BACK
# agent.teleport(position, direction) - teleports your pet to a position facing NORTH, SOUTH, EAST or WEST
# remember to use a for loop!

# write your code here

# start = pos(x, y, z)
# for index in range(0, coloured_wool_blocks_length):
#     if agent.inspect(AgentInspection.BLOCK, DOWN) == chosen_coloured_wool_block:
#         agent.interact(RIGHT)
#         break
#     agent.move(FORWARD, 1)
# agent.teleport(start)

# once that works we can implement our comparison
# before we move our pet we now want to inspect the block below
# we can do this with agent.inspect(AgentInspection.BLOCK, direction)
# this will provide us with the name of the block
# use this and our chosen coloured wool block in an if statement to make the comparison
# when a match is made you can interact using agent.interact(direction) and then break the loop
# edit the code you wrote above
