# First Project Intro – the Classic Guessing Game

import random


def main():
    show_header()
    mm_count = random.randint(1,100)
    set_rand_num()
    guessing(mm_count)  

def show_header():
    print("-----------------------------------")
    print("-------- M&M Guessing Game --------")
    print("-----------------------------------")

# Setup game requirements.

def set_rand_num():
    print("Guess the number & you get lunch on the house!")

# sanity testing that the break statement was working as intended. 
# print(mm_count)

# Loop over requirements.

def guessing(count):
    attempt_max = 5
    attempts = 0
    while attempts < attempt_max:
        guess_str = input("How many M&M do you think there are in the jar? ")
        guess = int(guess_str)
        attempts += 1
        if count == guess:
            print(f"Congratulations you won! It was {mm_count} and you guessed it in {attempts} attempts! Enjoy your free lunch!")
            break
        elif count < guess:
            print("You need to guess a bit lower!")
        else: 
            print("You need to guess a bit higher!")
    print("Thanks for playing!")

    

if __name__ == '__main__':
    main()

