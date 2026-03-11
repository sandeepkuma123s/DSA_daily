num = int(input("Enter a number: "))
digits = [int(d) for d in str(num)]
power = len(digits)
total = sum(d ** power for d in digits)

if total == num:
    print(f"{num} is an Armstrong number.")
else:
    print(f"{num} is not an Armstrong number.")
