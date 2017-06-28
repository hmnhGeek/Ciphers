import argparse as ap
import vigenerecipher as vgc

parser = ap.ArgumentParser()
parser.add_argument('-c', action = 'store_true')
parser.add_argument('-d', action = 'store_true')
parser.add_argument('-m', type = str, action = 'store', dest = 'm')
parser.add_argument('-k', type = str, action = 'store', dest = 'k')

args = parser.parse_args()

if args.c and not args.d:
    print vgc.cipher(args.m, args.k)
else:
    print vgc.decipher(args.m, args.k)
