# function that counts the number of vowels in a given string
def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = sum(1 for char in s if char in vowels)
    return count    
input_string = input("Enter a string: ")
vowel_count = count_vowels(input_string)
print(f"The number of vowels in the given string is: {vowel_count}")
print("vowel count")
