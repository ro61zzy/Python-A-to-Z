# numbers = [5, 2, 1, 7, 4]
# numbers.insert(0,20) # you cn use different
# numbers.pop()removes the last number on a list
# .index(8)checks for the existence of a number in a list
# .count(5)checks the number on a list
# .sort/reverse    do nt print it call it
# .copy takes a copy
# print(numbers)
# write a program to remove the duplicate a list

numbers = [4,3,2,4,6,4,6,8,5,2,5,5,4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)

