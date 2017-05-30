#####################
# CONSOLE UTILITIES #
#####################

import sys
import merkle_hellman as mh
import Caesar as c
import Vigenere as v


def again():
    print("*** AGAIN?? ***")
    option = input("(Y)es or (N)o")
    if option not in ['y', 'n', 'Y', 'N']:
        print("invalid choice.....re-enter")
        again()
    elif option in ['N', 'n']:
        print("Good Bye !")
        sys.exit()
    elif option in ['Y', 'y']:
        console()


def action():
    print("* ACTION *")
    option = input("(E)ncrypt or (D)ecrypt")
    if option not in ['E', 'D', 'e', 'd']:
        print("invalid choice....re-enter")
        action()
    elif option in ['E', 'e']:
        return 'e'
    elif option in ['D', 'd']:
        return 'd'


def console():
    print("*** TOOL ***")
    option = input("(C)aesar, (V)igenere or (M)erkle-Hellman?")
    if option not in ['C', 'V', 'M', 'c', 'v', 'm']:
        print("Invalid choice..retry..")
        console()
    elif option in ['C', 'c']:
        action_selected = action()
        if action_selected == 'e':
            word = input("Enter word to encrypt ").upper()
            print("Encrypting.....")
            print("***Encrypted word: ***", c.encrypt(word))
            print("Note it down to decrypt...")
            again()
        elif action_selected == 'd':
            word = input("Enter word to decrypt ").upper()
            print("Decrypting.....")
            print("Decrypted word: ", c.decrypt(word))
            again()

    elif option in ['v', 'V']:
        action_selected = action()
        if action_selected == 'e':
            word = input("Enter word to encrypt ").upper()
            key = input("Enter encryption key ").upper()
            print("Encrypting.....")
            print("***Encrypted word: ***", v.encrypt(word, key))
            print("Note it down to decrypt...")
            again()
        elif action_selected == 'd':
            word = input("Enter word to decrypt ").upper()
            key = input("Enter decryption key ").upper()
            print("Decrypting.....")
            print("Decrypted word: ", v.decrypt(word, key))
            again()


    elif option in ['M', 'm']:
        action_selected = action()
        if action_selected == 'e':
            print("Encrypting....")
            print("Generating private key....")
            private_key = mh.generate_private()
            public_key = mh.calculate_public_key(private_key)
            crypt = []
            message_file = input("Enter file name to be encrypted")
            with open(message_file, "r") as original:
                for word in original.readline():
                    crypt.append(mh.encrypt(word, public_key))
            original.close()
            LENGTH = len(crypt)
            encoded_file = input("Enter file name to store your code")
            # GENERATING CRYPTED CODE
            with open(encoded_file, "w") as cryptfile:
                for word in crypt:
                    cryptfile.write(str(word) + " ")
            cryptfile.close()
            mh.store_private_key(private_key)
            print("Your file is now encrypted to ", encoded_file)
            again()

        if action_selected == 'd':
            PRIVATE_KEY = mh.get_private_key()
            encoded_file = input("Enter file name to load your secret code from")
            with open(encoded_file, "r") as cryptfile:
                entire = cryptfile.readline()
                encoding = entire.split(sep=" ")
                decoded_file = input("enter file name to store your decoded message")
                with open(decoded_file, 'w') as decoded_f:
                    LENGTH = len(encoding) - 1
                    for i in range(0, LENGTH):
                        decoded_f.write(mh.decrypt(int(encoding[i]), PRIVATE_KEY))
                decoded_f.close()
            cryptfile.close()
            print("File", encoded_file, "has been decrypted and your secret message is stored in", decoded_file)
            again()

print("#### WELCOME TO THE CRYPTO SUITE ####")
console()
