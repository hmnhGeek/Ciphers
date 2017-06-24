from reorder import reorder

def cipher(message, keyword, groupify = False):

    # generate the orignal and re-ordered alphabets.
    original, shuffled = reorder(keyword)

    # initialise a ciphertext.
    ciphertext = ''

    for char in message:
        if char in original:
            anchor = original.index(char)
            ciphertext += shuffled[anchor]
        else:
            # copy it as it is in the ciphertext.
            ciphertext += char

    if not groupify:
        return ciphertext

    else:
        # omit punctuations and make groups of four.
        count = 0
        new_ciphertext = ''
        
        while ciphertext <> '':

            if count < 5:
                if ciphertext[0] in original:
                    new_ciphertext += ciphertext[0]
                    ciphertext = ciphertext[1::]
                    count += 1
                else:
                    ciphertext = ciphertext[1::]
            else:
                new_ciphertext += ' '
                count = 0

        return new_ciphertext

    
    
