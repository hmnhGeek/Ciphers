import ranks

def decrypter(ciphertext, keyword, fixer = '~'):

    keyword = keyword.upper()
    
    # first determine the number of rows and columns of the matrix.
    cols = len(keyword)
    rows = int(len(ciphertext)*cols**(-1))

    # now initialise the matrix.
    matrix = [[fixer for i in range(cols)] for j in range(rows)]

    # get the ranks of the keyword.
    rank = ranks.fetch_ranks(keyword)
    rankcopy = ranks.fetch_ranks(keyword)

    # get all duplicate ranks.
    duplc = ranks.duplicacy(rank)

    while rank <> []:

        i = min(rank)
        
        if i not in duplc:

            # get its index in rank list.
            index = rankcopy.index(i)

            for row in matrix:
                try:
                    row[index] = ciphertext[0]
                    ciphertext = ciphertext[1::]
                except:
                    pass

            rank.remove(i)

        else:
            # get all indexes of the duplicates.
            indexes = ranks.get_index_of_a_duplicate(i, rankcopy)

            while i in rank:
                rank.remove(i)

            for row in matrix:
                for index in indexes:
                    try:
                        row[index] = ciphertext[0]
                        ciphertext = ciphertext[1::]
                    except:
                        pass

    # initialise a deciphertext.
    deciphertext = ''

    for row in matrix:
        for char in row:
            deciphertext += char

    return deciphertext.rstrip(fixer)
            
