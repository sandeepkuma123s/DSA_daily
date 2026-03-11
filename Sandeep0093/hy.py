# Input two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Euclid's algorithm
while b != 0:
    a, b = b, a % b

print(f"The GCD is {a}")
