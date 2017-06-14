
from decipheraid import *

def decipher(coded, key, direction = 'clockwise', fixer = '~'):

    copy = coded
    
    rows = key
    cols = int(len(coded)*key**(-1))

    matrix = [[fixer for i in range(cols)] for j in range(rows)]
    cpm = [[fixer for i in range(cols)] for j in range(rows)]

    if direction == 'clockwise':
        
        rightmost, bottommost, leftmost, topmost = True, False, False, False

        while cpm <> [[fixer*2 for i in range(cols)] for j in range(rows)]:
            #try:
            if rightmost:

                col = find_rightmost(cpm, fixer)
               
                for row in range(rows):
                    try:
                        if cpm[row][col] <> fixer*2:
                            matrix[row][col] = copy[0]
                            copy = copy[1::]
                            cpm[row][col] += fixer
                    except:
                        if cpm[row][col] <> fixer*2:
                            cpm[row][col] += fixer

                rightmost = False
                bottommost = True

            elif bottommost:

                row = find_bottommost(cpm, fixer)

                for col in range(cols-1, -1, -1):
                    try:
                        if cpm[row][col] <> fixer*2:
                            matrix[row][col] = copy[0]
                            copy = copy[1::]
                            
                            cpm[row][col] += fixer
                    except:
                        if cpm[row][col] <> fixer*2:
                            cpm[row][col] += fixer

                bottommost = False
                leftmost = True

            elif leftmost:

                col = find_leftmost(cpm, fixer)

                for row in range(rows-1, -1, -1):
                    try:
                        if cpm[row][col] <> fixer*2:
                            matrix[row][col] = copy[0]
                            copy = copy[1::]
                            
                            cpm[row][col] += fixer
                    except:
                        if cpm[row][col] <> fixer*2:
                            cpm[row][col] += fixer

                leftmost = False
                topmost = True

            elif topmost:

                row = find_topmost(cpm, fixer)

                for col in range(cols):
                    try:
                        if cpm[row][col] <> fixer*2:
                            matrix[row][col] = copy[0]
                            copy = copy[1::]
                            
                            cpm[row][col] += fixer
                    except:
                        if cpm[row][col] <> fixer*2:
                            cpm[row][col] += fixer

                topmost = False
                rightmost = True





    elif direction == 'anti-clockwise':
    
        rightmost, bottommost, leftmost, topmost = False, False, False, True

        while cpm <> [[fixer*2 for i in range(cols)] for j in range(rows)]:
            #try:
            if rightmost:

                col = find_rightmost(cpm, fixer)
               
                for row in range(rows-1, -1, -1):
                    try:
                        if cpm[row][col] <> fixer*2:
                            matrix[row][col] = copy[0]
                            copy = copy[1::]
                            cpm[row][col] += fixer
                    except:
                        if cpm[row][col] <> fixer*2:
                            cpm[row][col] += fixer

                rightmost = False
                bottommost = True

            elif bottommost:

                row = find_bottommost(cpm, fixer)

                for col in range(cols):
                    try:
                        if cpm[row][col] <> fixer*2:
                            matrix[row][col] = copy[0]
                            copy = copy[1::]
                            
                            cpm[row][col] += fixer
                    except:
                        if cpm[row][col] <> fixer*2:
                            cpm[row][col] += fixer

                bottommost = False
                rightmost = True

            elif leftmost:

                col = find_leftmost(cpm, fixer)

                for row in range(rows):
                    try:
                        if cpm[row][col] <> fixer*2:
                            matrix[row][col] = copy[0]
                            copy = copy[1::]
                            
                            cpm[row][col] += fixer
                    except:
                        if cpm[row][col] <> fixer*2:
                            cpm[row][col] += fixer

                leftmost = False
                bottommost = True

            elif topmost:

                row = find_topmost(cpm, fixer)

                for col in range(cols-1, -1, -1):
                    try:
                        if cpm[row][col] <> fixer*2:
                            matrix[row][col] = copy[0]
                            copy = copy[1::]
                            
                            cpm[row][col] += fixer
                    except:
                        if cpm[row][col] <> fixer*2:
                            cpm[row][col] += fixer

                topmost = False
                leftmost = True

        

        
    decoded = ''
        
    for col in range(cols):
        for row in range(rows):
            decoded += matrix[row][col]

    return decoded.rstrip(fixer)
        
