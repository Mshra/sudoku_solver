from main import SUDOKU_COLUMN, SUDOKU_ROW

def check_row(row: list[str]) -> bool:
    if len(row) != SUDOKU_ROW: return False

    num_set = set()
    for number in row:
        if number in num_set:
            return False
        num_set.add(number)
    return True

def valid(sudoku: list[list]) -> bool:
    if len(sudoku) != SUDOKU_COLUMN:
        return False

    for row in sudoku:
        from valid import check_row
        if check_row(row) == False:
            return False

    return True

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
