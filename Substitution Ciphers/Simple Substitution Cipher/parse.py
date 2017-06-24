#/usr/bin/python

import argparse
import substitution_cipher as sc

parser = argparse.ArgumentParser()

parser.add_argument('-c', action = "store_true", help = "To cipher the plaintext.")
parser.add_argument('-d', action = "store_true", help = "To decipher the plaintext.")
parser.add_argument('-m', action = "store", dest = 'm', type = str, help = "To type plaintext.")
parser.add_argument('-f', action = "store", dest = 'f', type = str, help = "To pass a plaintext file.")
parser.add_argument('-s', action = "store", dest = 's', type = str, help = "To pass a saving location.")
parser.add_argument('-k', action = "store", dest = 'k', type = str, help = "To pass a keyword.")
parser.add_argument('-g', action = "store", dest = 'g', type = int, default = 0, help = "To pass a groupify action. Either 0 or 1.")

args = parser.parse_args()
args.g = bool(args.g)

if args.c and not args.d:
    if args.f:
        f = open(args.f, 'r')
        content = f.read()
        f.close()

        ciphertext = sc.encrypt(content, args.k, args.g)

        if args.s:
            f = open(args.s, 'w')
            f.write(ciphertext)
            f.close()
        else:
            print ciphertext
    else:
        ciphertext = sc.encrypt(args.m,args.k,args.g)
        if args.s:
            f = open(args.s, 'w')
            f.write(ciphertext)
            f.close()
        else:
            print ciphertext
            
elif args.d and not args.c:
    if args.f:
        f = open(args.f, 'r')
        content = f.read()
        f.close()

        deciphertext = sc.decrypt(content, args.k)
        
        if args.s:
            f = open(args.s, 'w')
            f.write(deciphertext)
            f.close()
        else:
            print deciphertext
    else:
        deciphertext = sc.decrypt(args.m,args.k,args.g)
        if args.s:
            f = open(args.s, 'w')
            f.write(deciphertext)
            f.close()
        else:
            print deciphertext
else:
    print "Invalid choice!!"

