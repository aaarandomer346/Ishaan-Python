print("hello, world") # regular print statment

print ("hello,", "world") # same output

print("hello, ", end='') # overrides how a print statment ends, usually its \n, or new line
print("world")

print("hello", "world", sep = ', ') # adds a seperator between the 2, usally a single space, but can be overriden

print("hello, world") # can either use double
print('hello, world') # or single quotes

print("hello, " + "world") # does the same as
print("hello,", "world") # this

print("4 % 2 =", 4%2) # can also put ints and floats into print functions
# print("4 % 2 = " + 4 % 2) does not work, gives an error
print("4 % 2 = " + str(4 % 2)) # this works since it is cast to a string                # you can only add 2 strings together
print("4 is even? " + str(4 % 2 == 0)) # also works with boolean values

x = 5
y = 10

print("x = {}, y = {}".format(x, y)) # palce {} within the string and then use .format to add variables where the {} is placed.
                                     # how the variables are ordered matter
                                     # you could also do:
                                     # str = "Hello world at {} o'clock"
                                     # strformated = str.format("10:00")
                                     # print(strformated)