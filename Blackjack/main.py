import random


def HitOrStand(money):
    hitostand = input("Hit or Stand? ")
    if hitostand == "Hit" or hitostand == "hit":
        money = hit(money)
    elif hitostand == "Stand" or hitostand == "stand":
        money = stand(money)
    else:
        print("Invalid, please say again")
        money = HitOrStand(money)
    return money

def hit(money):
    playerCards.append(random.randint(2, 11))
    if sum(playerCards) == 21:
        print("You Have: " + str(playerCards) + " " + str(sum(playerCards)))
        print("You Win!")
        money = money + (int(bet) * 2)
        print("You now have: $" + str(money))
    elif sum(playerCards) > 21:
        if 11 in playerCards:
            index_11 = playerCards.index(11)
            playerCards[index_11] = 1
            print("You Have: " + str(playerCards) + " " + str(sum(playerCards)))
            money = HitOrStand(money)
        else:
            print("You Have: " + str(playerCards) + " " + str(sum(playerCards)))
            print("You Lose...")
    else:
        print("You Have: " + str(playerCards) + " " + str(sum(playerCards)))
        money = HitOrStand(money)
    return money

def stand(money):
    dealer = dealerbeatplayer()
    if dealer == "True":
        print("Dealer Has: " + str(dealerCards) + " " + str(sum(dealerCards)))
        print("You Win!")
        money = money + (int(bet) * 2)
        print("You now have: $" + str(money))
    elif dealer == "Draw":
        print("Dealer Has: " + str(dealerCards) + " " + str(sum(dealerCards)))
        print("Draw!")
        money = money + int(bet)
        print("You now have: $" + str(money))
    else:
        print("Dealer Has: " + str(dealerCards) + " " + str(sum(dealerCards)))
        print("You Lose...")
    return money

def dealerbeatplayer():
    if sum(dealerCards) < 17:
        dealerCards.append(random.randint(2, 11))
        return dealerbeatplayer()
    else:
        if sum(dealerCards) > 21:
            if 11 in dealerCards:
                index_11 = dealerCards.index(11)
                dealerCards[index_11] = 1
                return dealerbeatplayer()
            else:
                return "True"
        elif sum(dealerCards) < sum(playerCards):
            return "True"
        elif sum(dealerCards) == sum(playerCards):
            return "Draw"
        return "False"
    
playing = True
money = 200

while playing == True:

    dealerCards = []
    playerCards = []

    print("You have: $" + str(money))
    bet = input("How much do you want to bet? ")
    money = money - int(bet)

    for i in range(2):
        playerCards.append(random.randint(2, 11))

    for i in range(2):
        dealerCards.append(random.randint(2, 11))

    print("You Have: " + str(playerCards) + " " + str(sum(playerCards)))
    print("Dealer Has: " + str(dealerCards[1]))

    if sum(playerCards) == 21:
        print("you win")
        money = money + (int(bet) * 2)
        print("You now have: $" + str(money))
    else:
        money = money = HitOrStand(money)
    
    playagain = input("Play Again? (y/n) ")
    if playagain == "y":
        playing = True
    else:
        playing = False