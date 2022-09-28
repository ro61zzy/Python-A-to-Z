from pathlib import Path
# we have diff paths
# an absolute path you start from the local disk
# relative path start from the current to somewhere else

###
# path = Path("ecommerce")
# print(path.exists()) # checks if the path exists

# path = Path("email")
# print(path.exists()) # since we dont have such a directory we automatically create it
# by adding mkdir for make directory or rmdir to remove directory

####
# path = Path("email")
# print(path.rmdir())
# we can also use this to look for files in the same path of directory by use of glob("* to mean all
path = Path()
for file in path.glob("*.py"): # to look for all py files in the directory
    print(file)