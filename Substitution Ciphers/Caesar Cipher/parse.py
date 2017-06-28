import argparse
import caesarcipher as cc

parser = argparse.ArgumentParser()

parser.add_argument('-c', action = "store_true", help = "To cipher the plaintext.")
parser.add_argument('-d', action = "store_true", help = "To decipher the plaintext.")
parser.add_argument('-m', action = "store", dest = 'm', type = str, help = "To send message.")
parser.add_argument('-f', action = "store", dest = 'f', type = str, help = "To send plaintext file.")
parser.add_argument('-s', action = "store", dest = 's', type = str, help = "To send saving location.")
parser.add_argument('-k', action = 'store', dest = 'k', type = int, help = "To set the key.")

args = parser.parse_args()

if args.c and not args.d:
    if not args.f and args.s:
        ciphertext = cc.cipher(args.m, args.k)

        fil = open(args.s, 'w')
        fil.write(ciphertext)
        fil.close()

        print "Saved!!"

    elif args.f and args.s:

        fil = open(args.f, 'r')
        content = fil.read()
        fil.close()

        ciphertext = cc.cipher(content, args.k)

        fil = open(args.s, 'w')
        fil.write(ciphertext)
        fil.close()

        print "Saved!!"

    elif args.f and not args.s:

        fil = open(args.f, 'r')
        content = fil.read()
        fil.close()

        ciphertext = cc.cipher(content, args.k)

        print ciphertext

    elif not args.f and not args.s:
        
        print cc.cipher(args.m, args.k)




if args.d and not args.c:
    if not args.f and args.s:
        deciphertext = cc.decipher(args.m, args.k)

        fil = open(args.s, 'w')
        fil.write(deciphertext)
        fil.close()

        print "Saved!!"

    elif args.f and args.s:

        fil = open(args.f, 'r')
        content = fil.read()
        fil.close()

        deciphertext = cc.decipher(content, args.k)

        fil = open(args.s, 'w')
        fil.write(deciphertext)
        fil.close()

        print "Saved!!"

    elif args.f and not args.s:

        fil = open(args.f, 'r')
        content = fil.read()
        fil.close()

        deciphertext = cc.decipher(content, args.k)

        print deciphertext

    elif not args.f and not args.s:
        
        print cc.decipher(args.m, args.k)

