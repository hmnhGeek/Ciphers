
def check_duplicacy(keyword):
    
    l = [i for i in keyword.upper()]

    
    for i in l:
        if i in l[l.index(i)+1::]:
            return False

    return True

def fetch_index(keyword):
    if check_duplicacy(keyword):
        keyword = keyword.upper()
        
        l = ['A', 'B', 'C', 'D',
             'E', 'F', 'G', 'H',
             'I', 'J', 'K', 'L',
             'M', 'N', 'O', 'P',
             'Q', 'R', 'S', 'T',
             'U', 'V', 'W', 'X',
             'Y', 'Z']
        

        indexes = list()

        for char in keyword:
            indexes.append(l.index(char)+1)

        copy = []
        for char in keyword:
            copy.append(l.index(char)+1)

        proxy = [0 for i in range(len(keyword))]

        counter = 1
        
        while copy <> []:
            minima = min(copy)
            for i in range(len(indexes)):
                if indexes[i] == minima:
                    proxy[i] = counter

            copy.remove(minima)
            counter += 1

        return proxy

    else:
        return None

       
