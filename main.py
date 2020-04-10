def testUser():
    """
    Provides a card from the list of cards to test the user

    Args:
        none

    Returns:
        Returns random card from list of cards

    Raises:
        none
    """
    return cards[random.randint(0, len(cards)-1)]

def addCard(q, a):
    """
    Creates the new card to be added to the list

    Args:
        q: string / question from user input
        a: string / answer from user input

    Returns:
        none

    Raises:
        none
    """
    c = {}
    c["question"] = q
    c["answer"] = a
    cards.append(c)
    saveCards(cards)

def saveCards():
    """
    Converts cards from list to JSON string then updates
    JSON file with the set of cards at that current time

    Args:
        none

    Returns:
        none

    Raises:
        none yet
    """
    with open('cards.json', 'w') as f:
        json.dump(cards, f, indent=2)

def displayCards():
    """
    Displays all the cards in the present list

    Args:
        none

    Returns:
        none

    Raises:
        none
    """
    for i in cards:
        print(i["question"])

def loadCards():
    """
    Reads in JSON file then and converts it to a python list

    Args:
        none

    Returns:
        c: list / the list of sets (cards)

    Raises:
        none
    """
    with open('cards.json') as f:
        c = json.load(f)
    return c

def getUserInput():
    """
    Gets option integer user input

    Args:
        none

    Returns:
        x: integer / the integer that the user has selected and been validated

    Raises:
        ValueError: raises an exception for when input is not an integer
    """
    while True:
        try:
            x = int(input("Select option by number: "))
            break
        except ValueError:
            print("Not a valid integer please try again")
    return x

def getUserIndex():
    """
    Gets index user input

    Args:
        none

    Returns:
        x: integer / the index integer that the user has selected and been validated

    Raises:
        ValueError: raises an exception for when the input is not an integer
    """
    while True:
        try:
            x = int(input("Select index: "))
            break
        except ValueError:
            print("Not a valid integer please try again")
    return x

def removeCard():
    """
    Removes a card from the list of cards based off of index

    Args:
        none

    Returns:
        none

    Raises:
        none
    """
    print("Select card by index to be removed")
    for i in range(0, len(cards)):
        print(str(i) + " IndexNo - Question: " + cards[i]["question"])
    index = getUserIndex()
    if (index < len(cards) and index >= 0):
        del cards[i]
    saveCards(cards)


def main():
    running = True
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

if __name__ == '__main__':
    import json
    import random
    # Cards is a global variable
    cards = loadCards()
    # Calls the main fucntion that runs the program
    main()
