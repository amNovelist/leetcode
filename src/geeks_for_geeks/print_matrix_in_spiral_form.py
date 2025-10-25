# Input: mat[][] = [[1,   2,   3,   4],
#                   [5,    6,   7,   8],
#                   [9,   10,  11,  12],
#                   [13,  14,  15,  16]]
# Output: [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]

def print_matrix_in_spiral_form(arr):
    if not arr:
        print(arr)
    row_max = len(arr)
    col_max = len(arr[0])

    if row_max == 1 and col_max == 1:
        print(arr)

    col_min = 0
    row_min = 0
    dir = "L"
    i = 0
    j = 0
    print(arr[i][j])
    total_prints = row_max * col_max
    prints = 1
    while prints < total_prints:
        while j+1 < col_max and prints < total_prints:
            j = j+1
            if dir != "L":
                col_min = col_min + 1
                dir = "L"
            print(arr[i][j])
            prints += 1
            print(f"Prints: {prints}, i={i}, j={j}, row_max = {row_max}, row_min={row_min}, col_max={col_max}, col_min={col_min}")


        while i+1 < row_max and prints < total_prints:
            i = i+1
            if dir != "D":
                row_min = row_min+1
                dir = "D"
            print(arr[i][j])
            prints += 1
            print(f"Prints: {prints}, i={i}, j={j}, row_max = {row_max}, row_min={row_min}, col_max={col_max}, col_min={col_min}")

        while j-1 >= col_min and prints < total_prints:
            j = j-1
            if dir != "R":
                col_max = col_max-1
                dir = "R"
            print(arr[i][j])
            prints += 1
            print(f"Prints: {prints}, i={i}, j={j}, row_max = {row_max}, row_min={row_min}, col_max={col_max}, col_min={col_min}")

        while i-1 >= row_min and prints < total_prints:
            i = i - 1
            if dir != "U":
                row_max = row_max-1
                dir = "U"
            print(arr[i][j])
            prints += 1
            print(f"Prints: {prints}, i={i}, j={j}, row_max = {row_max}, row_min={row_min}, col_max={col_max}, col_min={col_min}")

mat =       [[1,   2,   3,   4],
             [5,    6,   7,   8],
             [9,   10,  11,  12],
             [13,  14,  15,  16]]
# print_matrix_in_spiral_form(mat)

mat =       [[1,    3,   4],
             [5,    6,    8],
             [9,     11,  12],
             [13,    15,  16]]

print_matrix_in_spiral_form(mat)