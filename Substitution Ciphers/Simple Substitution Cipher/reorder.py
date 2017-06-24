from alphabets import *

def reorder(keyword):
    # remove duplicates from the key.
    keyword = generate_key(keyword)

    # get alphabets in a list.
    order = get_list()

    # initialise cipher array with characters from keyword.
    cipher_array = [i for i in keyword]

    # now add all other keys in order, skipping only those which we just inserted.
    for char in order:
        if char not in cipher_array:
            cipher_array.append(char)

    return order, cipher_array
