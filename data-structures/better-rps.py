import random


#use dictionaries to make it significantly easeir to check if we want.
rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper']
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors']
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock']
    },
}

def main():
    show_header()
    start_game("Jess", "AI")

def show_header():
    print("-----------------------------------")
    print("-------- Rock, Paper, Scissors v2 --------")
    print("-------- Data Structures Edition --------")
    print("-----------------------------------")

# Function to begin the game

def start_game(player_1, player_2):
    wins = { player_1: 0, player_2: 0}
    roll_names = list(rolls.keys())    

    while not find_winner(wins, wins.keys()):
        roll1 = get_roll(player_1, roll_names)
        roll2 = random.choice(roll_names)

        if not roll1:
            print("Can' play the game. Exiting.")
            break

        print(f"{player_1} rolls {roll1}.")
        print(f"{player_2} rolls {roll2}.")
        #We created a method out of this function and wrapped everything together. This helps to check an accurate winner.
        print(f"Current Win Status: {wins}")
        winner = check_winner(player_1, player_2, roll1, roll2)

        print("The game is over!")
        if winner is None:
            print("It was a tie!")
        else:   
            print(f"{winner} wins!")
            wins[winner] += 1
            
        print(f"Score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}.")
        print("----------------------")

    overall_winner = find_winner(wins, wins.keys())
    
    print(f"{overall_winner} wins the game! Thanks for playing!")


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name,0) >= best_of:
            return name
    
    return None

def check_winner(player_1, player_2, roll1, roll2):
    winner = None

    if roll1 == roll2:
        print("The game was a tie.")

    outcome = rolls.get(roll1, {})

    if roll2 in outcome.get('defeats'):
        return player_1
    elif roll2 in outcome.get('defeated_by'):
        return player_2

    return winner


def get_roll(player_name, roll_names):
    print("Available Rolls:")
    for index, r in enumerate(rolls, start=1):
        print(f"{index}. {r}")
        index += 1

    prompt = input(f"{player_name}, what is your roll? [rock, paper, scissors]: ")
    selected_index = int(prompt) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print(f"Sorry {player_name}, {prompt} is not a valid roll.")
        return None
    
    return roll_names[selected_index]


if __name__ == '__main__':
    main()