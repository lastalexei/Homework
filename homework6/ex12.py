number = int(input('Введите число H: '))
matrix = [[11, 2, 35],
          [11, 35, 6],
          [17, 6, 9]]


def finding_number():
    include_number = []
    dont_include_number = []

    for j in range(len(matrix[0])):
        has_H = False
        for i in range(len(matrix)):
            if matrix[i][j] == number:
                has_H = True
                break
        if has_H:
            include_number.append(j)
        else:
            dont_include_number.append(j)

    return include_number, dont_include_number


include_number, dont_include_number = finding_number()
print(f'Столбцы {include_number} включают число {number}')
print(f'Столбцы {dont_include_number} не включают число {number}')
