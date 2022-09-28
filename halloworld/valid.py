# if name is less than 3 characters long : name must be at least 3 characters
# Otherwise if it's more than 50 characters long  name can be a maximum of 50 characters
# Otherwise name looks good

name = "jtretryuiohjgffhoiuytreesdhjlkjhgf"
if len(name) < 3:
    print("Name must be at least three characters")
elif len(name) > 50:
    print("Name must be a maximum of 50 characters")
else:
    print("Name looks good!")

