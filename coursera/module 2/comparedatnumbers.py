# compare 2 numbers for greater/lesser than
# the string before any code in a function/class is called a docstring, used to give a description of what the function does
# either do help(functionName) to give docstring
# or do print(functionName.__doc__) to give docstring. Remember, doc has 2 underscores before and after it
def compare(a, b):
    """Compares the values a and b

    Args:
        a int: first number
        b int: second number

    Returns:
        boolean: returns true if a > b, returns false if a < b
    """
    if a > b:
        return True
    return False
a = input("Enter the first number: ")
b = input("Enter the second number: ")
if compare(int(a), int(b)) == True:
    print(a, "is greater than", b)
else:
    print(b, "is greater than", a)
help(compare)