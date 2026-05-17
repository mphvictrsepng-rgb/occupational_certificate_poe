
# 1.1 - Convert 0xFA from hex to binary
binary_fa = "11111010"             # 0xF = 1111 and 0xA = 1010, so combined gives 11111010 in binary

# 1.2 - The base-10 symbol for the binary number 1001
symbol_1001 = 9               # 1*2^3 + 0*2^2 + 0*2^1 + 1*2^0 = 8 + 0 + 0 + 1 = 9

# 1.3 - Convert the binary groups into hexadecimal
hex_1 = "C0DE"  # 11000000 11011110, where C = 1100, 0 = 0000, D = 1101, E = 1110
hex_2 = "BEF"   # 10111110 11101111 , where B = 1011, E = 1110, F = 1111
hex_3 = "F0D"   # 11110000 00001101 , where F = 1111, 0 = 0000, D = 1101

# Print the answers for easy checking
print("1.1 - 0xFA in binary:", binary_fa)
print("1.2 - 1001 in base-10:", symbol_1001)
print("1.3 - Hex values:", hex_1, hex_2, hex_3)
