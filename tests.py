import os
from main import battleshipValidator

directory = 'tests'
filenames = []


# iterate over files in
# that directory
for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        filenames.append(f)


# print(filenames)
for f in filenames:
    with open(f, 'r', encoding='utf-8') as file:
        board = file.read()
    print(f)
    validator = battleshipValidator(board)
    print(validator.validate())