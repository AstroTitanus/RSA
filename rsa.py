"""

Helpful resources:
https://www.comparitech.com/blog/information-security/rsa-encryption/ (understanding rsa)
https://www.zditect.com/guide/python/mod-inverse-python.html (mod inverse)
"""

import numpy as np
from primes import random_prime
import helper as h

class RSA():
    
    def __init__(self, prime_len = 26):
        self.prime_len = prime_len
        self.primes = self.__primes()
        self.public_key = self.__public_key()
        self.private_key = self.__private_key()

    
    def __primes(self):
        """Generates two random prime numbers for rsa cipher

        Returns:
            dict: dict with keys 'p', 'q' and vals of the prime numbers
        """

        primes = {}
        primes['p'] = random_prime(self.prime_len)
        primes['q'] = random_prime(self.prime_len)

        return primes
    

    def __public_key(self):
        """Generates the public key values 'n' and 'e'

        Returns:
            touple: public key values
        """

        p = self.primes['p']
        q = self.primes['q']

        # n - first part of the public key
        prime_multiple = p*q

        # Carmichaels totient
        lcm = np.lcm.reduce(np.array([p-1, q-1]))
        
        # Generating e - second part of the public key
        if len(str(lcm)) <= 5:
            e = h.find_indivisible_to(len(str(lcm)) - 1, lcm)
        else:
            e = h.find_indivisible_to(5, lcm)

        # Sanity check
        assert h.gcd(e, lcm) == 1

        return (prime_multiple, e)
    

    def __private_key(self):
        """Generates the private key values 'n' and 'd'

        Returns:
            touple: private key values
        """

        p = self.primes['p']
        q = self.primes['q']

        # n - first part of the private key
        prime_multiple = p*q

        # Inverse modulo - second part of the private key
        d = pow(self.public_key[1], -1, int(np.lcm.reduce(np.array([p-1, q-1]))))

        return (prime_multiple, d)
    

    def encrypt(self, message):
        n = self.public_key[0]
        e = self.public_key[1]

        # Convert message to binary
        bin_message = h.str_to_bin(message)

        # Split binary to groups
        bin_message_groups = h.split_binary(bin_message, 32)

        # Encrypting
        result = ""
        for i, bit_group in enumerate(bin_message_groups):
            num = int(bit_group, 2)
            pow_result = pow(num, e, n)
            result += str(pow_result)
            # Output formatting
            if i < len(bin_message_groups)-1: result += "\n"

        return result
    

    def decrypt(self, encrypted):
        n = self.private_key[0]
        d = self.private_key[1]

        encrypted_groups = encrypted.split("\n")

        decrypted_bits = ""
        for group in encrypted_groups:
            decrypted_num = pow(int(group), d, n)
            decrypted_bits += str(bin(decrypted_num)[2:])
        
        decrypted_string = h.bin_to_str(decrypted_bits)

        return decrypted_string