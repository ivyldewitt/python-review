# 1. Choose the players
# 2. Create the board
# 3. Choose an initial player – who goes first, x's or o's (decide who the players are)
# 4. Each person puts a spot on the board in a loop.
    # Show the board (physical indicator on screen)
    # Make sure they don't choose a location that's already been taken (verification)
    # Choose location, mark it.
    # Switch players
# 5. Until someone wins. – Exit Game!


## Step 1 – Create the Board 

def main():
    # create a list of rows, in which the rows contain lists
    board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    # How will we do this?  
    # board = [
    #     [r1_c1, r1_c2, r1_c3],
    #     [r2_c1, r2_c2, r2_c3],
    #     [r3_c1, r3_c2, r3_c3]
    # ]

    ## Step 2. Choose the initial player
    # Using a list may make it easier than having to do individual variables,which we did in rps
    active_player_index = 0
    players = ["Ivy", "Computer"]
    # We can use modulo to toggle if we wanted to.
    # active_player_index = (active_player_index + 1) % 2
    players[active_player_index]
    player_symbols = ["X", "O"]
    #List out current player, swap in while loop. 
    player = players[active_player_index] 

    # Step 4 – Until someone wins
    while not find_winnner(board):
        # Begin process of playing the round
        player = players[active_player_index] 
        symbol = player_symbols[active_player_index]
        announce_turn(player)
        show_board(board)
        if not choose_location(board, symbol):
            print("That isn't an option! Please try another spot.")
            continue

        # Toggle Active Player
        active_player_index = (active_player_index + 1) % len(players)

    print(f"Game Over: {player} has won with the board.")
    show_board(board)


def announce_turn(player):
    # SHOW THE BOARD
    print(f"It's {player}'s turn. Here's the board:")
    print()


def show_board(board):
    for row in board:
        # Begin by printing the separator, with "End" is presumably the way to end the row in place
        print("| ", end="")
        for cell in row:
            symbol = cell if cell is not None else "_"
            # Print each option and run through the different "pieces/names"
            print(symbol, end=" | ")
        print()


def choose_location(board, symbol):
    row = int(input("Choose which row: "))
    col = int(input("Choose which column: "))

    row -= 1
    col -= 1

    if row < 0 or row >= len(board):
        return False

    if col < 0 or col >= len(board[0]):
        return False

    cell = board[row][col]
    if cell is not None:
        return False

    board[row][col] = symbol
    return True

def find_winnner(board):
    # TODO: 3a Check for Winner

    # Win by rows

    # Win by columns

    # Win by diagonals
    return False


if __name__ == '__main__':
    main()