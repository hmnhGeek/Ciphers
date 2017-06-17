
def duplicacy(datalist):

    dups = []

    for i in range(len(datalist)):
        if datalist[i] not in dups and datalist[i] in datalist[i+1::]:
            
            dups.append(datalist[i])

    return dups

def get_index_of_a_duplicate(rank, data):

    indexes = []
    
    if rank in duplicacy(data):

        for i in range(len(data)):
            if data[i] == rank:
                indexes.append(i)

    return indexes

def get_ranks(ords):
    distincts = []

    for ORD in ords:
        if ORD not in distincts:
            distincts.append(ORD)

    distincts.sort()

    starter = 1
    rankings = {}

    for i in distincts:
        rankings.update({i:starter})
        starter += 1

    return rankings

def fetch_ranks(keyword):

    keyword = keyword.upper()

    chars = [char for char in keyword]

    ordinates = []
    copy = []
    for char in chars:
        ordinates.append(ord(char))
        copy.append(ord(char))

    ranks = get_ranks(copy)
    
    for i in range(len(ordinates)):
        ordinates[i] = ranks[ordinates[i]]

    return ordinates

    
