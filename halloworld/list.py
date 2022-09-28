# names = ["bob", "jede", "shelo", "lucy", "zion"]
# print(names[1:4])

# write a program to find the largest number in a list
numbers = [3, 5, 6, 8, 2, 4, 9]
max = numbers[0]
for number in numbers:
    if number > max:
        max = number
print(max)