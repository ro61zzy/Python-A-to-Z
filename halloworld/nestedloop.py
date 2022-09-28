# we run the first loop first and then the second one but the second one must run first to end
# so as to go back to the first one
# iterations


for x in range(4):
    for y in range(3):
        print(f"({x},{y})")
