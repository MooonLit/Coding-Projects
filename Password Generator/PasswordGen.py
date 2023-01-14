import random
user_input = str(input('Enter a Passowrd:\n'))

for character in user_input:
    if character == ' ':
        print(' ', end='')
    elif character != ' ':
        character = ord(character) + random.randint(0, 9)
        print(chr(character), end='')
