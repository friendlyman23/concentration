import concentration_constants as CC
import random

CARD_ART = [
[' .-. ', '( (  ', " '-` "], 
[' ✿ ✿ ', '  ✿  ', '✿  ✿ '], 
['     ', '(^ᴥ^)', '(^ᴥ^)'], 
['     ', '𓋼𓍊 𓆏 ', ' 𓍊𓋼𓍊 '], 
['𓆣  𓆣 ', '  𓆣  ', '𓆣 𓆣  '], 
['ପଓ ପଓ', 'ପଓ   ', '  ପଓ '], 

]

board = [[x for x in CARD_ART] * 2]

board = random.shuffle(board)

board = [CARD_ART[i:i+2] for i in range(0, len(CARD_ART), 3)]



print(board)