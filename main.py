# Authors: Alexander Wang + Lucas Gavrielides

# These are used to import methods
import decode
import encode


# Menu and User prompts
while True:
    print('Menu')
    print('-------------')
    print('1. Encode')
    print('2. Decode')
    print('3. Quit\n')

    option = int(input('Please enter an option: '))
    # User picked options are parsed by the if statements!
    if option == 1:
        original_password = input('Please enter your password to encode: ')
        if len(original_password) == 8 and original_password.isnumeric():
            encoded_password = encode.encode(original_password)
            print('Your password has been encoded and stored!\n')
            continue
        else:
            print('Invalid Input! Password contains more than 8 digits or contains a letter! \n ')

    if option == 2:
        # Decode and encode are both revealed!
        print(f'The encoded password is {encoded_password}, and the original password is {decode.decode(encoded_password)}.\n')
    if option == 3:
        # Menu stops!
        break


