#####################
#  VINGENERE CIPHER #
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


def get_shift(char):
    return (ord(char) - 65)


def modify_key(word, key):
    length_of_word = len(word)
    length_of_key = len(key)
    result_key = []

    if length_of_word <= length_of_key:
        for index, letter in enumerate(word):
            result_key.append(key[index])

    elif length_of_word > length_of_key:
        for index, letter in enumerate(word):
            result_key.append(key[(index % length_of_key)])

    return ''.join(result_key)


def encrypt(word, key):
    new_key = modify_key(word, key)
    result = []
    for index, letter in enumerate(word):
        displaced_character = encode(letter, get_shift(new_key[index]))
        result.append(displaced_character)

    return ''.join(result).upper()


def decrypt(word, key):
    new_key = modify_key(word, key)
    result = []
    for index, letter in enumerate(word):
        displaced_character = decode(letter, get_shift(new_key[index]))
        result.append(displaced_character)

    return ''.join(result).upper()
