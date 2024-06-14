from valid import valid

SUDOKU_ROW = 9
SUDOKU_COLUMN = 9

class InvalidSudokuRow(Exception):
    def __init_subclass__(cls) -> None:
        return super().__init_subclass__()

    def __str__(self):
        return f'The row didn\'t have 9 numbers'

def buildSudoku():
    sudoku = []
    print('enter rows of the sudoku(0 to indicate empty space)')

    while len(sudoku) != SUDOKU_ROW:
        try:
            _row = input().split(' ')
            if len(_row) != SUDOKU_COLUMN:
                raise InvalidSudokuRow
            sudoku.append(_row)
        except InvalidSudokuRow as err:
            print(err)
    return sudoku

def solveSudoku():
    pass

sudoku = [
    ['5', '3', '0', '0', '7', '0', '0', '0', '0'],
    ['6', '0', '0', '1', '9', '5', '0', '0', '0'],
    ['0', '9', '8', '0', '0', '0', '0', '6', '0'],
    ['8', '0', '0', '0', '6', '0', '0', '0', '3'],
    ['4', '0', '0', '8', '0', '3', '0', '0', '1'],
    ['7', '0', '0', '0', '2', '0', '0', '0', '6'],
    ['0', '6', '0', '0', '0', '0', '2', '8', '0'],
    ['0', '0', '0', '4', '1', '9', '0', '0', '5'],
    ['0', '0', '0', '0', '8', '0', '0', '7', '9']
]
