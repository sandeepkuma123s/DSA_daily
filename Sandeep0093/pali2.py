# write a program to check if a array is a palindrome or not
def is_palindrome(arr):
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] != arr[right]:
            return False
        left += 1
        right -= 1
    return True
numbers = [1, 2, 3, 2, 1]
if is_palindrome(numbers):
    print("The array is a palindrome")
else:
    print("The array is not a palindrome")
    

    