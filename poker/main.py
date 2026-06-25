import random

cards = ["S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK", "SA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK", "DA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK", "HA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK", "CA"]
rawCards = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
straightFlushHands = [
    ["SK", "SQ", "SJ", "S10", "S9"],
    ["SQ", "SJ", "S10", "S9", "S8"],
    ["SJ", "S10", "S9", "S8", "S7"],
    ["S10", "S9", "S8", "S7", "S6"],
    ["S9", "S8", "S7", "S6", "S5"],
    ["S8", "S7", "S6", "S5", "S4"],
    ["S7", "S6", "S5", "S4", "S3"],
    ["S6", "S5", "S4", "S3", "S2"],
    ["D5", "D4", "D3", "D2", "DA"],

    ["DK", "DQ", "DJ", "D10", "D9"],
    ["DQ", "DJ", "D10", "D9", "D8"],
    ["DJ", "D10", "D9", "D8", "D7"],
    ["D10", "D9", "D8", "D7", "D6"],
    ["D9", "D8", "D7", "D6", "D5"],
    ["D8", "D7", "D6", "D5", "D4"],
    ["D7", "D6", "D5", "D4", "D3"],
    ["D6", "D5", "D4", "D3", "D2"],
    ["D5", "D4", "D3", "D2", "DA"],

    ["HK", "HQ", "HJ", "H10", "H9"],
   ["HQ", "HJ", "H10", "H9", "H8"],
   ["HJ", "H10", "H9", "H8", "H7"],
   ["H10", "H9", "H8", "H7", "H6"],
   ["H9", "H8", "H7", "H6", "H5"],
   ["H8", "H7", "H6", "H5", "H4"],
   ["H7", "H6", "H5", "H4", "H3"],
   ["H6", "H5", "H4", "H3", "H2"],
   ["H5", "H4", "H3", "H2", "HA"],

    ["CK", "CQ", "CJ", "C10", "C9"],
   ["CQ", "CJ", "C10", "C9", "C8"],
   ["CJ", "C10", "C9", "C8", "C7"],
   ["C10", "C9", "C8", "C7", "C6"],
   ["C9", "C8", "C7", "C6", "C5"],
   ["C8", "C7", "C6", "C5", "C4"],
   ["C7", "C6", "C5", "C4", "C3"],
   ["C6", "C5", "C4", "C3", "C2"],
   ["C5", "C4", "C3", "C2", "CA"]
]
straightHands = [
    ["A", "K", "Q", "J", "10"],
    ["K", "Q", "J", "10", "9"],
   ["Q", "J", "10", "9", "8"],
   ["J", "10", "9", "8", "7"],
   ["10", "9", "8", "7", "6"],
   ["9", "8", "7", "6", "5"],
   ["8", "7", "6", "5", "4"],
   ["7", "6", "5", "4", "3"],
   ["6", "5", "4", "3", "2"],
   ["5", "4", "3", "2", "A"]
]

playerList = []
pot = 0
betPlayersNeed = 0
cardsShown = []
playersLeft = True
turn = 1

class players():
    def __init__(self, cards, status, money, currBet, playerNum):
        self.cards = cards
        self.status = status
        self.money = money
        self.currBet = currBet
        self.playerNum = playerNum

def raiseBet(players, betPlayesrNeeds, pot):
    print("You have: " + str(players.money))
    players.currBet = int(input("How much do you want to bet? "))
    if players.currBet > int(players.money):
        print("You don't have that much money!")
        cancelBetoContinue = input("cancel bet? ")
        if cancelBetoContinue == "cancel":
            players.currBet = 0
            players.status = "check"
            return players, betPlayesrNeeds, pot
        else:
            return raiseBet(players, betPlayersNeed, pot)
    else:
        betPlayesrNeeds = players.currBet
        players.money = int(players.money) - int(players.currBet)
        pot += players.currBet
        return players, betPlayesrNeeds, pot

def checkocall(players, betPlayerNeed, pot):
    if betPlayerNeed > 0:
        players.currBet = betPlayerNeed
        players.money = int(players.money) - int(players.currBet)
        pot += players.currBet
        players.status == "check"
    return players, betPlayerNeed, pot

def playerTurn(players, betPlayersNeed, pot):
    if players.status != "fold": 
        if turn != 1:
            print(cardsShown)
        print("Bet Needed to Call: " + str(betPlayersNeed))
        print("Current Player: " + str(players.playerNum + 1))
        input("Show Card? ")
        print(players.cards)
        players.status = input("check/call, raise, fold? ")
        if players.status == "check" or players.status == "call":
            players, betPlayersNeed, pot = checkocall(players, betPlayersNeed, pot)
            return players, betPlayersNeed, pot
        elif players.status == "raise":
            players, betPlayersNeed, pot = raiseBet(players, betPlayersNeed, pot)
            return players, betPlayersNeed, pot
        else:
            return players, betPlayersNeed, pot
    return players, betPlayersNeed, pot

def checkIfAllPlayersBet(players, betPlayersNeed, pot):
    if players.currBet == 0 and betPlayersNeed > 0:
        print("Current Player: " + str(players.playerNum + 1))
        input("Show Cards? ")
        print(players.cards)
        CheckorFold = input("Check or Fold? ")
        if CheckorFold == "check":
            return checkocall(players, betPlayersNeed, pot)
        else:
            players.status = "fold"
            return players, betPlayersNeed, pot
    return players, betPlayersNeed, pot

