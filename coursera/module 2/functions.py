# Python has numerous builtin functions, here are some of them:
# print()
# float()
# round()
# max()
# min()
# len()
# some of them have already been used in the previous parts of this course
# if you want to know how to use it, you have 2 options:
    # 1, google it
    # 2, hover over the function to see what parameters it takes (works on vscode only ig)

# User Defined Functions
# function conventions:
    # Name a function based on what it does
    # whitespace is important
# sometimes takes an input, or parameters
# sometimes gives outputs values back to where it was called using return keyword
# define them using:
def function_name(parameter1, parameter2):
    parameter1 = parameter2
    return parameter1

# Example function:
def double(input):
    return input * 2
print(double(3))