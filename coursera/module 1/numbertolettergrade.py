gradeinpercent = int(input("What number grade did you get? "))

if gradeinpercent >= 90:
    print("You got an A")
elif 80 <= gradeinpercent < 90:
    print("You got a B")
elif 70 <= gradeinpercent < 80:
    print("You got a C")
elif 60 <= gradeinpercent < 70:
    print("You got a D")
else:
    print("You got an F")