# for loops can be used to iterate a code block a set amount of times
# here is a example of a for loop used to iterate through a list and print each value

mylist = [1, 'dog', 1203, '#', 'washington', 'bugatti']
for i in mylist: # i gives the value in the list
    print(i)

print("\n")
# find even numbers in a list and add it to a new list

numlist = [1,2,3,4,5,6,7,8,9,10] # list with the numnbers
evenlist = [] # empty list
for num in numlist: # for each value in numlist
    if num % 2 == 0: # if the number is even
        evenlist.append(num) # add it to the list
print(evenlist) # prints evenlist
print("There are {} even numbers in the provided list!".format(len(evenlist)))

print("\n")

# find the lowest number
numlist = [52, 72, 81, 71, 31, 62, 73, 8,63, 13, 0, -345, 31, -343] # list storing all the numbers
lowestnum = numlist[0] # the lowest number
for nums in numlist: # for each value in the list
    if nums < lowestnum: # if the current number is lower than the number in lowestnum
        lowestnum = nums # sets the new lowest num
print(lowestnum) # prints the lowest number in the list

print("\n")

# iterate over lists of strings
planetlist = ['sun', 'mercury', 'venus', 'earth', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune', 'pluto'] # list of planets
for planet in planetlist: # for each string in the array
    if planet == 'sun': # if the curent index has 'sun' as the value
        print("{} is a star, not a planet!".format(planet)) # print this
    elif planet == 'pluto': # if the current index has 'pluto' as the value
        print("{} is no longer considered a planet!".format(planet)) # print this
    else: # otherwise, if it isnt sun or pluto
        print("{} is a planet!".format(planet)) # print this

print("\n")

# iterate over a string
string = 'monday'
for char in string: # for each character in the string
    print(char) # print the character in the string

print("\n")

# for loop using .range()
# iterate over 10 numbers
for x in range(10): # range(amountOfNumbers), doesnt include the numnber specified
    print(x)
print("\n")
# iterate over 10 numbers
for x in range(0, 10): # range(startNumber, endNumber), doesnt include the end number, includes the starting number
    print(x)
print("\n")
# iterate over 6 numbers
for x in range(1, 7): # range(startNumber, endNumber), doesnt include the end number, includes the starting number
    print(x)
print("\n")
# iterate over 5 numbers, 0 - 28, skipping every 6 numbers
for x in range(0, 30, 7): # range(startNumber, endNumber, step), doesnt include the end number, includes the starting number
                            # step works by skipping the next step-1 numbers, and then using the next number
    print(x)
print("\n")
# iterate over 5 numbers, 5 - 1
for x in range(5, -1, -1): # range(startNumber, endNumber, step), doesnt include the end number, includes the starting number
    print(x)
print("\n")
# get odd numbers 1-1200
oddnums = []

for num in range(1, 1201):
    if num % 2 != 0:
        oddnums.append(num)
print(oddnums)