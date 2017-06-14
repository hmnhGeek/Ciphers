from rows_columns import *
from decip import decipher

def cipher(message, key, direction = 'clockwise', fixer = '~'):

    # first check if key is not 0 or 1 or key is equal to length of the message
    if key != 0 and key < len(message)-1 and key != 1 and key > 0:
    
        # design a matrix with no. of rows = key and no. of columns = roundoff(length of msg/key)
        rows = key
        if len(message) % key <> 0:
            cols = int(len(message)*key**(-1)) + 1
        else:
            cols = int(len(message)*key**(-1))

        # create a copy of the original message
        copy = message
        copy1 = message

        # now create the matrix
        matrix = [[fixer for i in range(cols)] for j in range(rows)]
        cpm = [[fixer for i in range(cols)] for j in range(rows)]
        
        # insert each character from message column wise
        for col in range(cols):
            for row in range(rows):
                try:
                    matrix[row][col] = copy[0]
                    copy = copy[1::]
                except:
                    pass

        for col in range(cols):
            for row in range(rows):
                try:
                    cpm[row][col] = copy1[0]
                    copy1 = copy1[1::]
                except:
                    pass


        # initialise a ciphered message
        ciphered = ''

        # consider if to tavel column or row first
        if direction == 'clockwise':
            rightmost = True
            leftmost = False
            bottommost = False
            topmost = False
            
            # run a while loop until all characters are popped out of matrix
            while cpm != [[fixer for i in range(rows)] for j in range(cols)]:
                try:
                    if rightmost:
                        col = find_rightmost(cpm, fixer)
                        
                        for row in range(rows):
                            if matrix[row][col] != fixer and fixer not in matrix[row][col]:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                                cpm[row][col] = fixer
                            elif matrix[row][col] == fixer:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer

                        rightmost = False
                        bottommost = True
                            
                    elif leftmost:
                        col = find_leftmost(cpm, fixer)

                        for row in range(rows-1, -1, -1):
                            if matrix[row][col] != fixer and fixer not in matrix[row][col]:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                                cpm[row][col] = fixer
                            elif matrix[row][col] == fixer:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer

                        leftmost = False
                        topmost = True
                        
                    elif bottommost:
                        row = find_bottommost(cpm, fixer)

                        for col in range(cols-1, -1, -1):
                            if matrix[row][col] != fixer and fixer not in matrix[row][col]:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                                cpm[row][col] = fixer
                            elif matrix[row][col] == fixer:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer

                        bottommost = False
                        leftmost = True
                        
                    elif topmost:
                        row = find_topmost(cpm, fixer)

                        for col in range(cols):
                            if matrix[row][col] != fixer and fixer not in matrix[row][col]:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                                cpm[row][col] = fixer
                            elif matrix[row][col] == fixer:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                        topmost = False
                        rightmost = True
                except:
                    break
                
                
        elif direction == 'anti-clockwise':
            rightmost = False
            leftmost = False
            bottommost = False
            topmost = True
            
            # run a while loop until all characters are popped out of matrix
            while cpm != [[fixer for i in range(rows)] for j in range(cols)]:
                try:
                    if rightmost:
                        col = find_rightmost(cpm, fixer)
                        
                        for row in range(rows-1, -1, -1):
                            if matrix[row][col] != fixer and fixer not in matrix[row][col]:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                                cpm[row][col] = fixer
                            elif matrix[row][col] == fixer:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer

                        rightmost = False
                        bottommost = True
                            
                    elif leftmost:
                        col = find_leftmost(cpm, fixer)

                        for row in range(rows):
                            if matrix[row][col] != fixer and fixer not in matrix[row][col]:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                                cpm[row][col] = fixer
                            elif matrix[row][col] == fixer:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer

                        leftmost = False
                        bottommost = True
                        
                    elif bottommost:
                        row = find_bottommost(cpm, fixer)

                        for col in range(cols):
                            if matrix[row][col] != fixer and fixer not in matrix[row][col]:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                                cpm[row][col] = fixer

                            elif matrix[row][col] == fixer:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer

                        bottommost = False
                        rightmost = True
                        
                    elif topmost:
                        row = find_topmost(cpm, fixer)

                        for col in range(cols-1, -1, -1):
                            if matrix[row][col] != fixer and fixer not in matrix[row][col]:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                                cpm[row][col] = fixer
                            elif matrix[row][col] == fixer:
                                ciphered += matrix[row][col]
                                matrix[row][col] += fixer
                                
                        topmost = False
                        leftmost = True
                except:
                    break

        return ciphered

        
    else:
        if key == 0:
            return "Key must not be 0."
        elif key == 1:
            return "Key must not be 1."
        elif key < 0:
            return "Key must be positive."
        elif key == len(message)-1:
            return "Key must be less than "+str(len(message)-1)+" for this message."
        elif key > len(message) or key == len(message):
            return "Key must be less than "+str(len(message)-1)+" for this message."


def decrypt(ciphertext, key, direction = 'clockwise', fixer = '~'):

    if key > 1:
        return decipher(ciphertext, key, direction, fixer)
    else:
        return "Key must be greater than 1."
