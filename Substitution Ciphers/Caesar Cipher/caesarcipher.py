from alphabets import __map__

def cipher(message, key):

    if key >= 1 and key < 52:
        orig_to_ref = __map__(key)[0]

        ciphertext = ''

        for i in message:
            if i in orig_to_ref:
                ciphertext += orig_to_ref[i]
            else:
                ciphertext += i

        return ciphertext
    else:
        return "Key must be in between 1 to 51, both inclusive."

    
def decipher(message, key):
    
    if key >= 1 and key < 52:
        ref_to_orig = __map__(key)[1]

        deciphertext = ''

        for i in message:
            if i in ref_to_orig:
                deciphertext += ref_to_orig[i]
            else:
                deciphertext += i

        return deciphertext
    else:
        return "Key must be in between 1 to 51, both inclusive."
