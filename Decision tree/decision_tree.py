
def start():
    print("\nTesting decision structures.\n")


def exit():
    print("Exiting...")


def use_input():
    '''all input by user required in program'''

    while True:
        try:
            num = int(input("Insert a number: "))

            print(
                "\nOptions:\n1 - In one multi-branched decision \n2- In chained if-statements \n0 - Exit\n")

            choice = int(input("Your choice: "))

            break

        except:
            print("Invalid input!\n")

    return (choice, num)


def multi_brached(num):
    '''here only one operation will be done'''

    if (num >= 400):
        return num + 44

    elif (num >= 200):
        return num + 22

    elif (num >= 100):
        return num + 11

    else:
        return num

# print(multi_brached(90))


def chained(num):
    '''here calculating operation varies according to user input. can be calculated upto 3 times'''

    value3, value2, value1 = 0, 0, 0  # Initialize a invalid value

    if (num >= 400):
        value1 = 44

    if (num >= 200):
        value2 = 22

    if (num >= 100):
        value3 = 11

    else:
        return num

    return value1 + value2 + value3 + num


# print(chained(40))

def main():

    start()
    (choice, num) = use_input()

    if (choice == 1):
        result = multi_brached(num)
        print(f"\nResult is {result}\n")


    elif (choice == 2):
        result = chained(num)
        print(f"\nResult is {result}\n")

    elif (choice == 0):
        exit()

    else:
        print("Unknown option.")


main()