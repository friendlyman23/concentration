import random
import time

#
# randomize the cards
#
# draw the board
# put the cards on the board
# get player's flips
# check if flips match
# remove matches from the board and record a point
# check to see if the player has matched all the cards
# count the turn
# check if the player is out of turns
# if out of turns, report the final score

# generate a list of dictionary keys with each one appearing twice in the list

CARD_DICT = {

'moon': ['| .-. |', '|( (  |', '| \'-` |'], 

'butterfly': ['| ᙙῖᙖ |','|ପଓ   |', '|  ʚl̈ɞ|'], 

'stars': ['| ✿ ✿ |', '|  ✿  |', '|✿  ✿ |'], 

'frog': ['|     |', '|𓋼𓍊 𓆏 |', '| 𓍊𓋼𓍊 |'], 

'dog': ['|     |', '|(^ᴥ^)|', '|(^ᴥ^)|'], 

'beetle': ['|𓆣  𓆣 |', '|  𓆣  |', '|𓆣 𓆣  |' ]

}




deck = [] # get cards from the dict and put each into the deck twice
for card in CARD_DICT:
    deck.append(CARD_DICT[card])
    deck.append(CARD_DICT[card])

for card in deck:
    print(card[0])


# for i in range(len(deck)): # add card tops and bottoms to card artwork to make complete cards
#     deck[i] = [' _____ '] + deck[i]
#     deck[i].append('|_____|')

# random.shuffle(deck)



# linesToPrint = len(deck) + ((len(deck) / 4) * 2) # number of lines to print is total number of cards + toal number of cards / 4 (why?)
# linesToPrint = int(linesToPrint)

# def printBoard(deck, linesToPrint):
#     for i in range(1, (linesToPrint + 1)): 
#         if resetCountdown == 0:
#             print()
#             row += 4
#             column = 0
#             resetCountdown = 5
#         else: 
#             print(deck[row][column], deck[row + 1][column], deck[row + 2][column], deck[row + 3][column], sep='      ')
#             column = column + 1
#             resetCountdown -= 1



# # generate card backs. make a list of card blanks that can be referenced and replaced by card art
# cardBacks = [[] for i in range(12)]


# for i in range(len(deck)):
#     cardBacks[i].append(' _____ ')
#     cardBacks[i].append('|     |')
#     cardBacks[i].append('|CARD |')
#     if i >= 9:
#         cardBacks[i].append('| ' + str(i + 1) + '  |')
#     else:
#         cardBacks[i].append('|  ' + str(i + 1) + '  |')
#         cardBacks[i].append(' _____ ')


# column = 0
# row = 0
# resetCountdown = 5

# printBoard(deck, linesToPrint)

# printBoard(cardBacks, linesToPrint)



# # lineNumber = 1
# # for cardArt in deck:
# #     if lineNumber == 1, 7, 13:
# #         print(' _____', '  _____', '  _____', '  _____', sep='      ')
# #     elif lineNumber == 5, 11, 17:
# #         print('|_____|', '|_____|', '|_____|', '|_____|', sep='      ')
# #     elif lineNumber == 6, 12:
# #         print()
# #     else:
# #         print('|' + deck[cardArt][i] + '|','|' + deck[1][i] + '|', '|' + deck[2][i] + '|', '|' + deck[3][i] + '|', sep='      ')
# #     lineNumber = lineNumber + 1
# #     print('|' + deck[0][i] + '|','|' + deck[1][i] + '|', '|' + deck[2][i] + '|', '|' + deck[3][i] + '|', sep='      ')
# # print('|_____|', '|_____|', '|_____|', '|_____|', sep='      ')


    

# # print(' _____', '  _____', '  _____', '  _____', sep='      ')
# # print('|' + restructuredDeck[0][0] + '|','|' + restructuredDeck[0][1] + '|', '|' + restructuredDeck[0][2] + '|', '|' + restructuredDeck[0][3] + '|', sep='      ')
# # print('|' + restructuredDeck[1][0] + '|','|' + restructuredDeck[1][1] + '|', '|' + restructuredDeck[1][2] + '|', '|' + restructuredDeck[1][3] + '|', sep='      ')
# # print('|' + restructuredDeck[2][0] + '|','|' + restructuredDeck[2][1] + '|', '|' + restructuredDeck[2][2] + '|', '|' + restructuredDeck[2][3] + '|', sep='      ')
# # print('|_____|', '|_____|', '|_____|', '|_____|', sep='      ')







# # restructuredDeck = [[], [], []]

# # for i in range(len(deck)):
# #     restructuredDeck[0].append(deck[i][0])
# #     restructuredDeck[1].append(deck[i][1])
# #     restructuredDeck[2].append(deck[i][2])

# # for rist in restructuredDeck:
# #     print(rist)


