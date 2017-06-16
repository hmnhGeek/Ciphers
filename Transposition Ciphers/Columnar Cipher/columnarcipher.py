import index_provider

def cipher(message, keyword, fixer = '~'):

    # first make the keyword uppercase.
    keyword = keyword.upper()

    # now declare the number of columns.
    cols = len(keyword)

    # now create an empty list which will store rows (again a list with number of elements = cols) in this list.
    # before this, create a copy of the message and also initialise the empty list.
    proxy = message
    matrix = []

    while proxy <> '':
        
        row = []
        while len(row) <> cols:
            try:
                row.append(proxy[0])
                proxy = proxy[1::]
            except:
                row.append(fixer)
        else:
            matrix.append(row)

    # now use index_provider.fetch_index(keyword) to get rank of each character in the keyword as a list.
    ranks = index_provider.fetch_index(keyword)

    if ranks <> None:

        # initialise the ciphertext.
        ciphertext = ''
        
        # now split out each column in matrix according to ranks.
        for i in range(1, len(ranks)+1):
            col_index = ranks.index(i)

            for j in matrix:
                
                ciphertext += j[col_index]

        return ciphertext

    else:
        return "Use a keyword which has no duplicate character. Example, 'zebras'."


def decipher(ciphertext, keyword, fixer = '~'):

    keyword = keyword.upper()
    
    # now we must initialise a matrix with number of cols = len(keyword) and rows = len(ciphertext)/len(keyword).
    cols = int(len(keyword))
    rows = int(len(ciphertext)*(cols**(-1)))

    matrix = [['' for i in range(cols)] for j in range(rows)]

    # get rank of keyword using index_provider's fetch_index() function.
    ranks = index_provider.fetch_index(keyword)

    if ranks <> None:

        # now start with lowest rank and move to the last rank and fill columns accordingly.
        for i in range(1, len(keyword)+1):
            col_index = ranks.index(i)

            for j in matrix:
                try:
                    j[col_index] = ciphertext[0]
                    ciphertext = ciphertext[1::]
                except:
                    pass

        deciphertext = ''

        for row in matrix:
            for char in row:
                deciphertext += char

        return deciphertext.rstrip(fixer)

    else:
        return "Use a keyword which has no duplicate character. Example, 'zebras'."
