import os
from ciphers.caesar import Caesar
from ciphers.rail_fence import RailFence
from ciphers.viegnere import Viegnere
from ciphers.matrix import Matrix


def do_option(option: int, mode_option: int, text: str, key: str):
    if option == 1:
        rail_fence = RailFence(int(key))

        if mode_option == 1:
            print("Zaszyfrowany tekst: {}".format(rail_fence.encode(text)))
        else:
            print("Odszyfrowany tekst: {}".format(rail_fence.decode(text)))

    if option == 2:
        viegnere = Viegnere()

        if mode_option == 1:
            print("Zaszyfrowany tekst: {}".format(viegnere.encode(text, key)))
        else:
            print("Odszyfrowany tekst: {}".format(viegnere.decode(text, key)))

    if option == 3:
        matrix = Matrix(key)

        if mode_option == 1:
            print("Zaszyfrowany tekst: {}".format(matrix.encode(text)))
        else:
            print("Odszyfrowany tekst: {}".format(matrix.decode(text)))

    if option == 4:
        caesar = Caesar(int(key))

        if mode_option == 1:
            print("Zaszyfrowany tekst: {}".format(caesar.encode(text)))
        else:
            print("Odszyfrowany tekst: {}".format(caesar.decode(text)))

    if option > 4:
        print("Zla opcja!")

    return


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause_console():
    os.system('pause' if os.name == 'nt' else "read -rsp $'Press any key to continue...\n' -n 1 key")


def main():

    while True:
        clear_console()
        print("1. Szyfr Rail Fence")
        print("2. Szyfr Viegnera")
        print("3. Przestawienia macierzowe")
        print("4. Szyfr Cezara")
        print("0. Wyjscie")
        option = int(input("Opcja: "))

        if option == 0:
            break

        else:
            print("\n1. Szyfrowanie")
            print("2. Odszyfrowanie")
            mode_option = int(input("Opcja: "))

            text = input("\nPodaj tekst do zaszyfrowania: ")
            key = input("Podaj klucz: ")
            do_option(option, mode_option, text, key)
            pause_console()


if __name__ == '__main__':
    main()
