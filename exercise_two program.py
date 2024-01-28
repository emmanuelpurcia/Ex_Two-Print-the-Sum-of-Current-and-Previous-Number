# Hello! This python program prints the sum of the current and previous given number.

# pseudocode

# Write a program to iterate the first 10 numbers
numbers_given_in_range = [0,1,2,3,4,5,6,7,8,9,10,]

# In each iteration, print the sum of the current and previous number
print('And now, we will show the sum of the current and previous number. Here we go!:')
for i in range (10):
    numbers_given_in_range_current = numbers_given_in_range[i]
    numbers_given_in_range_previous = numbers_given_in_range[i+1]
    numbers_given_in_current_and_previous_sum = int(numbers_given_in_range_previous) + int(numbers_given_in_range_current)
    print('The current number is ',numbers_given_in_range_current,' while the previous number is ',numbers_given_in_range_previous,' therefore their sum would be ',numbers_given_in_current_and_previous_sum)

