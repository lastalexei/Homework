matrix = [[11, 2, 35],
          [11, 35, 6],
          [17, 6, 9]]


def sum_diagonale():
    summa_side = summa_main = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if i == j:
                summa_main += matrix[i][j]
            if i + j == len(matrix[0]) - 1:
                summa_side += matrix[i][j]
    return summa_side, summa_main


summa_side, summa_main = sum_diagonale()
print(f'Сумма элементов на главной диагонали: {summa_main}\nСумма элементов на побочной диагонали: {summa_side}')
