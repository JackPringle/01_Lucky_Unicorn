import random


# Functions go here...

# checks users enter yes / no to a given question
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"

        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")


# displays instructions, returns ""
def instructions():
    print("**** How to PLay ****")
    print()
    print("Thankyou for choosing to play Lucky Unicorn Game!")
    print("Enter the amount of money you would like to play with, then start your first round")
    print("To start the game, press <Enter>")
    print("Keep playing until you want to stop, but if you run out of money the game will end")
    print("Good luck player!")
    print()
    return ""


# Number check
def num_check(question, low, high):
    error = "Please enter a whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # Ask the question
            response = int(input(question))
            # If the amount is too low / too high give
            if low < response <= high:
                return response

            # Output an error
            else:
                print(error)

        except ValueError:
            print(error)


# decorates statements with given symbol
def statement_generator(statement, decoration, lines=None):
    sides = decoration * 5

    statement = f"{sides} {statement} {sides}"
    top_bottom = decoration * len(statement)

    if lines == 1:
        print(statement)

    else:
        print(top_bottom)
        print(statement)
        print(top_bottom)

    return ""


# Main Routine goes here...
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()

played_before = yes_no("Have you played the game before? ")
print(f"You chose {played_before} to played before")
print()

if played_before == "no":
    instructions()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)

balance = how_much

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
print()

while play_again == "":
    # increase # of rounds played
    rounds_played += 1

    # Print round number
    print(f"*** Round # {rounds_played} ***")

    chosen_num = random.randint(1, 100)

    # Adjust balance
    # if the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1

    # The token is either a horse or zebra...
    # in both cases subtract $0.50 from the balance
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = f"You got a {chosen}. Your balance is ${balance:.2f}"

    statement_generator(outcome, prize_decoration, 1)
    print()

    if balance < 1:
        # If balance is too low, exit the game and output a suitable message
        play_again = 'xxx'
        print("Sorry you have run out of money")
    else:
        play_again = input("Press Enter to play again or 'xxx' to quit")

print()

print(f'Final Balance: ${balance:.2f}')
