def buildSudoku():
    SUDOKU_ROW = 9
    SUDOKU_COLUMN = 9

    class InvalidSudokuRow(Exception):
        def __init_subclass__(cls) -> None:
            return super().__init_subclass__()

        def __str__(self):
            return f'The row didn\'t have 9 numbers'

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

print(buildSudoku())

# TODO: build an interface for taking in sudoku first
