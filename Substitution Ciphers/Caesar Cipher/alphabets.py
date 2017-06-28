

def get_alphabets():

    return ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z']

def shift(key):

    reference = get_alphabets()

    # pop from the reference list, until the loop runs key times.
    for i in range(key):
        reference.insert(0, reference.pop())

    return reference


def __map__(key):

    original, reference = get_alphabets(), shift(key)

    orig_to_ref, ref_to_orig = {}, {}

    for i in range(len(original)):
        orig_to_ref.update({original[i]:reference[i]})

    for i in range(len(reference)):
        ref_to_orig.update({reference[i]:original[i]})

    return orig_to_ref, ref_to_orig
