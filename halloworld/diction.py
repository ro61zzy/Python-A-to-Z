# customer = {
#     "name": "rozzy karemeri",
#     "age": "20",
#     "is_verified": True
# }
# customer["name"] = "bobby"
# print(customer.get("name", "not available"))

phone = input("phone: ")
digits_mapping = {
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four"
}
output = ""
for ch in phone:
    output += digits_mapping.get(ch, "!") + " "
print(output)