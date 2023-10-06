
def welcome():
    '''Welcoming the user'''
    print("\n\nWelcome to unit conversion program.\n")

# welcome()


def choose_option():
    '''aske the User to choose type of conversion they like.'''

    print(('''Optins below:\n1 - Gram to pounds\n2 - Length conversions\n0 - Exit\n'''))

    choice = 99  # Initialize choice to invalid values

    while choice not in [0, 1, 2]:

        try:
            choice = int(input("Your Choice: "))
        except:
            print("Invalid option! \n")

    # print(choice)

    return choice


# choose_option()

def weight():
    '''Grams to pounds'''

    while True:
        try:
            gram = float(input("Insert grams: "))
            break
        except:
            print("Enter correct option\n")

    pound = gram/453.6

    # rounding the value to 3 digits after the decimal point
    pound = (round(pound, 3))

    print(f"\n{gram} grams converts to {pound} pounds.\n")

# print(weight())


def length():
    '''Conversion of Length'''

    print("Select units from list: \n1 - Millimeters  \n2 - Meters \n3 - Kilometers")

    source, target = 0, 0  # Initialize source and target to invalid values
    while source not in [1, 2, 3] or target not in [1, 2, 3]:

        try:
            source = int(input("Source unit(1-3): "))
            target = int(input("Target unit(1-3): "))
            distace = float(input("Insert distance: "))

        except:
            print("Enter a number\n")

        else:
            print("Invalid input!\n")

    # lenght conversion formula
    mm_to_m = 1 / 1000
    mm_to_km = 1 / 1_000_000
    m_to_mm = 1000
    m_to_km = 1 / 1000
    km_to_mm = 1_000_000
    km_to_m = 1000

    # logic to use formula as required
    if (source == 1 and target == 1):
        print(f" {distace} mm ")
    elif (source == 1 and target == 2):
        print(f" {distace} mm converts to { mm_to_m * distace} m ")

    elif (source == 1 and target == 3):
        print(f" {distace} mm converts to  {distace * mm_to_km} km ")

    elif (source == 2 and target == 1):
        print(f" {distace} m converts to  {distace * m_to_mm} mm")

    elif (source == 2 and target == 2):
        print(f" {distace} m  ")

    elif (source == 2 and target == 3):
        print(f" {distace} m converts to  {distace* m_to_km} km ")

    elif (source == 3 and target == 1):
        print(f" {distace} km converts to  {distace * km_to_mm} mm ")

    elif (source == 3 and target == 2):
        print(f" {distace} km converts to  {distace * km_to_m} m ")

    elif (source == 3 and target == 3):
        print(f" {distace} km ")

    else:
        print("Input may be wrong!")
    print("")
# print(length())


def exit():

    print("\nThanks for using the Converter\n")


def main():
    '''Main function of the program'''

    # to welcome user
    welcome()

    while (True):
        # asking the User to choose type of conversion they like
        choice = choose_option()
        print("")

        if (choice == 0):
            exit()
            break
        elif (choice == 1):
            weight()
        elif (choice == 2):
            length()


main()
