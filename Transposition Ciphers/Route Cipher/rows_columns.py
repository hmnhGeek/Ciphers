def getdim(matrix):
    return len(matrix), len(matrix[0])

def find_rightmost(matrix, fixer):

    rows, cols = getdim(matrix)

    for col in range(cols-1, -1, -1):
        for row in range(rows):
            if matrix[row][col] != fixer:
                return col

def find_leftmost(matrix, fixer):
    
    rows, cols = getdim(matrix)

    for col in range(cols):
        for row in range(rows):
            if matrix[row][col] != fixer:
                return col

def find_bottommost(matrix, fixer):
    
    rows, cols = getdim(matrix)

    for row in range(rows-1, -1, -1):
        for col in range(cols):
            if matrix[row][col] != fixer:
                return row

def find_topmost(matrix, fixer):

    rows, cols = getdim(matrix)

    for row in range(rows):
        for col in range(cols):
            if matrix[row][col] != fixer:
                return row

