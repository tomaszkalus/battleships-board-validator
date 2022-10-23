from msilib.schema import Error
import pprint
import re

bo = '''| | | | | | | | | | |
| | | | | |#| | | | |
| |#|#|#| |#| | | | |
| | | | | |#| | | | |
| | | | | | |2| | | |
| | | | | | | |#| |X|
| | | | | | | | | |X|
| |#| | | |#| | | | |
| |#| | | | | | | | |
| | | | | | | | | |X|'''

template = '''\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|
\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|
\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|
\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|
\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|
\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|
\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|
\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|
\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|
\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|[ \S]\|'''

def validate(inp):
    pattern = re.compile(template)
    return(bool(pattern.fullmatch(inp)))
    

def parseInput(inp):
    if not validate(inp):
        raise Exception("Bad board!")
    out = []
    for i in inp.split('\n'):
        row = []
        for j in i[1:-1].split('|'):
            row.append(j != ' ')
        out.append(row)
    return out
           

def check_horizontal(bo, row, col):
    if not bo[row][col]:
        raise ValueError('The field on the board must be occupied')
    for i in range(1, 5):
        if not bo[row][col + i]:
            return i
    return False

def check_vertical(bo, row, col):
    if not bo[row][col]:
        raise ValueError('The field on the board must be occupied')
    for i in range(1, 5):
        if not bo[row + i][col]:
            return i
    return False


board_parsed = parseInput(bo)
pprint.pprint(board_parsed[7][5])
print(check_vertical(board_parsed, 1, 5))
    

#jeśli natrafi na niepusty:
#czy poziomo na prawo jest łódka?
#czy na pionowo w dół jest łodka?
#jeśli tak to dodaj te pola do pola_do_ominiecia [] i dodaj do dictionary statki jeden
#jeśli nie zgadza się ilość statków, zwróć False

#teraz idź po wszystkich polach ze statków i sprawdź czy jest odstęp, jak nie to wyjeb False



