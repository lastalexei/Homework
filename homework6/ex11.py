matrix = [[11, 2, 35],
          [4, 35, 6],
          [17, 6, 9]]
k = 1
new_matrix = []


def add_rows():
    for i in range(len(matrix)):
        new_rows = []
        for j in range(len(matrix[0])):
            new_rows.append(matrix[i][j] + matrix[k][j])
        new_matrix.append(new_rows)
    for row in new_matrix:
        print(row)


add_rows()