##########################
#  MERKLE HELLMAN CIPHER #
##########################
import utils
import random


# creates super increasing sequence
def create_super_increasing():
    sequence = []
    initial = random.randint(2, 10)
    total = initial
    sequence.append(initial)
    for i in range(7):
        new = random.randint(total + 1, 2 * total)
        total = total + new
        sequence.append(new)
    return [sequence, total]


# find co prime of Q
def find_coprime(q):
    while True:
        temp = random.randint(2, q - 1)
        if (utils.coprime(temp, q)):
            return temp


def generate_private():
    temp = create_super_increasing()
    super_sequence = temp[0]
    # total_seq
    total_seq = temp[1]

    # value of Q
    Q = random.randint(total_seq + 1, total_seq * 2)

    # value of R
    R = find_coprime(Q)

    # PRIVATE KEY
    return [super_sequence, Q, R]


def calculate_public_key(private_key):
    sequence = private_key[0]
    q = private_key[1]
    r = private_key[2]
    key = []
    for i in range(8):
        temp = r * sequence[i] % q
        key.append(temp)
    return key


def encrypt(char, public_key):
    char_array = utils.byte_to_bits(ord(char))
    cipher = 0
    total = 0
    for i in range(0, 8):
        temp = char_array[i] * public_key[i]
        total = total + temp
    cipher = total
    return cipher


def decrypt(char, private_key):
    c = char
    super_sequence = private_key[0]
    q = private_key[1]
    r = private_key[2]
    s = utils.modinv(r, q)
    # decrypt step 1
    c1 = c * s % q
    temp = c1
    value = []
    i = 7
    while i >= 0:
        if (super_sequence[i] <= temp):
            temp = temp - super_sequence[i]
            i = i - 1
            value.append(1)
        else:
            value.append(0)
            i = i - 1
    value.reverse()
    ans = utils.bits_to_byte(value)
    return chr(ans)


def store_private_key(private_k):
    private_file = "private.txt"
    with open(private_file, 'w') as private_f:
        private_f.write(str(private_k))
    private_f.close()

def get_private_key():
    print("Refer private.txt to access the private key")
    list1 = []
    pri = []
    print("Enter values from your private key file :)")
    print("Enter initial sequence")
    for i in range(8):
        temp_seq = int(input("enter sequence number"))
        list1.append(temp_seq)
    q = int(input("Enter code 1 / value of q"))
    r = int(input("Enter code 2 / value of r"))
    pri.append(list1)
    pri.append(q)
    pri.append(r)
    return pri

