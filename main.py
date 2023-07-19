def encode(password):
    res = ''
    for digit in password:
        encoded_digit = str(int(digit) + 3)
        res += encoded_digit
    return res


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
        password = str(input('Please enter your password to encode: '))
        encoded_password = encode(password)
        print('Your password has been encoded and stored!')
        print()
    elif option == 2:
        print(f'The encoded password is {encoded_password}, and the original password is {password}')
        print()
    else:
        menu = False
