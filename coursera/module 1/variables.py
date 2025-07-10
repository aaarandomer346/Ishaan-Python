# when a variable is assigned a value, it takes the type of the value, so you dont need to specify the type of variable it is
# variable names are case-sensitive
# to incriment a variable by a value, use +=, to decrement, use -=
# variables can be reassigned to different values, even if what they are reassigned to has a different type
# another way to do multiplication is to do *=, then followed by a number to multiply by

# boolean operators return a true or false value
# the "and" operator is used when you want both statments to be true for something to run
    # print(x > 3 and x < 5)
    # this can be reritten as print(3 < x < 5)
# the "or" operator is used when as long as 1 statment is True, something runs
    # print(x < 3 or x == 3)
    # this can be reritten as print(x <= 3)
# the "not" operator is used when you want to switch a boolean value. For example, True to False and False to True
    # res = (y <= x)
    # print(not res)

print("Variables Basic")
x = 1
y = x + 3

print(x)
print(y)

x += 3
y -= 1

print(x)
print(y)

x = 'four'
y = True

print(x)
print(y)

x = 5
y = 3

print("\nBoolean Operators")
print("And operator", str(x > 3 and x < 5))
print("And operator simplified", str(3 < x < 5))
print("Or Operator", str(x < 3 or x == 3))
print("Or Operator Simplified", str(x <= 3))
res = (y <= x)
print("Not Operator", not res)