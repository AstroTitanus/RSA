from rsa import RSA
import helper as h

rsa = RSA()
print(rsa.public_key)
print(rsa.private_key)

encrypted = rsa.encrypt("ahoja")
print(encrypted)
# print(rsa.decrypt(encrypted))

# binary = h.str_to_bin("ahoj")
# print(h.bin_to_str(binary))

# ahoj = "ahoj"
# ahoj_binary = "{0:b8}".format(ahoj)

# print(binary)
# print(ahoj_binary)


# import time
# start = time.time()
# for i in range(20000):
#     a = public_key(26)
#     if a != 1:
#         print(f"i: {i}; Fail")
# end = time.time()
# print("Time consumed in working: ",end - start)