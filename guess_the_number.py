from random import randrange
import math


def main():
    game_mode = int(input("Choose game mode \nUser to guess the number, Press 1 \nComputer to guess the number, Press 2 \n"))
    lower_bound = int(input("Please enter lower bound: "))
    upper_bound = int(input("Please enter upper bound: "))
    if game_mode == 1:
        guess_the_number_user(lower_bound, upper_bound)
    elif game_mode == 2:
        guess_the_number_computer(lower_bound, upper_bound)
    
    return 0



def guess_the_number_user(lower_bound, upper_bound):
    number_to_guess = randrange(lower_bound, upper_bound)
    user_guess = math.inf
    guess_counter = 0
    while number_to_guess != user_guess:
        guess_counter = guess_counter + 1
        user_guess = int(input(f"Guess the number between {lower_bound} and {upper_bound}: "))
        if user_guess < number_to_guess:
            print("Too small, try again: ")
        elif user_guess > number_to_guess:
            print("Too big, try again: ")

    print(f"Congratulations! You guessed the number {number_to_guess} in {guess_counter} tries")

    game_over = input("To return to main menu press the (m) button. To quit the game press ENTER ")
    if game_over == 'm':
        print("__________________________________________________________________________\n")
        main()

    return 0


def guess_the_number_computer(lower_bound, upper_bound):
    feedback = ' '
    computer_guess = math.inf
    guess_counter = 0 
    while feedback != 'c':
        guess_counter += 1
        computer_guess = randrange(lower_bound, upper_bound)
        feedback = input(f"Is {computer_guess} correct (c), too low (l) or too high (h): ")
        if feedback == 'l':
            lower_bound = computer_guess + 1
        elif feedback == 'h':
            upper_bound = computer_guess - 1
        if lower_bound == upper_bound:
            guess_counter += 1
            print(f"Only number left is {lower_bound}\n")
            computer_guess = lower_bound
            break

    print(f"Computer guessed the number {computer_guess} in {guess_counter} tries")

    game_over = input("To return to main menu press the (m) button. To quit the game press ENTER ")
    if game_over == 'm':
        print("__________________________________________________________________________\n")
        main()

    return 0


main()
