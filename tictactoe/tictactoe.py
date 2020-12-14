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
    players = [" You", "Computer"]
    # We can use modulo to toggle if we wanted to.
    active_player_index = (active_player_index + 1) % 2
    players[active_player_index]
    player_symbols = ["X", "O"]




if __name__ == '__main__':
    main()