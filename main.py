import random

# Constants
BOX_1 = [(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
BOX_2 = [(0, 3), (0, 4), (0, 5), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5)]
BOX_3 = [(0, 6), (0, 7), (0, 8), (1, 6), (1, 7), (1, 8), (2, 6), (2, 7), (2, 8)]
BOX_4 = [(3, 0), (3, 1), (3, 2), (4, 0), (4, 1), (4, 2), (5, 0), (5, 1), (5, 2)]
BOX_5 = [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (4, 5), (5, 3), (5, 4), (5, 5)]
BOX_6 = [(3, 6), (3, 7), (3, 8), (4, 6), (4, 7), (4, 8), (5, 6), (5, 7), (5, 8)]
BOX_7 = [(6, 0), (6, 1), (6, 2), (7, 0), (7, 1), (7, 2), (8, 0), (8, 1), (8, 2)]
BOX_8 = [(6, 3), (6, 4), (6, 5), (7, 3), (7, 4), (7, 5), (8, 3), (8, 4), (8, 5)]
BOX_9 = [(6, 6), (6, 7), (6, 8), (7, 6), (7, 7), (7, 8), (8, 6), (8, 7), (8, 8)]
BOXES = [BOX_1, BOX_2, BOX_3, BOX_4, BOX_5, BOX_6, BOX_7, BOX_8, BOX_9]


def main():
    print("Welcome to the Sudoku-Suite")

    example_sudoku = [
        [1, 2, 3, 4, 5, 6, 7, 8, 1],
        [2, 3, 4, 5, 6, 7, 8, 9, 1],
        [3, 4, 5, 6, 7, 8, 9, 1, 2],
        [4, 5, 6, 7, 8, 9, 1, 2, 3],
        [5, 6, 7, 8, 9, 1, 2, 3, 4],
        [6, 7, 8, 9, 1, 2, 3, 4, 5],
        [7, 8, 9, 1, 2, 3, 4, 5, 6],
        [8, 9, 1, 2, 3, 4, 5, 6, 7],
        [9, 1, 2, 3, 4, 5, 6, 7, 8],
    ]

    sudoku_string = convert_to_sudoku_string(example_sudoku)

    print(sudoku_string)

    check_sudoku(example_sudoku)


def check_sudoku(sudoku_array):
    # Check rows
    row_errors = []
    for index, row in enumerate(sudoku_array):
        already_in_row = []
        for element in row:
            if element not in already_in_row:
                already_in_row.append(element)
            else:
                row_errors.append(f"Error in row {index + 1}")
                break

    # Check columns
    column_errors = []
    for index, row in enumerate(transpose_sudoku(sudoku_array)):
        already_in_row = []
        for element in row:
            if element not in already_in_row:
                already_in_row.append(element)
            else:
                column_errors.append(f"Error in column {index + 1}")
                break

    # Check boxes
    box_errors = []
    for index, box in enumerate(BOXES):
        already_in_box = []
        for coordinates in box:
            i = coordinates[0]
            j = coordinates[1]
            if sudoku_array[i][j] not in already_in_box:
                already_in_box.append(sudoku_array[i][j])
            else:
                box_errors.append(f"Error in box {index + 1}")
                break

    for error in row_errors:
        print(error)

    for error in column_errors:
        print(error)

    for error in box_errors:
        print(error)


def transpose_sudoku(sudoku_array):
    transposed_sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0],
                         [0, 0, 0, 0, 0, 0, 0, 0, 0]]
    i = 0
    while i < 9:
        j = 0
        while j < 9:
            transposed_sudoku[i][j] = sudoku_array[j][i]
            j += 1
        i += 1

    return transposed_sudoku


def convert_to_sudoku_string(sudoku_array):
    sa = sudoku_array
    string = f"+ - - - + - - - + - - - +\n" \
        f"| {sa[0][0]} {sa[0][1]} {sa[0][2]} | {sa[0][3]} {sa[0][4]} {sa[0][5]} | {sa[0][6]} {sa[0][7]} {sa[0][8]} |\n" \
        f"| {sa[1][0]} {sa[1][1]} {sa[1][2]} | {sa[1][3]} {sa[1][4]} {sa[1][5]} | {sa[1][6]} {sa[1][7]} {sa[1][8]} |\n" \
        f"| {sa[2][0]} {sa[2][1]} {sa[2][2]} | {sa[2][3]} {sa[2][4]} {sa[2][5]} | {sa[2][6]} {sa[2][7]} {sa[2][8]} |\n" \
        f"+ - - - + - - - + - - - +\n" \
        f"| {sa[3][0]} {sa[3][1]} {sa[3][2]} | {sa[3][3]} {sa[3][4]} {sa[3][5]} | {sa[3][6]} {sa[3][7]} {sa[3][8]} |\n" \
        f"| {sa[4][0]} {sa[4][1]} {sa[4][2]} | {sa[4][3]} {sa[4][4]} {sa[4][5]} | {sa[4][6]} {sa[4][7]} {sa[4][8]} |\n" \
        f"| {sa[5][0]} {sa[5][1]} {sa[5][2]} | {sa[5][3]} {sa[5][4]} {sa[5][5]} | {sa[5][6]} {sa[5][7]} {sa[5][8]} |\n" \
        f"+ - - - + - - - + - - - +\n" \
        f"| {sa[6][0]} {sa[6][1]} {sa[6][2]} | {sa[6][3]} {sa[6][4]} {sa[6][5]} | {sa[6][6]} {sa[6][7]} {sa[6][8]} |\n" \
        f"| {sa[7][0]} {sa[7][1]} {sa[7][2]} | {sa[7][3]} {sa[7][4]} {sa[7][5]} | {sa[7][6]} {sa[7][7]} {sa[7][8]} |\n" \
        f"| {sa[8][0]} {sa[8][1]} {sa[8][2]} | {sa[8][3]} {sa[8][4]} {sa[8][5]} | {sa[8][6]} {sa[8][7]} {sa[8][8]} |\n" \
        f"+ - - - + - - - + - - - +\n"

    return string

if __name__ == "__main__":
    main()
