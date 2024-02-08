import random
import sys
import os

CARD_ART = [

[' .-. ', '( (  ', " '-` "], 
[' ✿ ✿ ', '  ✿  ', '✿  ✿ '], 
['     ', '(^ᴥ^)', '(^ᴥ^)'], 
['     ', '𓋼𓍊 𓆏 ', ' 𓍊𓋼𓍊 '], 
['𓆣  𓆣 ', '  𓆣  ', '𓆣 𓆣  '], 
['ପଓ ପଓ', 'ପଓ   ', '  ପଓ '], 

]

def getCards(art):

    theCards = []

    for _ in CARD_ART:
        modifiedCard = []
        modifiedCard.append(' _____ ')
        for line in _:
            modifiedCard.append('|' + line + '|')
        modifiedCard.append('|_____|')
        theCards.append({'cardFront': modifiedCard})

    for card in theCards:
        card['isOnBoard'] = True
        card['isFlipped'] = False

    for card in theCards[:]:
        theCards.append(card.copy())

    random.shuffle(theCards)

    for card in theCards:
        tempCard = []
        if theCards.index(card) >= 9:
            extraSpace = ' '
        else:
            extraSpace = '  '
        tempCard.append(' _____ ')
        tempCard.append('|     |')
        tempCard.append('|CARD |')
        tempCard.append('|' + extraSpace + str(theCards.index(card) + 1) + '  |')
        tempCard.append('|_____|')
        card['cardBack'] = tempCard.copy()
        
    return theCards

def printBoard(cards, turns):

    os.system('cls' if os.name == 'nt' else 'clear')
    
    board = [cards[i:i+4] for i in range(0, 12, 4)]

    for group in board:
        for i in range(len(cards[0]['cardFront'])):
            for card in group:
                if not card['isOnBoard']:
                    print('       ', end=' ')
                elif card['isFlipped']:
                    side = 'cardFront'
                    print(card[side][i], end=' ')
                else:
                    side = 'cardBack'
                    print(card[side][i], end=' ')
            print()
    print('*' * 32)
    print(f'TURNS REMAINING: {turns}')

#returns turns
def getNumTurns():
    print('How good are you at Memory Match?\n1: I\'m OK\n2: I\'m good\n3: I\'m Amazing')
    print('\n0: "Help me"\n')
    diff = int(input('Enter 1, 2, 3. Or 0. '))
    
    if diff == 1:
        turns = 20
    elif diff == 2:
        turns = 15
    elif diff == 3:
        turns = 10
    else:
        print('OK!!!!!')
        turns = 1000

    return turns

def flipCard(cards, cardToFlip):
    cards[cardToFlip]['isFlipped'] = True

def playerMove(cards):

    flipNumOne = getCardFlip(cards, 'first')
    flipCard(cards, flipNumOne)
    printBoard(cards, turns)

    flipNumTwo = getCardFlip(cards, 'second')
    flipCard(cards, flipNumTwo)
    printBoard(cards, turns)

    if cards[flipNumOne]['cardFront'] == cards[flipNumTwo]['cardFront']:
        print('You found a match!')
        cards[flipNumOne]['isOnBoard'] = cards[flipNumTwo]['isOnBoard'] = False
        input('(Press Enter to continue.)')

    else:
        print('No match found.')
        cards[flipNumOne]['isFlipped'] = cards[flipNumTwo]['isFlipped'] = False
        input('(Press Enter to continue.)')

def getCardFlip(cards, flipNum):

    cardFlipped = ''
    while True:
        cardFlipped = input(f'Enter the number of the {flipNum} card you want to flip (1-12). Or type "quit"\n')
        if cardFlipped == 'quit':
            sys.exit()
        try:
            cardFlipped = int(cardFlipped) - 1
            if cardFlipped not in range(12):
                print('Please enter a number between 1 and 12.')
                input('(Press enter to continue.)')
                continue
            if not cards[cardFlipped]['isOnBoard']:
                print('That card is no longer on the board.')
                input('(Press enter to continue.)')
                continue
            elif cards[cardFlipped]['isFlipped']:
                print('You have already flipped that card.')
                input('(Press enter to continue.)')
                continue
            else:
                return cardFlipped
        except ValueError:
            print('You must enter a number between 1 and 12.')

def checkWin(cards, cardsRemaining):
    cardsRemaining = 12
    for card in cards:
        if not card['isOnBoard']:
            cardsRemaining -= 1
    return cardsRemaining

def isFutile(cardsRemaining, turns):
    if cardsRemaining / 2 > turns:
        return True
    else:
        return False

print('Welcome to Memory Match!')

theCards = getCards(CARD_ART)
turns = getNumTurns()
cardsRemaining = 12
while turns > 0:
    
    printBoard(theCards, turns)
    playerMove(theCards)
    
    cardsRemaining = checkWin(theCards, cardsRemaining)
    if not cardsRemaining:
        print('Congratulations! You have found all of the matches. You win!!!!!!')
        sys.exit()
    else:
        turns -= 1
    
    if isFutile(cardsRemaining, turns):
        print(f'There are {int(cardsRemaining / 2)} more matches to make, but only {turns} turns remaining, so it is no longer possible for you to win. If you would like to quit now, please type "quit." To continue anyway, press enter.')
        if input() == 'quit':
            sys.exit()

print('No turns remaining. Game over.')






