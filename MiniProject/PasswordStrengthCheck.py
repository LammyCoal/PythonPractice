password = input('Enter your password: ')
length = len(password) >= 8
number = False
capital = False
symbols = False

symbol = "@#$%^&*()?"

for letter in password:
    if letter.isdigit():
        number = True
    elif letter in symbol:
        symbols = True
    elif letter.isupper():
        capital = True

if length and number and capital and symbols:
    print('Strong Password')
elif length and (number or capital or symbols):
    print('Medium Password')
else:
    print('Weak Password')


#To make it cleaner we can use this:
import string

def password_strength_check(pass_word):
    length_char = len(pass_word) > 8
    has_number = any(char.isdigit() for char in password)
    is_upper = any(char.upper() for char in password)
    is_lower = any(char.lower() for char in password)
    special = any(char in string.punctuation for char in password)

    score = sum([length_char, has_number, is_upper, is_lower, special])

    if score == 5:
        print('Strong Password')
    elif score >= 3:
        print('Medium Password')
    else:
        print('Weak Password')
