from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import os
import time
import matplotlib.pyplot as plt
import numpy as np
import lorem
import random
import string

def aes_encryption(plain_text, key):
    cipher = AES.new(key, AES.MODE_CBC)
    cipher_text = cipher.encrypt(pad(plain_text, AES.block_size))
    return cipher.iv + cipher_text

def aes_decryption(cipher_text, key):
    iv = cipher_text[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    plain_text = unpad(cipher.decrypt(cipher_text[AES.block_size:]), AES.block_size)
    return plain_text

#key = get_random_bytes(16)
#plain_text = b'This is a test.'
#cipher_text = aes_encryption(plain_text, key)
#decrypted_text = aes_decryption(cipher_text, key)
#print(decrypted_text)



def otp_encryption(plain_text):
    key = os.urandom(len(plain_text))
    cipher_text = bytes([plain_text[i] ^ key[i] for i in range(len(plain_text))])
    return cipher_text, key

def otp_decryption(cipher_text, key):
    plain_text = bytes([cipher_text[i] ^ key[i] for i in range(len(cipher_text))])
    return plain_text

#plain_text = b'This is a test.'
#cipher_text, key = otp_encryption(plain_text)
#decrypted_text = otp_decryption(cipher_text, key)
#print(decrypted_text)




# Generate a dataset of 100 plain texts of varying lengths
#dataset = [lorem.text() for _ in range(100)]
dataset = [''.join(random.choices(string.ascii_letters + string.digits, k=random.randint(10**6, 10**7))) for _ in range(10)]

aes_times = []
otp_times = []

for plain_text in dataset:
    # Convert the plain text from str to bytes
    plain_text = plain_text.encode()

    # Measure execution time for AES
    start_time = time.time()
    key = get_random_bytes(16)
    cipher_text = aes_encryption(plain_text, key)
    decrypted_text = aes_decryption(cipher_text, key)
    end_time = time.time()
    aes_times.append(end_time - start_time)

    # Measure execution time for OTP
    start_time = time.time()
    cipher_text, key = otp_encryption(plain_text)
    decrypted_text = otp_decryption(cipher_text, key)
    end_time = time.time()
    otp_times.append(end_time - start_time)

# Create plot
fig, ax = plt.subplots()

plt.plot(aes_times, label='AES', marker='o')
plt.plot(otp_times, label='OTP', marker='o')

plt.xlabel('Plain Text Index')
plt.ylabel('Time (s)')
plt.title('Execution time by algorithm')
plt.legend()

plt.tight_layout()
plt.show()
