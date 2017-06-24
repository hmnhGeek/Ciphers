from reorder import reorder

def decipher(ciphertext, keyword):

    # generate original and reordered alphabets.
    original, shuffled = reorder(keyword)

    # initialise a deciphertext.
    deciphertext = ''

    for char in ciphertext:
        if char in shuffled:
            deciphertext += original[shuffled.index(char)]
        else:
            deciphertext += char

    return deciphertext
