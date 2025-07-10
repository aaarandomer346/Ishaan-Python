import traceback

def calculator(age_input=None):

    # Get dog age
    if age_input is None:
        age = input("Input dog years: ")
    else:
        age = str(age_input)

    try:
        # Cast to float
        dog_age = float(age)

        # If user enters negative number, print message
        if dog_age <= 0:
            print("Dog cannot have a negative age!")
        else:
            if dog_age <= 1.0:
                human_age = dog_age * 15
            elif dog_age <= 2.0:
                human_age = dog_age * 12
            elif dog_age <= 3.0:
                human_age = dog_age * 9.3
            elif dog_age <= 4.0:
                human_age = dog_age * 8
            elif dog_age <= 5.0:
                human_age = dog_age * 7.2
            else:
                human_age = 36 + ((dog_age - 5) * 7)
            print("The given dog age {} is {} in human years.".format(dog_age, round(human_age, 1)))
        # Otherwise, calculate dog's age in human years

        # your code here

    except:
        print(age, "is an invalid age.")
        print(traceback.format_exc())

calculator() # This line calls the calculator function