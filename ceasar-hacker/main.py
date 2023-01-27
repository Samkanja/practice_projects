import string

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def ceaser_hacker(key,msg):
    
    output =set()
    for i in range(len(SYMBOLS)):
        translated = ''
        for char in msg:
            if char in SYMBOLS:
                num = SYMBOLS.find(char)
                num = num - i

                if num < 0:
                    num  = num + len(SYMBOLS)
                translated  = translated + SYMBOLS[num]
            else:
                translated =  translated + char

        output.add(translated)
    return output


msg = input('messege: ')
print(ceaser_hacker(3,msg))
    

    