from msilib.schema import Error
import pprint
import re

REGEX = '''\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|
\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|
\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|
\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|
\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|
\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|
\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|
\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|
\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|
\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|[ X]\|'''


bo = '''| | | | | | | | | | |
| | | | | |X| | | | |
| |X|X|X| |X| | | | |
| | | | | |X| | | | |
| | | | | | |X| | | |
| | | | | | | |X| |X|
| | | | | | | | | |X|
| |X| | | |X| | | | |
| |X| | | | | | | | |
| | | | | | | | | |X|'''


class battleshipValidator:
    def __init__(self, board) -> None:
        self.isBoardValid(board)
        self.board = self.parseBoard(board)
        self.visited = set()
        self.ships = {1: 0, 2: 0, 3: 0, 4: 0}

    def isBoardValid(self, bo) -> None:
        if not isinstance(bo, str):
            raise TypeError("The board should be the type of string")
        pattern = re.compile(REGEX)
        if not bool(pattern.fullmatch(bo)):
            raise ValueError("The board is not formatted correctly")

    def validate(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col:
                    print(f"{i}, {j}")
                    print(self.check_horizontal(i, j))
                    print(self.visited)
                    # if self.check_horizontal(i, j) == 1:
                    #     if self.check_vertical(i, j) == 1:
                    #         self.ships[1] += 1
                    #         print(f"{i}, {j}")
        print(self.ships)

    def parseBoard(self, bo):
        out = []
        for i in bo.split('\n'):
            row = []
            for j in i[1:-1].split('|'):
                row.append(j != ' ')
            out.append(row)
        return out

    def check_horizontal(self, row, col):
        for i in range(1, 5):
            try:
                if not self.board[row][col + i]:
                    return i
            except IndexError:
                break
            self.visited.add((row, col + i))

        return False

    def check_vertical(self, row, col):
        for i in range(1, 5):
            try: 
                if not self.board[row + i][col]:
                    return i
            except IndexError:
                continue
        return False

    def check_blank_horizontal(self, row, col, length):
        print(col - 1)
        print(col + length + 1)
        for i in range(col - 1, col + length + 1):
            print(
                f"{row+1}:{i} - {self.board[row+1][i]} , {row-1}:{i} - {self.board[row-1][i]}")
            if self.board[row + 1][i] or self.board[row - 1][i]:
                return False
        return True

    def check_blank_vertical(self, row, col, length):
        print(row - 1)
        print(row + length + 1)
        for i in range(row - 1, row + length + 1):
            print(
                f"{i}:{col+1} - {self.board[i][col+1]} , {i}:{col-1} - {self.board[i][col-1]}")
            if self.board[i][col+1] or self.board[i][col-1]:
                return False
        return True


validator = battleshipValidator(bo)
# validator.validate()
pprint.pprint(validator.board)
# print(validator.check_horizontal(2, 1))
# print(validator.check_blank_horizontal(2, 1, 3))
# print(validator.check_blank_vertical(7, 5, 1))
validator.validate()


# board_parsed = parseInput(bo)
# pprint.pprint(board_parsed[7][5])
# print(check_vertical(board_parsed, 1, 5))


# jeśli natrafi na niepusty:
# czy poziomo na prawo jest łódka?
# czy na pionowo w dół jest łodka?
# jeśli tak to dodaj te pola do pola_do_ominiecia [] i dodaj do dictionary statki jeden
# jeśli nie zgadza się ilość statków, zwróć False

# teraz idź po wszystkich polach ze statków i sprawdź czy jest odstęp, jak nie to wyjeb False
