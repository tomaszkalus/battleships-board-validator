import pprint
import re
import sys
import fileinput

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


class battleshipValidator:
    SHIPS = {4: 1, 3: 2, 2: 3, 1: 4}

    def __init__(self, board) -> None:
        self.isBoardValid(board)
        self.board = self.parseBoard(board.strip())
        self.visited = set()
        self.ships = []
        self.number_of_ships = {1: 0, 2: 0, 3: 0, 4: 0}

    def isBoardValid(self, bo) -> None:
        if not isinstance(bo, str):
            raise TypeError("The board should be the type of string")
        pattern = re.compile(REGEX)
        if not bool(pattern.fullmatch(bo.strip())):
            raise ValueError("The board is not formatted correctly")

    def validate(self):
        for i, row in enumerate(self.board):
            for j, col in enumerate(row):
                if col and (i, j) not in self.visited:
                    ship = self.identify(i, j)
                    if ship[0] > 4 or ship[1] > 4:
                        return False

                    if ship[0] > 1 and ship[1] > 1:
                        return False


                    self.ships.append((i, j, *ship))
                    self.number_of_ships[max(*ship)] += 1

        for ship in self.ships:
            if not self.check_spaces(*ship):
                return False

        if battleshipValidator.SHIPS != self.number_of_ships:
            return False
        return True

    def parseBoard(self, bo):
        out = []
        for i in bo.split('\n'):
            row = []
            for j in i[1:-1].split('|'):
                row.append(j != ' ')
            out.append(row)
        return out

    def check_spaces(self, row, col, vy, vx):
        # horizontal
        length = max(vx, vy)
        if vx > vy:
            for y in range(length + 2):
                if (row - 1, col - 1 + y) in self.visited or (row + 1, col - 1 + y) in self.visited:
                    return False
            if (row, col - 1) in self.visited or (row, col + length) in self.visited:
                return False
            return True

        # vertical
        for x in range(length + 2):
            if (row - 1 + x, col - 1) in self.visited or (row - 1 + x, col + 1) in self.visited:
                return False
        if (row - 1, col) in self.visited or (row + length, col) in self.visited:
            return False
        return True

    def identify(self, row, col):
        v = [0, 0]

        #row
        while True:
            try:
                if not self.board[row + v[0]][col]:
                    break
            except IndexError:
                break

            self.visited.add((row + v[0], col))
            v[0] += 1


        #col
        while True:
            try:
                if not self.board[row][col + v[1]]:
                    break
            except IndexError:
                break
            self.visited.add((row, col + v[1]))
            v[1] += 1


        return v


if __name__ == "__main__":
    
    board = ""
    for line in fileinput.input():
        board += line.strip()
        board += '\n'
    validator = battleshipValidator(board)
    print(validator.validate())