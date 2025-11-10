matrix = [[11, 2, 35], [4, 35, 6], [17, 86, 9]]


def sum_matrix():
    num_columns = len(matrix[0])
    summa = 0
    columns_sum = num_columns * [0]
    for row in matrix:
        for j, col in enumerate(row):
            columns_sum[j] += col
            summa += col
    return summa, columns_sum


summa, columns_sum = sum_matrix()

print(f'Сумма элементов матрицы - {summa}')
for j, column in enumerate(columns_sum):
    print(f'Процент столбца {j} - {column / summa * 100:.3f} %')
