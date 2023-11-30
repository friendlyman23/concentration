import concentration_constants as CC
import random
import copy
import time

# five lines per card
    #  -----  line 1
    # |     | line 2
    # |CARD | line 3
    # | 1   | line 4
    # |_____| line 5

def welcomePlayer():
    
    concentration = 'CONCENTRATION'
    for letter in concentration:
        print(letter, end=' ')
        # time.sleep(.5)
    print()
    print('There are %s cards on the board. Try to find all the matches in five tries.' % CC.CARD_TOTAL)
    # input('(Press RETURN to see the board.)')
    # sleep(.75)

def getCardBacks():

    # now make the strings that will go in the fourth line

    # initialize card numbers list
    cardNos = []

    # add card sides and extra space to the card nos
    for i in range(1, CC.CARD_TOTAL + 1):
        if i < 10:
            extraSpace = '   '
        else:
            extraSpace = '  '
        cardNos.append('|' + extraSpace + str(i) + ' |')

    cardBacks = []

    for _ in range(CC.CARD_TOTAL):
        cardBacks.append([])

    for i in range(len(cardBacks)):
        cardBacks[i].extend(CC.CARD_TOP)
        cardBacks[i].extend(CC.CARD_LINE_2)
        cardBacks[i].extend(CC.CARD_LINE_3)
        cardBacks[i].append(cardNos[i])
        cardBacks[i].extend(CC.CARD_BOTTOM)

    cardBacks = tuple(tuple(_) for _ in cardBacks)

    return cardBacks


def getCardFronts():

# import the card art, double each, and add the sides of the card to the art


    cardFrontsArt= copy.deepcopy(CC.CARD_ART)

    for i in range(len(cardFrontsArt)):
        for j in range(len(cardFrontsArt[i])):
            cardFrontsArt[i][j] = '|' + cardFrontsArt[i][j] + '|' 

    cardFronts = [[] for _ in range(len(CC.CARD_ART))]
    for i in range(len(cardFronts)):
        cardFronts[i] = CC.CARD_TOP + cardFrontsArt[i] + CC.CARD_BOTTOM

    cardFronts = [x for x in cardFronts * 2]

    random.shuffle(cardFronts)

    cardFronts = tuple(tuple(_) for _ in cardFronts)

    return cardFronts

def setFlippedList():
    isFlipped = {}
    for i in range(1, CC.CARD_TOTAL + 1):
        isFlipped[i] = False
    return isFlipped

def flipCard(card, isFlipped):
    isFlipped[card] = not isFlipped[card]

    return card

def getCards(backs, fronts):

    cards = []
    listOfFronts = []
    listOfBacks = []
    for i in range(CC.CARD_TOTAL):
        listOfFronts.append(list(fronts[i]))
        listOfBacks.append(list(backs[i]))

    cards.append(listOfBacks)
    cards.append(listOfFronts)

    return cards

def printBoard(cards, isFlipped):

    # assemble the deck and check whether to show the front or back of a card based on whether it is flipped

    board = []

    for i in range(CC.CARD_TOTAL):
        if isFlipped[i + 1] is True:
            board.append(cards[1][i])
        else:
            board.append(cards[0][i])

    board = [board[i:i+CC.CARDS_PER_ROW] for i in range(0, CC.CARD_TOTAL, CC.CARDS_PER_ROW)]

    for group in board:
        for i in range(CC.LINES_PER_CARD):
            for j in range(CC.CARDS_PER_ROW):
                print(group[j][i], end=' ')
            print() 
                

def playerTurn(cards, isFlipped):

    isFlipped = setFlippedList()

    playerChoice0 = 0

    while playerChoice0 not in range(1, CC.CARD_TOTAL + 1):
        print('Which card would you like to flip?')
        playerChoice0 = int(input())

    flipCard(playerChoice0, isFlipped)
    printBoard(cards, isFlipped)

    playerChoice1 = 0

    while playerChoice1 not in range(1, CC.CARD_TOTAL + 1):
        print('Choose one more card to flip.')
        playerChoice1 = int(input())

    flipCard(playerChoice1, isFlipped)
    printBoard(cards, isFlipped)

    if cards[1][playerChoice0 - 1] == cards[1][playerChoice1 - 1]:
        # Update the structure of matched cards in the cards list
        cards[0][playerChoice0 - 1] = [' ' * 7] * CC.LINES_PER_CARD
        cards[0][playerChoice1 - 1] = [' ' * 7] * CC.LINES_PER_CARD
        cards[1][playerChoice0 - 1] = [' ' * 7] * CC.LINES_PER_CARD
        cards[1][playerChoice1 - 1] = [' ' * 7] * CC.LINES_PER_CARD
        return playerChoice0, playerChoice1
    else:
        return 'No match found. :('


    




while True:

    welcomePlayer()

    # get card fronts and backs
    cardBacks = getCardBacks()
    cardFronts = getCardFronts()

    #list of cards indicating whether they are flipped
    isFlipped = setFlippedList()

    #put the card sides together into a deck of cards
    cards = getCards(cardBacks, cardFronts)

    




    turns = 10
    matches = 0

    while turns > 0:

        #print the board

        isFlipped = setFlippedList()
         
        printBoard(cards, isFlipped)


        moveResult = playerTurn(cards, isFlipped)

        if type(moveResult) == tuple:
            print('You found a match!')
            input('Press return to continue.')
            match1, match2 = moveResult
            for i in range(5):
                cards[1][match1 - 1][i] = ' ' * 7
                cards[1][match2 - 1][i] = ' ' * 7
            setFlippedList()

            matches += 1
            if matches == 6:
                print('You won!')
                print('HECK YEAH')
                time.sleep(1)
                print('              HECK YEAH!')
                time.sleep(1)
                print('    HECK YEAH DUDE!')
                
                break

            turns -= 1
        
        else:
            print(moveResult)
            input('Press return to continue.')
            turns -= 1
            isFlipped = setFlippedList()

    print('The game is over.')
    input('Press return to continue.')


    

            


    

    

    





    

    





print(0)









