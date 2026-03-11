# write a program to find number of  duplicate in an array
def count_duplicates(arr):
    count_map = {}
    for number in arr:
        if number in count_map:
            count_map[number] += 1
        else:
            count_map[number] = 1
    duplicate_count = sum(1 for count in count_map.values() if count > 1)
    return duplicate_count
numbers = [1, 2, 2, 3, 4, 4, 5]
duplicates = count_duplicates(numbers)
print(f"The number of duplicate elements in the array is: {duplicates}")

