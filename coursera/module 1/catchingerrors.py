number = input("Please enter an integer: ")

try: # try to cast to an int
    number = int(number)
except ValueError as e: # if the valueerror appears, instead of stopping the program, do this
    print("what you entered is not an integer")
    print(e)
else: # if the try was successful, do thiss
    print(str(number), "is an integer!")


_number = 3
print(_number)

