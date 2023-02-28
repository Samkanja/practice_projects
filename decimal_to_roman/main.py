def decimal_to_roman(decimal_num:int) -> str:
    roman_num = ''
    decimal_to_roman = {
        1000:'M',900:'CM',500:'D',400:'CD',
        100:'C',90:'XC',50:'L',40:'XL',10:'X',
        9:'IX',5:'V',4:'IV',1:'I'
    }
    for dec, rom in decimal_to_roman.items():
        while decimal_num >= dec:
            roman_num += rom
            decimal_num -= dec
    return roman_num

num = int(input('num: '))
print(decimal_to_roman(num))