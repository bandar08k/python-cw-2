my_name = input("what is your name")
my_age = input("how old are you")
print(f"My name is {my_name} and I am {my_age} years old")


first_number = float(input("first number"))
secound_number = float(input("secound number"))
operation = input("enter an operation")


if operation == "+":
    print (first_number + secound_number)
elif operation == "-":
    print (first_number - secound_number)
elif operation == "*":
    print (first_number * secound_number)
elif operation == "/":
    print (first_number / secound_number)
else:
    print("the operation is not valid")


bus_capacity = 20
people_inbus = float(input("the people in the bus"))
people_outbus = float(input("the people want to enter the bus"))
empty_seats = bus_capacity - people_inbus

if empty_seats > people_outbus :
    print(f"the empty seats is{empty_seats}")
elif empty_seats <= people_outbus:
    print("the bus is full")