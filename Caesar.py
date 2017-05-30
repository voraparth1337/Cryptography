#####################
#  CAESAR CIPHER    #
#####################

def encode(char, shift):
    char_value = ord(char)
    char_shifted_value = char_value + shift
    if char_shifted_value > 90:
        coded_value = char_shifted_value - (ord("Z") - ord("A")) - 1
        return chr(coded_value)
    else:
        return chr(char_shifted_value)


def decode(char, shift):
    char_value = ord(char)
    char_shifted_value = char_value - shift
    if char_shifted_value < 65:
        coded_value = char_shifted_value + (ord("Z") - ord("A")) + 1
        return chr(coded_value)
    else:
        return chr(char_shifted_value)


def encrypt(word):
    result = []
    for letter in word:
        displaced_character = encode(letter, 3)
        result.append(displaced_character)
    return ''.join(result).upper()


def decrypt(word):
    result = []
    for letter in word:
        displaced_character = decode(letter, 3)
        result.append(displaced_character)
    return ''.join(result).upper()
