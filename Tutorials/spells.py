# the aim of this class is to use and understand input, processing, and output

# unfortunately we cannot use the input() command in minecraft
# use the variables below as your inputs instead

spell0 = "AlAkAzAm"         # output: "alakazam"
spell1 = "  baMzook  "      # output: "bamzook"
spell2 = " AbRa CadabrA  "  # output: "abracadabra"
spell3 = "abcd123-.,"       # output: "error" 

# process these inputs and say the output in game
# use the following commands:

# INPUT_STRING.to_lower_case()      # makes lowercase
# INPUT_STRING.trim()               # removes trailing and leading whitespace
# INPUT_STRING.replace("X","Y")     # replaces character X with character Y
# player.say("SAY_IN_GAME")         # says a string in game

# write your code here for task 1



# once you have managed that we can now command our familiar
# for each output, a certain block should be placed 

# "alakazam" requires BLACKSTONE, 2 blocks from start
# "bamzook" requires ICE, 5 blocks from start
# "abracadabra" requires DIAMOND_BLOCK, 11 blocks from start

# use if-elif-else to compare the processed input to expected output
# use these commands to control your familiar:

# agent.set_slot(SLOT_NUM)                      # sets active slot to SLOT_NUM
# agent.set_item(BLOCK_NAME, COUNT, SLOT_NUM)   # puts n blocks in slot SLOT_NUM
# agent.move(DIRECTION, NUM_BLOCKS)             # moves a direction, x amount of blocks
# agent.place(DIRECTION)                        # places the active slot in direction

# DIRECTIONS are UP, DOWN, LEFT, RIGHT, FORWARD, and BACK
# SLOT_NUM can be 1-27

# talk to Sellen to reset familiar and clear area

# write your code here for task 2


