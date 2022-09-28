# is a built in function that accepts parameters in form of user input

order = 20
customer_name = "Rose"

def shopping(message):
    print(f"{customer_name} has made {order} orders of motivation together with other {num_of_customers} customers")
    print(message)

num_of_customers = input("Enter number of customers: \n")
shopping("Inventory done!")