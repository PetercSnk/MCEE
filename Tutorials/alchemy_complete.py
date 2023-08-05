# the aim of this class is to understand binary and how to apply addition and shifts

# you should be familiar with the decimal system which is where we represent numbers using the symbols 0 to 9
# decimal is base 10 as we have 10 symbols (0 - 9)
# a number like 1234 has a 4 in the 10^0 (1) slot, 3 in the 10^1 (10) slot, 2 in the 10^2 (100) slot, and 1 in the 10^3 (1000) slot

# binary is base 2 as we only have 2 symbols, 0 and 1
# we do not represent numbers as 10^x, instead we represent them as 2^x
# this means our "slots" are 2^0 (1), 2^1 (2), 2^2 (4), 2^3 (8), 2^4 (16), 2^5 (32), and so on ...
# the binary number 1101 has 1 in the 2^0, 0 in the 2^1, 1 in the 2^2, and 1 in the 2^3
# this results in 1*1 + 0*2 + 1*4 + 1*8 = 13

# to add 2 binary numbers we can follow these rules:
# 0 + 0 = 0
# 1 + 0 = 1
# 1 + 1 = 0, carry the 1 over
# 1 + 1 + 1 = 1, carry the 1 over

# example:
# 0101 0011 +
# 0111 0110 =
# 1100 1001 
# 111  11  

# if extra help is needed go through the example here: https://www.bbc.co.uk/bitesize/guides/z26rcdm/revision/4

# shifts are simpler and just move all numbers either left or right
# as we are in base 2 a shift one place to the left mutiplies by 2, one shift to the right divides by 2

# example:
# 8  4  2  1 this is the "slot" the number is in
# 0  1  0  1 << shift 2 places to the left
# this is 5 in decimal

# 32  16  8  4  2  1
# 0   1   0  1  0  0
# as we are shifting 2 places to the left it we multiply by 4 which results in 20 in decimal, 5*4 = 20

# your turn to try now, use this area for workings
# when you know the answer use the black and white wool blocks to place it 
# black wool = 1, white wool = 0

# RED SECTION
# 010101 +
# 001101 = 
# 100010
#  1111

# YELLOW SECTION
# 011011 +
# 001011 =
# 100110
# 11 11

# PINK SECTION
# 000111 << shift 2 left (multiply by 4)
# 011100

# LIME SECTION
# 101000 >> shift 3 right (divide by 8)
# 000101