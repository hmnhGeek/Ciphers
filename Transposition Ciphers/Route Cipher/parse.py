import argparse
import routecipher as rc

parser = argparse.ArgumentParser()
parser.add_argument('-c', action= 'store_true', help = 'Use it to cipher the plaintext.')
parser.add_argument('-d', action= 'store_true', help = 'Use it to decipher the ciphertext.')
parser.add_argument('-f', action= 'store_true', help = 'Use it to open a file.')
parser.add_argument('-s', action= 'store_true', help = 'Use it to save to a file.')
parser.add_argument('key', type = int, help = 'Type your key.')
parser.add_argument('direction', type = str, help = 'Type route direction. Eg: clockwise, anti-clockwise.')
parser.add_argument('message', type = str, help = 'Type your message.')
parser.add_argument('save_loc', type = str, help = 'Type saving location.', nargs = '?')
parser.add_argument('fixer', type = str, help = 'Type a fixer.', nargs = '?')

args = parser.parse_args()

def action(msg, fix = None):
    if args.c:
        if fix <> None:
            return rc.cipher(msg, args.key, args.direction, fix)
        else:
            return rc.cipher(msg, args.key, args.direction)

    elif args.d:
        if fix <> None:
            return rc.decrypt(msg, args.key, args.direction, fix)
        else:
            return rc.decrypt(msg, args.key, args.direction)

if args.f:
    fil = file(args.message, 'r')
    content = fil.read()
    fil.close()

    if args.s:
        if args.fixer:
            gotthis = action(content, args.fixer)
        else:
            gotthis = action(content, None)
        
        fil = file(args.save_loc, 'w')
        fil.write(gotthis)
        fil.close()
    else:
        if args.save_loc:
            gotthis = action(content, args.save_loc)
        else:
            gotthis = action(content, None)

    print gotthis

else:

    if args.s:
        if args.fixer:
            gotthis = action(args.message, args.fixer)
        else:
            gotthis = action(args.message, None)
        
        fil = file(args.save_loc, 'w')
        fil.write(gotthis)
        fil.close()
    else:
        if args.save_loc:
            gotthis = action(args.message, args.save_loc)
        else:
            gotthis = action(args.message, None)

    print gotthis
