# nested if statements, if inside if

calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_n_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_units(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print ("You entered a zero, please enter a positive valid number")
    else:
        print("Please enter a positive integer")

user_input = input("Hey, enter a number of days and I'll convert them to hours: \n")
validate_n_execute()