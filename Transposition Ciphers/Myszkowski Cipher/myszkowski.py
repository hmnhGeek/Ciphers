import ranks
from myszkowski_decipher import decrypter

def readcolumn(rank, matrix, rankings):
    index = rankings.index(rank)

    text = ''
    for row in matrix:
        text += row[index]

    return text

def cipher(message, keyword, fixer = '~'):
    keyword = keyword.upper()
    if len(keyword) > 1 and len(keyword) < len(message):

        # first get ranks of the keyword.
        rank = ranks.fetch_ranks(keyword)
        rankcopy = ranks.fetch_ranks(keyword)
        
        # now initialise the matrix as we do in columnar cipher.
        # here columns = len(rank)
        cols = len(rank)

        # initialise the matrix.
        matrix = []

        # now the rows are determined after inserting the characters one by one and row by row.
        # so create a copy of the original message.
        copy = message

        while copy <> '':

            row = []

            while len(row) <> cols:
                try:
                    row.append(copy[0])
                    copy = copy[1::]
                except IndexError:
                    row.append(fixer)

            else:
                matrix.append(row)

        # now get the duplicate ranks in rank. Eg, [4,3,3,1,2] has duplicate rank 3.
        duplc = ranks.duplicacy(rank)

        # initialise ciphertext.
        ciphertext = ''
        
        # now find minimum rank
        # if the encountered element is unique in rank, read its column.
        # else read from left to right.
        while rank <> []:
            i = min(rank)
            
            if i not in duplc:
                add = readcolumn(i, matrix, rankcopy)
                ciphertext += add
                rank.remove(i)
            else:
                indexes = ranks.get_index_of_a_duplicate(i, rankcopy)

                while (i in rank):
                    rank.remove(i)
                
                for row in matrix:
                    for a_index in indexes:
                        ciphertext += row[a_index]

                
        return ciphertext
    else:
        return "The length of the keyword should be more than 1 and less than the length of message, i.e., "+str(len(message))+"."


def decipher(ciphertext, keyword, fixer = '~'):

    if len(keyword) > 1 and len(keyword) < len(ciphertext):

        return decrypter(ciphertext, keyword, fixer)

    else:
        return "The length of the keyword should be more than 1 and less than the length of message, i.e., "+str(len(ciphertext))+"."
        
