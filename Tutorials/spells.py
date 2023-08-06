# the aim of this class is to use and understand input, processing, and output

# this concept of input-process-output (ipo) is where we take input from the user, process it in some way, and
# then display the output to the user

# unfortunately we cannot use the input() command in minecraft, so we will assign our input to a variable
# this input will be processed where the output will be a command that says the spell in game and moves your pet
# and places a block

# taking input from a user can lead to errors when we do not process it correctly
# people do not think the same and may try different variations of a single input, such as capitals, lowercase,
# or simply make a mistake

# write some code that takes one of the inputs below, processes it by removing whitespace and making it lowercase, 
# checks if it is a real spell, runs the correct command if it is, otherwise produce error message to user

# the only real spells are alakazam, bamzook, and abracadabra, anything that doesnt match these after processing
# should output an error message saying "incorrect"

# inputs
spell0 = "AlAkAzAm"         # alakazam
spell1 = "  baMzook  "      # bamzook
spell2 = "AbRa Cada brA"    # abracadabra
spell3 = "abcd123-.,"       # this should tell user it's incorrect, try your own strings to test

# useful commands:
# INPUT_STRING.lower()                      # makes lowercase
# INPUT_STRING.strip()                      # removes trailing and leading whitespace
# INPUT_STRING.replace("x","y")             # replaces character x with character y
# agent.set_slot(1)                         # sets what slot your pet will use
# agent.set_item(BLOCK_NAME, COUNT, SLOT)   # sets a slot in your pet to a block
# agent.move(direction, number_of_blocks)   # moves your pet in a direction, x amount of blocks
# agent.place(DIRECTION)                    # places the selected slot in a direction
# directions are UP, DOWN, LEFT, RIGHT, FORWARD, and BACK
# world(x, y, z)                            # specifies a position in the world
# agent.teleport(position, direction)       # teleports your pet to a position facing NORTH, SOUTH, EAST or WEST
# the location you will want your pet to start at is x = -267, y = -43, z = 244, facing north

# alakazam requires BLACKSTONE to be placed 2 blocks from the start
# bamzook requires ICE to be placed 5 blocks from the start
# abracadabra requires a DIAMOND_BLOCK to be placed 11 blocks from the start

# speak to Sellen to clear the room and reset your pet 

# to complete this class you will need to place all 3 blocks
# write your code here



















