# use bitwise operators to set, clear, and toggle bits of an integer
num = 29  # binary: 11101   
print("Original number:", num)
# Set the 2nd bit (counting from 0)
set_bit = num | (1 << 2)

print("After setting 2nd bit:", set_bit)  # binary: 11101 | 00100 = 11101 (29)
# Clear the 3rd bit 
clear_bit = num & ~(1 << 3)
print("After clearing 3rd bit:", clear_bit)  # binary: 11101
# Toggle the 0th bit
toggle_bit = num ^ (1 << 0)
print("After toggling 0th bit:", toggle_bit)  # binary: 11101 ^ 00001 = 11100 (28)
print("bitwise operations")
    