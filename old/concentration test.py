cards = [

card1 = {'cardNo':1, 'back':[' _____ ', '|     |', '|CARD |', '|   1|', '|_____|'], 'front':[' _____ ', '| :)  |', '| :):)|', '|:)   |', ' _____ '], 'flippable':True, 'isFlipped':False}, 

card2 = {'cardNo': 2, 'back': [' _____ ', '|     |', '|CARD |', '|   2|', '|_____|'], 'front': [' _____ ', '| :=  |', '| :=:=|', '|:=   |', ' _____ '], 'flippable': True, 'isFlipped': False}, 

card3 = {'cardNo': 3, 'back': [' _____ ', '|     |', '|CARD |', '|   3|', '|_____|'], 'front': [' _____ ', '| :[  |', '| :[:[|', '|:[   |', ' _____ '], 'flippable': True, 'isFlipped': False}

card4 = {'cardNo':1, 'back':[' _____ ', '|     |', '|CARD |', '|   1|', '|_____|'], 'front':[' _____ ', '| :)  |', '| :):)|', '|:)   |', ' _____ '], 'flippable':True, 'isFlipped':False}, 

card5 = {'cardNo': 2, 'back': [' _____ ', '|     |', '|CARD |', '|   2|', '|_____|'], 'front': [' _____ ', '| :=  |', '| :=:=|', '|:=   |', ' _____ '], 'flippable': True, 'isFlipped': False}, 

card6 = {'cardNo': 3, 'back': [' _____ ', '|     |', '|CARD |', '|   3|', '|_____|'], 'front': [' _____ ', '| :[  |', '| :[:[|', '|:[   |', ' _____ '], 'flippable': True, 'isFlipped': False}

card7 = {'cardNo':1, 'back':[' _____ ', '|     |', '|CARD |', '|   1|', '|_____|'], 'front':[' _____ ', '| :)  |', '| :):)|', '|:)   |', ' _____ '], 'flippable':True, 'isFlipped':False}, 

card8 = {'cardNo': 2, 'back': [' _____ ', '|     |', '|CARD |', '|   2|', '|_____|'], 'front': [' _____ ', '| :=  |', '| :=:=|', '|:=   |', ' _____ '], 'flippable': True, 'isFlipped': False}, 

card9 = {'cardNo': 3, 'back': [' _____ ', '|     |', '|CARD |', '|   3|', '|_____|'], 'front': [' _____ ', '| :[  |', '| :[:[|', '|:[   |', ' _____ '], 'flippable': True, 'isFlipped': False}

card 10 = {'cardNo':1, 'back':[' _____ ', '|     |', '|CARD |', '|   1|', '|_____|'], 'front':[' _____ ', '| :)  |', '| :):)|', '|:)   |', ' _____ '], 'flippable':True, 'isFlipped':False}, 

card 11 = {'cardNo': 2, 'back': [' _____ ', '|     |', '|CARD |', '|   2|', '|_____|'], 'front': [' _____ ', '| :=  |', '| :=:=|', '|:=   |', ' _____ '], 'flippable': True, 'isFlipped': False}, 

card 12 = {'cardNo': 3, 'back': [' _____ ', '|     |', '|CARD |', '|   3|', '|_____|'], 'front': [' _____ ', '| :[  |', '| :[:[|', '|:[   |', ' _____ '], 'flippable': True, 'isFlipped': False}

]

board = []

for i in range(0, len(cards), 4):
    for x in range(len(cards[0][front])):
        lineToPrint = [cards[i]['front'][x