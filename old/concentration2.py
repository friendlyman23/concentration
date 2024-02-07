import random
import numpy as np
from time import sleep
import concentration_constants as CC

def welcomePlayer():
    
    concentration = 'CONCENTRATION'
    for letter in concentration:
        print(letter, end=' ')
        # sleep(0.85)
    print()
    print('There are %s cards on the board. Try to find all the matches in five tries.' % CC.CARD_TOTAL)
    # input('(Press RETURN to see the board.)')
    # sleep(.75)

#=======================================

def generateSecretBoard():
    
    # (making empty deck populated with zeroes)
    deck = [0] * len((CC.CARD_ART))
    for i in range(len(deck)):
        deck[i] = [0] * 3

    # add card artwork to deck with card edges
    for i in range(len(CC.CARD_ART)):
        for j in range(len(CC.CARD_ART[i])):
            deck[i][j] = '|' + CC.CARD_ART[i][j] + '|'

    # duplicate each card so each has a match
    for i in range(len(deck)):
        deck.append(deck[i])

    # shuffle the deck
    random.shuffle(deck)

    # group deck into four-card groups
    group = 0
    groupedDeck = []
    while group < len(deck):
        groupedDeck.append(deck[group:group + 4])
        group += 4

    return groupedDeck

    # make empty board 
    for i in range(len(board)):
    for j in range(len(board[0])):
        for k in range(CC.CARDS_PER_ROW):
            board[i][j].append(deck[k][j])

    
#=======================================

def generatePublicBoard():
    #  -----
    # |     |
    # |CARD |
    # | 1   |
    # |_____|


    # creating numbered card backs like above
    cardBacks = []
    
    cardBacks2 = []
    
    cardBacks2 = np.full((CC.CARD_ROWS, 1, CC.CARDS_PER_ROW), '|     |')
    cardBacks3 = np.full((CC.CARD_ROWS, 1, CC.CARDS_PER_ROW), '|CARD |')

    cardBacks4 = []
    for i in range(1, (CC.CARD_TOTAL + 1)):
        if i < 10:
            cardBacks4.append('| ' + str(i) + '   |')
        else:
            cardBacks4.append('| ' + str(i) + '  |')
    cardBacks4 = np.array(cardBacks4)
    cardBacks4.reshape(3, 1, 4)


    publicBoard = CC.CARD_TOPS + cardBacks2, cardBacks3, cardBacks4, CC.CARD_BOTTOMS

    return publicBoard

# def flipCard()

def playAgain():
    print('Would you like to play again?', end=' ')
    return input().lower().startswith('y')

groupedDeck = generateSecretBoard()

for group in groupedDeck:
    for art in group:
        print(*art)

gameIsDone = False

# game loop
while gameIsDone == False:
    
    welcomePlayer()

    secretBoard = generateSecretBoard()

    publicBoard = generatePublicBoard()

    # cardOne = input('Enter a number to indicate which card you will flip over first. (1-%s)' % (CC.CARD_TOTAL))

    # flipCard()

    # getChoiceOne(card1, card2)



    gameIsDone = True
    if gameIsDone:
        if playAgain():
            gameIsDone = False
        else:
            break


    