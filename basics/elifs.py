# multiple if statements ie elif
# one can use as many elif statements with different conditions
# elif has a condition while else doesn't

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
    
    if num_of_days > 0:
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

    elif num_of_days == 0:
        return "You entered a zero, please enter a positive valid number"

    else:
        return "You entered negative value, no conversion for you"

user_input = input("Hey, enter a number of days and I'll convert them to hours: \n")

user_input_number = int(user_input)

calculated_value = days_to_units(user_input_number)

print(calculated_value)