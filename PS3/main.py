import os

from PS3.algos.lfsr import LFSR
from PS3.algos.ssc import SSC
from PS3.algos.ca import CA

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause_console():
    os.system('pause' if os.name == 'nt' else "read -rsp $'Press any key to continue...\n' -n 1 key")


def do_option(option):
    polynomal_sum = input("Podaj po przecinku: ")
    polynomal = list(map(int, polynomal_sum.split(',')))

    if option == 1:
        lfsr = LFSR(polynomal)
        while True:
            print('{}'.format(lfsr.next_int()))

    if option == 2 or option == 3:
        result = ''
        seed = input("Podaj ziarno (liczbę całkowitą): ")
        print("\n1. Szyfrowanie")
        print("2. Odszyfrowanie")
        mode_option = int(input("Opcja: "))

        if mode_option == 1:
            text = input("\nPodaj tekst do zaszyfrowania: ")
            type = 'Zaszyfrowany tekst:'
        else:
            text = input("\nPodaj tekst do odszyfrwania: ")
            type = 'Odszyfrowany tekst:'

        if option == 2:
            ssc = SSC(polynomal, seed)
            result = ssc.crypt(text)

        if option == 3:
            ca = CA(polynomal, seed)

            if mode_option == 1:
                result = ca.encrypt(text)
            else:
                result = ca.decrypt(text)

        print('{} {}'.format(type, result))


def main():
    while True:
        clear_console()
        print("1. LFSR")
        print("2. Synchronous Stream Cipher")
        print("3. Ciphertext Autokey")
        print("0. Wyjscie")
        option = int(input("Opcja: "))

        if option == 0:
            break

        else:
            do_option(option)
            pause_console()


if __name__ == '__main__':
    main()
