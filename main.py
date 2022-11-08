from rsa import RSA
import helper as h
import string
import random

# string module constants
special_chars = list("ľščťžýáíéň§úřóď")
alphabet = special_chars + list(string.ascii_letters) + list(string.ascii_lowercase) + list(string.ascii_uppercase) + list(string.digits) + list(string.hexdigits) + list(string.whitespace) + list(string.punctuation)


def random_string(alphabet):
    rand_length = random.randint(1, 50)
    rand_string = ''
    for _ in range(rand_length):
        rand_index = random.randint(0, len(alphabet) - 1)
        rand_string += alphabet[rand_index]
    
    return rand_string


for i in range(10000):
    rsa = RSA()

    to_encrypt = random_string(alphabet)
    # print(f"'{to_encrypt}'")
    encrypted = rsa.encrypt(to_encrypt)
    decrypted = rsa.decrypt(encrypted)

    if to_encrypt != decrypted:
        print(f"{type(to_encrypt)} {len(to_encrypt)} '{to_encrypt}'")
        print(f"{type(decrypted)} {len(decrypted)} '{decrypted}'")

    assert to_encrypt == decrypted