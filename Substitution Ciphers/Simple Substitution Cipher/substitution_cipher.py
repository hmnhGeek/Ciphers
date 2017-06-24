from cipher import cipher
from decipher import decipher

def encrypt(message, keyword, groupify = False):

    return cipher(message, keyword, groupify)

def decrypt(message, keyword):

    return decipher(message, keyword)
