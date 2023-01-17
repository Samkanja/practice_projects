import string
def main():
    print('Do you want to (e)ncrypt or (d)ecrypt')
    style = input('method: ')
    key = int(input('key: '))
    messege = input('messege: ')
    match style:
        case 'e':
            res = encryption(messege,key)
            return res
        case 'd':
            res = decryption(messege,key)
            return res
        case _:
            return 'Invalid input'
    # if style == 'e':
    #     res = encryption(messege,key)
    #     return res
    # else:
    #     res = decryption(messege,key)
    #     return res



def encryption(msg:str ,key:int) -> str:
    alp = string.ascii_letters
    d = {}
    for i , ele in enumerate(alp):
        d[ele] = alp[(i + key)%52]
    res = ''
    for char in msg:
        if char.isalpha():
            if char.isupper():
                res += d[char].upper()
            else:
                res += d[char].upper()
        else:
            res += char
    return res

def decryption(msg:str , key :int) -> str:
    alp = string.ascii_letters
    d = {}
    for i , ele in enumerate(alp):
        d[ele] = alp[(i - key) % 52]
    res = ''
    for char in msg:
        if char.isalpha():
            if char.isupper():
                res +=  d[char]
            else:
                res += d[char]

        else:
            res += char
    return res
print(decryption('m',4))

if __name__ == '__main__':
    print(main())



