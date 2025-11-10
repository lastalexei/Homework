matrix = [[11, 2, 35],
          [4, 35, 6],
          [17, 6, 9]]
k = 1
new_matrix = []


def multiply_columns():
    for i in range(len(matrix)):
        new_rows = []
        for j in range(len(matrix[i])):
            new_rows.append(matrix[i][j] * matrix[i][k])
        new_matrix.append(new_rows)
    return  new_matrix


print(multiply_columns())