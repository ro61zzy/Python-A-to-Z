# a module is a file with some code
# we use them to organize our code
# for example we can create a separate file for
# use in conversions in every where converters.

# import converters
# from coverters import kg_to_lbs
#
# kg_to_lbs(100)
#
# print(converters.kg_to_lbs(70))

########
# numbers = [3, 5, 6, 8, 2, 4, 9]
# max = numbers[0]
# for number in numbers:
#     if number > max:
#         max = number
# print(max)
#
# create the same but organized programme


from utilities import find_max

numbers = [3, 5, 6, 8, 2, 4, 9]
maximum = find_max(numbers)
print(maximum)