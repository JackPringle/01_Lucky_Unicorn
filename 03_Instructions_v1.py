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


# Main Routine goes here...
played_before = yes_no("Have you played the game before? ")
print(f"You chose {played_before} to played before")
print()

if played_before == "no":
    instructions()

having_fun = yes_no("Are you having fun? ")
print(f"You said {having_fun} to having fun.")

print("Program continues")
