# Calculate Average From File
'''
Assume that a file containing a series of integers is named numbers.txt.
Write a program that calculates the average of all the numbers stored in
the file and prints the average to the screen.
'''


file = open('numbers.txt', 'r')

sum = 0
count = 0
for line in file:
    sum += int(line)
    count += 1

print(sum / count)
