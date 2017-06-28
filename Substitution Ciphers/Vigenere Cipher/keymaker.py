def make_proper(keyword):
    keyword = keyword.upper()

    l = [chr(i) for i in range(ord('A'), ord('Z')+1)]

    K = ''

    for i in keyword:
        if i in l and i not in K:
            K+= i

    return K
        

def make_key(message, keyword):

    if len(keyword) < len(message):
        keyword = make_proper(keyword)
        proper = ''

        while len(proper) != len(message):
            for i in keyword:
                proper += i

                if len(proper) == len(message):
                    break

        return proper

    elif len(keyword) > len(message):
        keyword = make_proper(keyword)
        
        if len(keyword) != len(message):
            return make_key(message, keyword)
        else:   
            return keyword[0:len(message)]
    else:
        keyword = make_proper(keyword)

        if len(keyword) != len(message):
            return make_key(message, keyword)
        else:
            return keyword
