import os
from crypto.enigma import Enigma


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def do_option(option, rotor_count, key):
    enigma = Enigma(key, rotor_count)

    encrypted = enigma.crypt('ALFA')
    print('Tekst zaszyfrowany: {}'.format(encrypted))


def main():
    while True:
        clear_console()
        print('1. Szyfrowanie tekstu')
        print('2. Odsztfrowanie tekstu')
        print('0. Wyjście')

        option = int(input("Opcja: "))

        if option == 0:
            break

        rotor_count = int(input('Liczba rotorów: '))
        key = input('Klucz: ')

        do_option(option, rotor_count, key)


if __name__ == "__main__":
    main()
