# there are so many methods, you get this from python 3 module index on google

# import random

# for i in range(3):
#  #   print(random.random()) ---we generate a random number
#     print(random.randint(10, 20))
# make a list of team members and randomly pick one who will lead

import random
members = ["Bob", "Jayden", "Lincoln", "Sheldon", "Lucy", "Zion"]
leader = random.choice(members)
print(leader)