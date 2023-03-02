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
    print("The rules of the game go here")
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


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")
print(f"You chose {played_before} to played before")
print()

if played_before == "no":
    instructions()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)

print(f"You will be spending ${how_much}")

having_fun = yes_no("Are you having fun? ")
print(f"You said {having_fun} to having fun.")

print("Program continues")
