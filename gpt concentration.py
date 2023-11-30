import random

# Function to create a deck of cards
def create_deck():
    cards = [str(i) for i in range(1, 9)] * 2
    random.shuffle(cards)
    return cards

# Function to initialize the game board
def initialize_board(deck):
    board = [['X'] * 4 for _ in range(4)]
    for i in range(4):
        for j in range(4):
            board[i][j] = deck.pop()
    return board

# Function to display the game board
def display_board(board):
    for row in board:
        print(' '.join(map(str, row)))

# Function to check if the selected cards match
def check_match(board, row1, col1, row2, col2):
    return board[row1][col1] == board[row2][col2]

# Main function to play the game
def play_concentration():
    deck = create_deck()
    board = initialize_board(deck)
    display_board(board)
    matched_cards = set()

    while len(matched_cards) < 8:
        print("Enter the row and column numbers of the two cards (e.g., 1 2):")
        row1, col1 = map(int, input().split())
        row2, col2 = map(int, input().split())

        row1 -= 1
        col1 -= 1
        row2 -= 1
        col2 -= 1

        if row1 not in range(4) or col1 not in range(4) or row2 not in range(4) or col2 not in range(4):
            print("Invalid input. Please try again.")
            continue

        if (row1, col1) in matched_cards or (row2, col2) in matched_cards:
            print("You've already matched these cards. Try again.")
            continue

        if check_match(board, row1, col1, row2, col2):
            print("Match found!")
            matched_cards.add((row1, col1))
            matched_cards.add((row2, col2))
        else:
            print("No match. Try again.")

        board[row1][col1] = 'X'
        board[row2][col2] = 'X'
        display_board(board)

    print("Congratulations! You've matched all the cards!")

# Run the game
if __name__ == "__main__":
    play_concentration()
