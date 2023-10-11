def welcome():
    '''to print welcome message for user'''
    print('''Welcome to the Caesar Cipher
This program encrypts and decrypts text with the Caesar Cipher.
''')


def enter_message():
    '''to ask user whether to encrypt or decrypt'''

    mode = input("Would you like to encrypt (e) or decrypt (d): ").lower()
    while mode not in ["e", "d"]:
        mode = input("You have entered invalid input! Enter again encrypt (e) or decrypt (d): ")

    #to ask user what's the message is
    message_or_file = input("Would you like to read from a file (f) or the console (c): ").lower()
    while message_or_file not in ["f", "c"]:
        message_or_file = input("You have entered invalid input! Enter again read from a file (f) or the console (c): ").lower()

    if message_or_file == "f":
        filename = input("Enter a filename: ")
        try:
            with open(filename, "r") as f:
                message = f.read().upper()
        except FileNotFoundError:
            print("File not found.")
            return None, None, None
        
    elif message_or_file == "c":
        message = input("What message would you like to {}: ".format(mode)).upper()

    while True:
        # Using try and except so that if the user inputs a wrong shift value, it goes to the except and prints an error.
        try:
            shift = int(input("What is the shift number:"))
            break
        except ValueError:
            print("Please enter a valid integer for the shift number.")

    return mode, message, shift


def encrypt(message, shift):
    '''to encrypt users message'''

    encrypted_message = ""
    for letter in message:
        if letter.isalpha():
            encrypted_letter = chr((ord(letter) + shift - 65) % 26 + 65)
        else:
            encrypted_letter = letter
        encrypted_message += encrypted_letter
    return(encrypted_message)


def decrypt(message, shift):
    '''to decrypt message'''
    decrypted_message = ""
    for letter in message:
        if letter.isalpha():
            decrypted_letter = chr((ord(letter) - shift - 65) % 26 + 65)
        else:
            decrypted_letter = letter
        decrypted_message += decrypted_letter
    return(decrypted_message)


def process_file(filename, shift):
    '''to read the file data'''
    with open(filename, "r") as f:
        text = f.readlines()

    encrypted_text = []
    for message in text:
        encrypted_message = encrypt(message, shift)
        encrypted_text.append(encrypted_message)

    return encrypted_text


def is_file(filename):
    '''This is used to check whether the file name is valid or not'''
    try:
        with open(filename, "r") as f:
            pass
    except FileNotFoundError:
        return False
    else:
        return True


def write_text(text):
    '''to creat new file for result data'''
    with open("result.txt", "w") as f:
        for message in text:
            f.write(message + "\n")


def main():
    '''to implement all function in one to make caesar cipher'''
    welcome()
    while True:
        #if any error occure user get reason of error without crash
        try:
            mode, message, shift = enter_message()

            if mode == "e":
                encrypted_message = encrypt(message, shift)
                print("Encrypted message: {}".format(encrypted_message))
                print()
                write_text([encrypted_message])

            else:
                decrypted_message = decrypt(message, shift)
                print("Decrypted message: {}".format(decrypted_message))
                print()
                write_text([decrypted_message])

            another_message = input("Would you like to encrypt or decrypt another message? (y/n): ")
            if another_message == "n":
                break
        except Exception as e:
            print(e)
    print()
    print("Thanks for using the program, goodbye!")


if __name__ == "__main__":
    main()


