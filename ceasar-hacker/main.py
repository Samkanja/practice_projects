import string

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def ceaser_hacker(key,msg):
    translated = ''

    for char in msg:
        if char in SYMBOLS:
            num = SYMBOLS.find(char)
            num = num - key

            if num < 0:
                num  = num + len(SYMBOLS)
            translated  = translated + SYMBOLS[num]
        else:
            translated =  translated + char

    return translated


msg = input('messege: ')
print(ceaser_hacker(3,msg))
    

    