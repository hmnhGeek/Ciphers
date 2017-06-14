import argparse
from railfencecipher import *

parser = argparse.ArgumentParser()
parser.add_argument("-c", action = "store_true", help = "Use it for ciphering.")
parser.add_argument("-d", action = "store_true", help = "Use it for deciphering.")
parser.add_argument("-f", action = "store_true", help = "Use it to read from a file.")
parser.add_argument("-s", action = "store_true", help = "Use it to save to a file.")
parser.add_argument("key", type = int, help = "Use it to pass a key.")
parser.add_argument("sentence", type = str, help = "Pass a sentence or a file location if -f is used.")
parser.add_argument("save_loc", type = str, nargs = '?', help = "Use it to specify saving location when -s is used.")

args = parser.parse_args()

sentence = args.sentence

key = args.key

if args.f:
    f = open(sentence, 'r')
    sen = f.read()
    f.close()

    if args.c:
        cip = cipher(sen, key)

    if args.d:
        decip = decipher(sen, key)


elif args.c:
    cip = cipher(sentence, key)

elif args.d:
    decip = decipher(sentence, key)


try:
    print cip

    if args.s:
        sv = args.save_loc
        f = open(sv, 'w')
        f.write(cip)
        f.close()
except:
    print decip
    if args.s:
        sv = args.save_loc
        f = open(sv, 'w')
        f.write(decip)
        f.close()
