# get bill
bill = float(input("How Much Is Your Bill? "))
tax = float(input("How Much Is The Sales Tax? "))
tip = float(input("How Much Do You Want To Tip? "))

# apply tax
bill += (bill*tax/100) # percent tax

# add tip
bill += (bill*tip/100) # percent tip

# round to 2 decimal places
bill = round(bill, 2)

# print final amount
print("Your total bill is: $", bill, sep='')