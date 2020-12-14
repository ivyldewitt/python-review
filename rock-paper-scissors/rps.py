import random

def main():
    show_header()

    player = "Jessie"
    ai = "Computer"

    start_game(player, ai)

def show_header():
    print("-----------------------------------")
    print("-------- Rock, Paper, Scissors Game --------")
    print("-----------------------------------")

# Function to begin the game

def start_game(player_1, player_2):
    rounds = 3

    wins_p1 = 0
    wins_p2 = 0

    rolls = [
        'rock',
        'paper',
        'scissors'
    ]       

    while wins_p1 < rounds and wins_p2 < rounds:
        roll1 = get_roll(player_1, rolls)
        roll2 = random.choice(rolls)

        if not roll1:
            print("Can' play the game. Exiting.")
            continue

        print(f"{player_1} rolls {roll1}.")
        print(f"{player_2} rolls {roll2}.")
        #We created a method out of this function and wrapped everything together. This helps to check an accurate winner.
        winner = check_winner(roll1, roll2, player_2, player_1)

        # print("The game is over!")
        if winner is None:
            print("It was a tie!")
        else:   
            print(f"{winner} wins!")
            if winner == player_1:
                wins_p1 += 1
            elif winner == player_2:
                wins_p2 += 1

        print(f"Score is {player_1}: {wins_p1} and {player_2}: {wins_p2}.")
        print("----------------------")

    overall_winner = None
    if wins_p1 >= rounds:
        overall_winner = player_1
    else:
        overall_winner = player_2
    
    print(f"{overall_winner} wins the game! Thanks for playing!")

def check_winner(roll1, roll2, player_2, player_1):
    winner = None

    if roll1 == roll2:
        print("The game was a tie.")
    elif roll1 == 'rock':
        if roll2 == 'paper':
            winner = player_2
        elif roll2 == 'scissors':
            winner == player_1
    elif roll1 == 'paper':
        if roll2 == 'scissors':
            winner = player_2
        elif roll2 == 'rock':
            winner = player_1
    elif roll1 == 'scissors':
        if roll2 == 'rock':
            winner = player_2
        elif roll2 == 'scissors':
            winner = player_1
    return winner


def get_roll(player_name, rolls):
    print("Available Rolls:")
    for index, r in enumerate(rolls, start=1):
        print(f"{index}. {r}")
        index += 1

    prompt = input(f"{player_name}, what is your roll? [rock, paper, scissors]: ")
    selected_index = int(prompt) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        text = selected_index + 1
        print(f"Sorry {player_name}, {text} is not a valid roll.")
        return None
    
    return rolls[selected_index]


if __name__ == '__main__':
    main()