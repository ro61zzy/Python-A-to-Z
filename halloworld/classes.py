# we use classes to define types of things eg strings dictionaries etc
# define a new type for example point
# when naming classes unlike variables and functions we capitalise the first
# letter instead of using an underscore eg EmailClient


class Point:
    def move(self):
        print("move")

    def draw(self):
        print("draw")


point1 = Point()
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

point2 = Point()
point2.x = 1 
print(point2.x)