#factorial using while loop
num = int(input("Enter a number: "))        
factorial = 1   

if num < 0:
    print("Factorial is not defined for negative numbers.")
elif num == 0 or num == 1:
    print(f"The factorial of {num} is 1.")  