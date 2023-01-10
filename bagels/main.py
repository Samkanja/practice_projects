import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f'num of digits {NUM_DIGITS}')

    while True:
        secret_number = get_secret_number()

        number_of_guesses = 1

        while number_of_guesses <= MAX_GUESSES:
            guess = ''

            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f"Guess {number_of_guesses}")
                guess = input('>: ')

            clues = get_clues(guess, secret_number)
            print(clues)
            number_of_guesses += 1

            if guess == secret_number:
                break
            if number_of_guesses > MAX_GUESSES:
                print('ran out of geusses')
                print(f'secret number {secret_number}')

        print('do you want to play again')
        if not input('>: ').lower().startswith('y'):
            break
    print('Thank for playing')

def get_secret_number():
    secret_number = random.randrange(100,999)
    return str(secret_number)

def get_clues(guess, secret_number):
    '''Returns string with the Pico , Fermi, bagels clues for guess'''

    if guess == secret_number:
        return 'You got it'

    clues  = []
    for i in range(len(guess)):
        if guess[i] == secret_number[i]:
            clues.append('Fermi')
        elif guess[i] in secret_number:
            clues.append("Pico")
    if len(clues) == 0:
        return 'Bagels'
    else:
        return ''.join(clues)

if __name__ == '__main__':
    main()
        
        