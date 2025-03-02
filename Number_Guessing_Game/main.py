import random

print("Welcome to number guessing game! \nYou have got 5 attempts\nGuess a number between (1-10) ")

number_to_guess = random.randrange(1,10)

chances = 5

guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    my_guess = int(input("Enter you guess number "))

    if my_guess == number_to_guess:
        print(f"""The number is {number_to_guess} and you found it right
              in the {guess_counter} attempt!""")
        break
    
    elif guess_counter >= chances and my_guess != number_to_guess:
        print(f"Oops Sorry the number is {number_to_guess} better luck next time!")

    elif my_guess < number_to_guess:
        print("Your guess is very low. Try again.")

    elif my_guess > number_to_guess:
        print("Your guess is very high. Try again.")