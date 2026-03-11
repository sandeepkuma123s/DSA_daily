# write a program to remove duplicates from array
def remove_duplicates(arr):
    seen = set()
    result = []
    for number in arr:
        if number not in seen:
            seen.add(number)
            result.append(number)
    return result
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = remove_duplicates(numbers)
print("Array after removing duplicates:", unique_numbers)