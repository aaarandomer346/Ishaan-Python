fav_movie = input("what is your favourite movie? ") # input 1
fav_drink = input("what is your favourite drink? ") # input 2

combined = "Your favourite movie is {}, and you like to watch it while drinking {}!".format(fav_movie, fav_drink) # adds the variables to the string
print(combined) # prints the string

print("\n")
age = int(input("How old are you? ")) # adds an input for age and casts to a string
print(age + 3) # sees what you will be in 3 years