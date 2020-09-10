# First Project Intro – the Classic Guessing Game

import random

def main():
    setup_game()
    guessing()



print("-----------------------------------")
print("-------- M&M Guessing Game --------")
print("-----------------------------------")

# Setup game requirements.


def setup_game():
    print("Guess the number & you get lunch on the house!")
    print()
    mm_count = random.randint(1,100)
    attempt_max = 5
    attempts = 0
    return attempts, attempt_max, mm_count

# sanity testing that the break statement was working as intended. 
# print(mm_count)

# Loop over requirements.

def guessing():
    while attempts < attempt_max:
        guess_str = input("How many M&M do you think there are in the jar? ")
        guess = int(guess_str)
        attempts += 1
        if mm_count == guess:
            print(f"Congratulations you won! It was {mm_count} and you guessed it in {attempts} attempts! Enjoy your free lunch!")
            break
        elif mm_count < guess:
            print("You need to guess a bit lower!")
        else: 
            print("You need to guess a bit higher!")
    print("Thanks for playing!")

    
    



if __name__ == '__main__':
    main()