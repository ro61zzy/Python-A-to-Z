order = 20
customer_name = "Rose"

# parameters are passed within the brackets of a function
# this are variables that are defined within a function
# one can have multiple params separated by a coma
def shopping(num_of_customers, message):
    # you can also define a local variable/variable inside available to the function
    my_var = "hello there"
    print(f"{customer_name} has made {order} orders of motivation together with other {num_of_customers} customers")
    print(my_var)
    print(message)

# so when the function is called the parameter is assigned
shopping(10, "Welcome")