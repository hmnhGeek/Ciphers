import VigSquare as vgs
import keymaker

square = vgs.Vsquare()

def cipher(message, keyword):

    key = keymaker.make_key(message, keyword)

    message = message.upper()

    ciphertext = ''

    for i in range(len(message)):
        if message[i] in square[0]:
            row_char = key[i]
            col_char = message[i]

            row = square[0].index(row_char)
            col = square[0].index(col_char)
            
            ciphertext += square[row][col]
        else:
            ciphertext += message[i]

    return ciphertext


def decipher(ciphertext, keyword):

    key = keymaker.make_key(ciphertext, keyword)

    ciphertext = ciphertext.upper()
    deciphertext = ''

    for i in range(len(ciphertext)):
        if ciphertext[i] in square[0]:
            row_char = key[i]

            row = square[0].index(row_char)

            for char in square[row]:
                if char == ciphertext[i]:
                    deciphertext += square[0][square[row].index(char)]
        else:
            deciphertext += ciphertext[i]


    return deciphertext

    
