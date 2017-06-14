
direction = 'down'

def get_index(key, current):
    global direction
    mid = key - 1


    if direction == 'down':
        if current < mid:
            return current + 1
        else:
            direction = 'up'
            return current -1
    elif direction == 'up':
        if current > 0:
            return current - 1
        else:
            direction = 'down'
            return current + 1


def cipher(sentence, key, fixer = '~'):

    global direction
    direction = 'down'
    
    cols = len(sentence)
    rows = key

    matrix = [[fixer for i in range(cols)] for j in range(rows)]

    ind = -1
    for i in range(len(sentence)):
        ind = get_index(key, ind)
        matrix[ind][i] = sentence[i]

    ciphered = ''
    
    for row in matrix:
        for char in row:
            if char <> fixer:
                ciphered += char

    return ciphered


def decipher(sentence, key, fixer = '~'):

    global direction
    direction = 'down'
    
    cols = len(sentence)
    rows = key

    copy = sentence
    
    matrix = [[fixer for i in range(cols)] for j in range(rows)]

    ind = -1
    for i in range(len(sentence)):
        ind = get_index(key, ind)
        matrix[ind][i] = 0

    for row in matrix:
        for char in row:
            if char == 0:

                row[row.index(char)] = sentence[0]
                sentence = sentence[1::]

    deciphered = ''
    direction = 'down'
    
    ind = -1
    for i in range(len(copy)):
        ind = get_index(key, ind)
        deciphered += matrix[ind][i]

    return deciphered
