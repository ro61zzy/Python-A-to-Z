# while loop will execute a certain number of statements as long as a condition is true


calculation_to_units = 24
name_of_unit = "hours"

def days_to_units(num_of_days):
        return f"{num_of_days} days are {num_of_days * calculation_to_units} {name_of_unit}"

def validate_n_execute():
    try:
            user_input_number = int(user_input)
            if user_input_number > 0:
                calculated_value = days_to_units(user_input_number)
                print(calculated_value)
            elif user_input_number == 0:
                print ("You entered a zero, please enter a positive valid number")
            else:
                print("you entered a negative number")

    except ValueError:
        print("Please enter a positive integer, Don't ruin my code")

# to make the program run indefinitely, while has to always be true
#while True
# to allow users themselves to exit the application, when user enters exit
user_input = ""
while user_input != "exit":
    user_input = input("Hey, enter a number of days and I'll convert them to hours: \n")
    validate_n_execute()

