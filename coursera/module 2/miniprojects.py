# calculate the average based on user input
# only if the user enters -1 does the code run the program

nums = []
numberinput = input("Enter a number to calculate the average off, or enter -1 to calculate the average: ")
while numberinput != '-1':
    try:
        number = float(numberinput)
        nums.append(number)
    except:
        print("Invalid input. Please enter a number or -1 to exit.")
    numberinput = input("Enter a number to calculate the average off, or enter -1 to calculate the average: ")
for num in nums:
    average = sum(nums) / len(nums)
print("Average of Numbers Given: ", average)

print('')
# word reversal
string = input("What word do you want to reverse? ") # get the word
letters = [] # make a list to hold each letter in the word
rev = '' # make the result string
for char in string: # for each character in the string
    letters.append(char) # add each character of the string into the list
for i in range(len(letters)): # for each index of the list letters
    rev = rev + letters[len(letters) - i - 1] # adds the last, then the second last, then so on
print(rev) # print the result

string = 'pasta'
result = ''

for i in range(len(string) - 1, -1, -1):
    result += string[i]
print(result)