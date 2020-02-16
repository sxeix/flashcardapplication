import json
import random

def testUser():
    return cards[random.randint(0, len(cards)-1)]

def addCard(q, a):
    c = {}
    c["question"] = q
    c["answer"] = a
    cards.append(c)
    saveCards(cards)

def saveCards(c):
    with open('cards.json', 'w') as f:
        json.dump(c, f, indent=2)

def displayCards():
    for i in cards:
        print(i["question"])

def loadCards():
    with open('cards.json') as f:
        c = json.load(f)
    return c

def getUserInput():
    while True:
        try:
            x = int(input("Select option by number: "))
            break
        except ValueError:
            print("Not a valid integer please try again")
    return x

def getUserIndex():
        while True:
            try:
                x = int(input("Select index: "))
                break
            except ValueError:
                print("Not a valid integer please try again")
        return x

def removeCard():
    print("Select card by index to be removed")
    for i in range(0, len(cards)):
        print(str(i) + " IndexNo - Question: " + cards[i]["question"])
    index = getUserIndex()
    if (index < len(cards) and index >= 0):
        del cards[i]
    saveCards(cards)

running = True
cards = loadCards()
while(running):
    print("---------------------")
    print("1. Test yourself")
    print("2. Add a card")
    print("3. Display all cards")
    print("4. Remove a card")
    print("0. EXIT")
    option = getUserInput()
    if option == 1:
        card = testUser()
        print("Question: " + card["question"])
        x = input("Press enter to reveal the answer")
        print("Answer: " + card["answer"])
    elif option == 2:
        q = str(input("Question: "))
        a = str(input("Answer: "))
        addCard(q, a)
    elif option == 3:
        displayCards()
    elif option == 4:
        removeCard()
    elif option == 0:
        running = False
    else:
        print("That is not a valid option")
