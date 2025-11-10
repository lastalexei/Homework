matrix = [[11, 2, 35], [4, 35, 6], [17, 86, 9]]

def min_max_matrix():
    min_matrix = matrix[0][0]
    max_matrix = matrix[0][0]
    min_matrix_pos = (0, 0)
    max_matrix_pos = (0, 0)
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] < min_matrix:
                min_matrix = matrix[i][j]
                min_matrix_pos = (i, j)

            if matrix[i][j] > max_matrix:
                max_matrix = matrix[i][j]
                max_matrix_pos = (i, j)

    return min_matrix, max_matrix, min_matrix_pos, max_matrix_pos


min_matrix, max_matrix, min_matrix_pos, max_matrix_pos = min_max_matrix()
print(f'Минимальный элемент: {min_matrix} с индексом {min_matrix_pos}')
print(f'Максимальный элемент: {max_matrix} с индексом {max_matrix_pos}')