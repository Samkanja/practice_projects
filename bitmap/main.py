from typing import TextIO, List


def problem_solved(messege):
    input_t = read_text()
    for line in input_t:
        for i , bit in enumerate(line):
            if bit == ' ':
                print(' ',end='')
            else:
                print(messege[i % len(messege)],end='')
        print() 




def read_text() -> List[str]:
    line = f.read().splitlines()
    return line

with open('bitmap/worldmap.txt') as f:
    print(problem_solved(messege=input('>: ')))
