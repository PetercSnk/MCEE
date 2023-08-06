# the aim of this class is to use and understand linear search

# linear search involves searching through an array one value at a time until a chosen value is found

# example:
# let's say our array is [0, 1, 11, 6, 2], and our chosen value is 6
# we need to visit each element in our array until we find the value 6
# starting at the first element we compare 0 to 6 which is not a match
# when the values don't match you move onto the next element and make another comparison
# when a match is made you simply stop the process

# in this case our array will be the different coloured wool blocks on the floor
# each coloured wool block will have an ingredient assigned to it which you can collect to brew potions
# the chosen value will be the coloured wool block that has the ingredient you need
# to brew a potion follow one of the recipes located around the room

# using your pet you will need to traverse the coloured wool blocks and inspect and compare
# them to your chosen coloured wool block
# when a match is made, interact with the button to receive the ingredient and return your pet to the start

# first get your pet to traverse the coloured wool blocks and return to the start when it reaches the end
# useful commands:
# world(x, y, z)                            # specifies a position in the world
# agent.move(direction, number_of_blocks)   # moves your pet in a direction, x amount of blocks
# directions are UP, DOWN, LEFT, RIGHT, FORWARD, and BACK
# agent.teleport(position, direction)       # teleports your pet to a position facing NORTH, SOUTH, EAST or WEST
# the location you will want your pet to start at is x = -323, y = -53, z = 244, facing east
# remember to use a for loop with range(start, end)!

# speak to Tanith to clear the room and reset your pet 

# to complete this class you will need to brew a splash potion of strength 2
# write your code here
















# once that works we can implement our comparison
# before we move our pet we now want to inspect the block below
# we can do this with agent.inspect(AgentInspection.BLOCK, direction)
# this will provide us with the id of the block
# use this and a chosen id in an if statement to make the comparison
# the ids for all the blocks are:
# oak planks = 5, cobblestone = 4, sandstone = 24, quartz block = 155, lime concrete = 236, shroomlight = 766, bricks = 45, 
# hay bale = 170, purpur block = 201, redstone block = 152, glowstone = 89
# when a match is made you can interact using agent.interact(direction) and then break the loop
# edit the code you wrote above