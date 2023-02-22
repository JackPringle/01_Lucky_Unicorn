# Ask users for a number
get_number = int(input("Choose a number? "))

# Multiply the number by 5
times_five = get_number * 5

answer = "{} time five is equal to " \
        "{}".format(get_number, times_five)

# Output the result
print(answer)