def getNumPlayersLeft(numPlayers, playerList):
    for i in playerList:
        if i.status == "fold":
            numPlayers -= 1
    return numPlayers

def highestHand(players, cardsShown, straightFlushHands, straightHands, rawcards):
    cardsWith = [[], [], [], []]
    for i in cardsShown:
        players.cards.append(i)
    cardsWith[0] = [s for s in cardsShown if "S" in s]
    cardsWith[1] = [s for s in cardsShown if "D" in s]
    cardsWith[2] = [s for s in cardsShown if "H" in s]
    cardsWith[3] = [s for s in cardsShown if "C" in s]

    # royal flush
    for i in cardsWith:
        if "A" in i and "K" in i and "Q" in i and "J" in i and "10" in i:
            return 1, "NA"
    
    # straight flush
    player_set = set(players.cards)
    if any(set(sf).issubset(player_set) for sf in straightFlushHands):
        return 2, "NA"
    
    # four of a kind
    for chartofind in rawcards:
        count = 0
        for string in players.cards:
            count += string.count(chartofind)
        if count == 4:
            return 3, "NA"
    
    # full house
    isthere2 = False
    isthere3 = False
    for chartoget in rawcards:
        cnt = 0
        for strin in players.cards:
            cnt += strin.count(chartoget)
        if cnt == 2:
            isthere2 = True
        elif cnt > 2:
            isthere3 = True
    if isthere2 == True and isthere3 == True:
        return 4, "NA"
    
    # flush
    for i in cardsWith:
        if len(i) >= 5:
            return 5, "NA"
    
    # straight
    ranks = [card[1:] for card in players.cards]
    rank_set = set(ranks)
    if any(set(st).issubset(rank_set) for st in straightHands):
        return 6, "NA"
    
    # three of a kind
    for chartofind in rawcards:
        count = 0
        for string in players.cards:
            count += string.count(chartofind)
        if count == 3:
            return 7, "NA"
        
    # 2 pair
    there2 = False
    isthere2again = False
    for charneeded in rawcards:
        cnt2 = 0
        for sttr in players.cards:
            cnt2 += sttr.count(charneeded)
        if cnt2 == 2 and there2 == False:
            there2 = True
        elif cnt2 == 2:
            isthere2again = True
    if there2 == True and isthere2again == True:
        return 8, "NA"
    
    # pair
    for chartofind in rawcards:
        count = 0
        for string in players.cards:
            count += string.count(chartofind)
        if count == 2:
            return 9, "NA"
    
    # high card
    return 10, str(ranks[0])

def round(cardsShown, pot, playerList, numPlayers):
    if numPlayers != 1:
        cardsShown.append(cards[random.randint(0, 51)])
        print("Shared Cards: " + str(cardsShown))
        print("Current Pot: " + str(pot))
        betPlayersNeed = 0
        for i in playerList:
            i, betPlayersNeed, pot = playerTurn(i, betPlayersNeed, pot)
        for i in playerList:
            i, betPlayersNeed, pot = checkIfAllPlayersBet(i, betPlayersNeed, pot)
        numPlayers = getNumPlayersLeft(numPlayers, playerList)
    return cardsShown, pot, playerList, numPlayers

numPlayers = int(input("Number of players? "))
amountPerPlayer = input("How much per player? ")

for i in range(int(numPlayers)):
    playerList.append(players([], "NA", amountPerPlayer, 0, i))

# First round, before center cards shown
for i in range(len(playerList)):
    for j in range(2):
        playerList[i].cards.append(cards[random.randint(0, 51)])
for i in playerList:
    i, betPlayersNeed, pot = playerTurn(i, betPlayersNeed, pot)

for i in playerList:
    i, betPlayersNeed, pot = checkIfAllPlayersBet(i, betPlayersNeed, pot)

numPlayers = getNumPlayersLeft(numPlayers, playerList)

if numPlayers != 1:
    # second round, center cards shown
    for i in range(3):
        cardsShown.append(cards[random.randint(0, 51)])
    print("Shared Cards: " + str(cardsShown))
    print("Current Pot: " + str(pot))
    betPlayersNeed = 0
    for i in playerList:
        i, betPlayersNeed, pot = playerTurn(i, betPlayersNeed, pot)
    for i in playerList:
        i, betPlayersNeed, pot = checkIfAllPlayersBet(i, betPlayersNeed, pot)
    numPlayers = getNumPlayersLeft(numPlayers, playerList)
    
    for i in range(2):
        round(cardsShown, pot, playerList, numPlayers)

    rank_value = {"2":2, "3":3, "4":4, "5":5, "6":6, "7":7,
      "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}

    scores = []
    for i in playerList:
        score, highcard_str = highestHand(i, cardsShown, straightFlushHands, straightHands, rawCards)
        highcard_val = rank_value.get(highcard_str, 0)  # 0 if highcard is "NA"
        scores.append([score, highcard_val])

    # Determine winner
    best_score_entry = min(scores, key=lambda x: (x[0], -x[1]))
    winner_index = scores.index(best_score_entry)
    winning_player = playerList[winner_index]

    print(f"Winning player: {winner_index + 1}")
    print(f"Winning hand score and high card: {best_score_entry}")
    print(f"Winning hand cards: {winning_player.cards}")