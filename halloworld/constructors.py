# we use classes to define types of things eg strings dictionaries etc
# define a new type for example point
# when naming classes unlike variables and functions we capitalise the first
# letter instead of using an underscore eg EmailClient


# class Point:
#     def __init__(self, x, y):   #  constructor
#         self.x = x
#         self.y = y
#
#     def move(self):
#         print("move")
#
#     def draw(self):
#         print("draw")
#
#
# point = Point(10, 20)
# print(point.x)

#  create a type person should have a name attribute + a talk attribute
class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, I am {self.name}")


john = Person("john smith")
john.talk()

bob = Person("bobby")
bob.talk()
