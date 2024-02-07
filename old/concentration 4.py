import concentration_constants as CC
import random
import copy

# five lines per card
    #  -----  line 1
    # |     | line 2
    # |CARD | line 3
    # | 1   | line 4
    # |_____| line 5

cardTop = tuple(' _____ ')
cardLine2 = ['|     |']
cardLine3 = ['|CARD |']
cardBottom = ['|_____|']

# now make the strings that will go in the fourth line

# initialize card numbers list
cardNos = []

# add card sides and extra space to the card nos
for i in range(1, CC.CARD_TOTAL + 1):
    if i < 10:
        extraSpace = '   '
    else:
        extraSpace = '  '
    cardNos.append('|' + extraSpace + str(i) + '|')

cardBacks = []

for _ in range(CC.CARD_TOTAL):
    cardBacks.append([])

for i in range(len(cardBacks)):
    cardBacks[i].extend(cardTop)
    cardBacks[i].extend(cardLine2)
    cardBacks[i].extend(cardLine3)
    cardBacks[i].append(cardNos[i])
    cardBacks[i].extend(cardBottom)








# import the card art, double each, and add the sides of the card to the art

cardFrontsArt = copy.deepcopy(CC.CARD_ART)

for i in range(len(cardFrontsArt)):
    for j in range(len(cardFrontsArt[i])):
        cardFrontsArt[i][j] = '|' + cardFrontsArt[i][j] + '|' 

cardFronts = [[] for _ in range(len(CC.CARD_ART))]
for i in range(len(cardFronts)):
    cardFronts[i] = cardTop + cardFronts[i] + cardFrontsArt[i] + cardBottom


    # cardFronts[i].extend(cardTop)
    # for j in range(len(cardFrontsArt[0])):
    #     cardFronts[i].append(cardFrontsArt[j])
    # cardFronts[i].extend(cardBottom)

cardFronts = [x for x in cardFronts * 2]

random.shuffle(cardFronts)





    










