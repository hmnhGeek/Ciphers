

def shift(number):

    copy = [chr(i) for i in range(ord('A'), ord('Z')+1)]

    while number != 0:
        copy.append(copy.pop(0))
        number -= 1

    return copy


def Vsquare():
    VS = []
    
    for i in range(26):
        VS.append(shift(i))

    return VS
