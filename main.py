# Paul DeHart
def encode(password):
    res = ''
    for digit in password:
        # encode each digit by increasing value by 3
        encoded_digit = str(int(digit) + 3)
        res += encoded_digit
        # store each digit and return result
    return res

def decode(encoded_password):
    #decoding function
    res = ""
    for digit in encoded_password:
        decoded_digit = str((int(digit) - 3))
        res += decoded_digit
    return res

def main():
    menu = True
    while menu:
        print('Menu')
        print('-------------')
        print('1. Encode')
        print('2. Decode')
        print('3. Quit')
        print()
        option = int(input('Please enter an option: '))
        if option == 1:
            # take user input for password and encode using encode function
            password = str(input('Please enter your password to encode: '))
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
            print()
        elif option == 2:
            # print the encoded password and original password
            print(f'The encoded password is {encoded_password}, and the original password is {password}')
            print()
        else:
            # exit menu
            menu = False
