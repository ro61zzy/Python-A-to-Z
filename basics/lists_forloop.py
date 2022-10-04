# lists [1, 2, 3], [boy, girl, nonbinary]
# we can provide a list of numbers as input, instead of inputing those values one at a time
calculation_to_units = 24
name_of_unit = "hours"
 
def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_n_execute():
    try:
            user_input_number = int(num_of_days_element)
            if user_input_number > 0:
                calculated_value = days_to_units(user_input_number)
                print(calculated_value)
            elif user_input_number == 0:
                print ("You entered a zero, please enter a positive valid number")
            else:
                print("you entered a negative number")

    except ValueError:
        print("Please enter a positive integer, Don't ruin my code")

user_input = ""
while user_input != "exit":
    user_input = input("Hey, enter a number of days and I'll convert them to hours: \n")
# for loop is used for iteration for a sequence eg list, let's get user input as a list
    # .split will convert string to list
    print(type(user_input.split(",")))
    print(user_input.split(","))
    for num_of_days_element in user_input.split(","):
        validate_n_execute()