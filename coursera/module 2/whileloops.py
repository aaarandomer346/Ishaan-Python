# repeatedly executes code until a condition is false
# run a program until something happens
# "break" can be used to exit a while loop or for loop when it is running
# 'continue' basically doesnt let any code under it in the loop run, and directly goes to the next iteration
# nested loop: for every iteration of the outer loop, the inner loop runs every iteration of the inner loop

a = 5
while a > 0: # as long as a is more than 0, execute the code
    print(a)
    a-=1 # decrease a by 1


# secret password
password = ''
password = input('Enter the password: ') # ask the user for the password
while password != 'password': # while the password is wrong
    print("Wrong Password! Please Try Again!") # print this
    password = input('Enter the password: ') # ask for user input
print("Correct Password!") # if the password is correct, the while loop stops, thus executing any code after it

# 'break' keyword
x = 1
while x <= 10: # while x is less than 10
    if x == 5: # if x is 5
        break # stop the while loop
    print(x) # print x
    x+=1 # incriment x
print('')
# continue keyword
for number in range(1, 21):
    if number % 2 != 0:
        if number % 3 == 0:
            continue
        print(number)

print('')
# nested loop
for i in range(1, 5):
    print("i:", i)
    for j in range(1, 11):
        print("\tj:", j)
print('')
# multiplication table
for base in range(1, 11):
    for num in range (1, 11):
        print("{} * {} = {}".format(base, num, base*num))