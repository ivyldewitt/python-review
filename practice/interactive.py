### PRACTICE ###

user_prompt = input("Please enter a whole number (no decimals): ")
user_int = int(user_prompt)


## Write a program that requests a number from the user. 
# Have the program print "Even" or "Odd" depending on whether 
# they entered an even or odd number.

while user_int != 0:

    if user_int % 2 == 0:
        print(f"It looks like {user_int} is an EVEN number!")
    else:
        print(f"{user_int} is an ODD number.")
    # I'm curious if there's a more efficient way to do this. I initially broke the loop instead of repeating this twice.
    user_prompt = input("Please enter a whole number (no decimals): ")
    user_int = int(user_prompt)


print("Thanks for playing!")
