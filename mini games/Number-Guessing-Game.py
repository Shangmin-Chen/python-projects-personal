from random import randint, choice

random_number = randint(1, 100)


def guess():
    try:
        # user input
        user = input("Guess a number? ")
        # win condition
        if str(user) == str(random_number):
            print("\nNice, you did it!")
        else:
            # hint condition
            print("\ntry again\n")
            difference = abs(random_number - int(user))
            another = randint(1, 100)
            # random choice to choose to give hint of
            choice_list = [difference, difference + another, difference - another, difference * another,
                           difference / another, difference ** 2, difference ** (1 / 2)]
            operation = choice(choice_list)
            if operation == choice_list[0]:
                print("you are " + str(operation) + " away from the number!\n")
                guess()
            # these are all opposite operation, if the choice_list has addition then the print statement
            # would give the hint of subtraction
            elif operation == choice_list[1]:
                print("you are " + str(operation) + " subtracted by " + str(another) + " away from the number!\n")
                guess()
            elif operation == choice_list[2]:
                print("you are " + str(operation) + " added by " + str(another) + " away from the number!\n")
                guess()
            elif operation == choice_list[3]:
                print("you are " + str(operation) + " divided " + str(another) + " away from the number!\n")
                guess()
            elif operation == choice_list[4]:
                print("you are " + str(operation) + " times " + str(another) + " away from the number!\n")
                guess()
            elif operation == choice_list[5]:
                print("you are square root of " + str(operation) + " away from the number!\n")
                guess()
            elif operation == choice_list[6]:
                print("you are " + str(operation) + " squared away from the number!\n")
                guess()

    # try and except for value error, aka if user inputs letters instead of numbers
    except ValueError:
        "value error, try again"
        guess()


# initializing the code
guess()
