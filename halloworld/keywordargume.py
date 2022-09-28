# def greet_user(first_name, last_name):
#     print(f"hi welcome {first_name} {last_name}!")
#     print("make yourself at home..")
#
#
# print("start")
# greet_user(last_name="smith", first_name="john")  # the key word arguments are supplied to clarify the position
# print("finish")

def greet_user(first_name, last_name):  # name is a parameter
    print(f"hi welcome {first_name} {last_name}!")
    print("make yourself at home..")


#  keyword arguments
print("start")
greet_user("john", "smith")  # john is an argument
#  calc_cost(50, 5, 0.1)----someone reading this will not understand
#  use keyword argument to improve the readability of the code
#  calc_cost(total=50, shipping=5, discount=0.1)-----now this is understandable
print("finish")

#  if you decide to mix both position and keyword arguments you should always use
#  the positional one infront of keyword or you"ll get an error