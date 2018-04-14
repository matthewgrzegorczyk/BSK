import os
from crypto.enigma import Enigma


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause_console():
    os.system('pause' if os.name == 'nt' else "read -rsp $'Press any key to continue...\n' -n 1 key")


def do_option(option, rotor_count, key):
    enigma = Enigma(key, rotor_count)
    if option == 1:
        text = input('Podaj tekst do zaszyfrowania: ')
        crypted = enigma.crypt(text)
        print('Odszyfrowany tekst: {}'.format(crypted))

    elif option == 2:
        text = input('Podaj tekst do odszyfrowania')
        crypted = enigma.crypt(text)
        print('Zaszyfrowany tekst: {}'.format(crypted))

    else:
        print('Zła opcja!')


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
        pause_console()


if __name__ == "__main__":
    main()
