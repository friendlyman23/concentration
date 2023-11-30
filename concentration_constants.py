# CONSTANTS

# list of three line, five space (3x5) unique card artworks
CARD_ART = [

[' .-. ', '( (  ', " '-` "], 
[' ✿ ✿ ', '  ✿  ', '✿  ✿ '], 
['     ', '(^ᴥ^)', '(^ᴥ^)'], 
['     ', '𓋼𓍊 𓆏 ', ' 𓍊𓋼𓍊 '], 
['𓆣  𓆣 ', '  𓆣  ', '𓆣 𓆣  '], 
['ପଓ ପଓ', 'ପଓ   ', '  ପଓ '], 

]



# number of cards in the deck is the length of the card art list multiplied by 2 (because each card has a match)
CARD_TOTAL = len(CARD_ART * 2)

# rows always have 4 cards
CARDS_PER_ROW = 4

# row total is the total number of cards divided by the column total
CARD_ROWS = int(CARD_TOTAL / CARDS_PER_ROW)

CARD_TOP = [' _____ ']
CARD_LINE_2 = ['|     |']
CARD_LINE_3 = ['|CARD |']
CARD_BOTTOM = ['|_____|']

# five lines per card
    #  -----
    # |     |
    # |CARD |
    # | 1   |
    # |_____|

LINES_PER_CARD = 5

# ASCII art "tops" and "bottoms" for the cards
