import argparse
import myszkowski as cp

parser = argparse.ArgumentParser()

parser.add_argument('-c', action = 'store_true', help = "Use it to cipher the text.")
parser.add_argument('-d', action = 'store_true', help = "Use it to decipher the text.")
parser.add_argument('-m', action = 'store_true', help = "Use it to type a message.")
parser.add_argument('-f', action = 'store_true', help = "Use it to read from a file.")
parser.add_argument('-s', action = 'store_true', help = "Use it to save to a file.")
parser.add_argument('Keyword', type = str, help = "Provide keyword.")
parser.add_argument('string', type = str, help = "Provide a string value, either a message of file address.")
parser.add_argument('save_loc', type = str, help = "Provide a saving location.", nargs = '?')
parser.add_argument('fixer', type = str, help = "Provide a fixer.", nargs = '?')

args = parser.parse_args()

def save(data, loc):
    f = open(loc, 'w')
    f.write(data)
    f.close()

def readdata(loc):
    f = open(loc)
    data = f.read()
    f.close()

    return data

if args.m:
    if args.c:
        if args.fixer and args.s:
            ciphertext = cp.cipher(args.string, args.Keyword, args.fixer)
            save(ciphertext, args.save_loc)
        elif args.s:
            ciphertext = cp.cipher(args.string, args.Keyword)
            save(ciphertext, args.save_loc)
        elif not args.s and args.save_loc:
            ciphertext = cp.cipher(args.string, args.Keyword, args.save_loc)
        else:
            ciphertext = cp.cipher(args.string, args.Keyword)

        print ciphertext
        
    elif args.d:
        if args.fixer and args.s:
            deciphertext = cp.decipher(args.string, args.Keyword, args.fixer)
            save(deciphertext, args.save_loc)
        elif args.s:
            deciphertext = cp.decipher(args.string, args.Keyword)
            save(deciphertext, args.save_loc)
        elif not args.s and args.save_loc:
            deciphertext = cp.decipher(args.string, args.Keyword, args.save_loc)
        else:
            deciphertext = cp.decipher(args.string, args.Keyword)

        print deciphertext






elif args.f:

    content = readdata(args.string)
    
    if args.c:
        if args.fixer and args.s:
            ciphertext = cp.cipher(content, args.Keyword, args.fixer)
            save(ciphertext, args.save_loc)
        elif args.s:
            ciphertext = cp.cipher(content, args.Keyword)
            save(ciphertext, args.save_loc)
        elif args.fixer:
            ciphertext = cp.cipher(content, args.Keyword, args.save_loc)
        else:
            ciphertext = cp.cipher(content, args.Keyword)

        print ciphertext
        
    elif args.d:
        if args.fixer and args.s:
            deciphertext = cp.decipher(content, args.Keyword, args.fixer)
            save(deciphertext, args.save_loc)
        elif args.s:
            deciphertext = cp.decipher(content, args.Keyword)
            save(deciphertext, args.save_loc)
        elif args.fixer:
            deciphertext = cp.decipher(content, args.Keyword, args.save_loc)
        else:
            deciphertext = cp.decipher(content, args.Keyword)

        print deciphertext
