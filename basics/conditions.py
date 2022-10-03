calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    # conditions are either true or false, otherwise known as Boolean data type
    print(num_of_days > 0) # this will print whether true or false
    condion_check = num_of_days > 0
    print(type(condion_check)) # type - inbuilt function that returns the data type
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"
    else:
        return "You entered negative value, no conversion for you"

user_input = input("Hey, enter a number of days and I'll convert them to hours: \n")
user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)
print(calculated_value)