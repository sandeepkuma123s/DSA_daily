# Two sum problem 
# Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to the target.
# Input:
# nums = [2,7,11,15]
# target = 9
# nums = [2,7,11,15]
# target = 9



# Algorithm

# Start with the list nums.

# Use a loop to pick the first number.

# Use another loop to pick the second number.

# Check if the sum of both numbers equals the target.

# If yes, print their indices

for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i] + nums[j] == target:
            print(i,j)