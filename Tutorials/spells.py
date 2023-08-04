# the aim of this class is to use and understand input, processing, and output

# this concept of input-process-output (ipo) is where we take input from the user, process it in some way, and
# then display the output to the user

# unfortunately we cannot use the input() command in minecraft, so we will assign our input to a variable
# this input will be processed where the output will be a command that says the spell in game and moves your pet
# and places a block

# taking input from a user can lead to errors when we do not process it correctly
# people do not think the same and may try different variations of a single input, such as capitals, lowercase,
# or simply make a mistake

# write a function that takes one of the following inputs, processes it into a single lowercase string and
# outputs the correct command

# the only real spells are alakazam, bamzook, and abracadabra, anything that doesnt match these after processing
# should output an error message saying "incorrect spell"

# alakazam
# bamzook
# abracadabra

# inputs
spell0 = "AlAkAzAm"         # alakazam
spell1 = "  baMzook  "      # bamzook
spell2 = "AbRa Cada brA"    # abracadabra
spell3 = "abcd123-.,"       # this should tell user it doesnt exist, try your own strings to test

# useful commands:
# INPUT_STRING.lower() # makes lowercase
# INPUT_STRING.strip() # removes trailing and leading whitespace
# INPUT_STRING.replace("x","y") # replaces character x with character y

# write your code here
