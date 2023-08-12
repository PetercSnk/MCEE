# the aim of this class is to understand binary addition and shifts

# the decimal system represents numbers using the symbols 0 to 9
# decimal is base 10 as we have 10 symbols (0 - 9)
# the value of each place is calculated by multiplying by 10^N

# let's look at the number 1024

# thousands (1000s) column  = 1*10^3
# hundreds (100s) column    = 0*10^2
# tens (10s) column         = 2*10^1
# ones (1s) column          = 4*10^0

# add all these values up 1*1000 + 0*100 + 2*10 + 4*1 = 1024

# binary is base 2 as we only have 2 symbols, 0 and 1
# the value of each place is now calculated by multipling by 2^N

# let's look at the binary number 10101

# sixteens (16s) column     = 1*2^4
# eights (8s) column        = 0*2^3
# fours (4s) column         = 1*2^2
# twos (2s) column          = 0*2^1
# ones (1s) column          = 1*2^0

# add all these values up 1*16 + 0*8 + 1*4 + 0*2 + 1*1 = 21

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

# extra help here: https://www.bbc.co.uk/bitesize/guides/z26rcdm/revision/4

# shifts are simpler and just move all numbers either left or right
# 1 shift to the left mutiplies by 2
# 1 shift to the right divides by 2

# example with binary number 0101, or 5 in decimal:
# 8s  4s  2s  1s
# 0   1   0   1 

# shifted 2 places to the left is the following:
# 32s  16s  8s  4s  2s  1s
# 0    1    0   1   0   0
# 2 shifts to the left is the same as multiplying by 2 then 2 again (4)

# your turn to try now
# use the black and white wool to place your answers in the sections
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