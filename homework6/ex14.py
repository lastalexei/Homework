matrix = [
    [1, 0, 1],
    [0, 1, 0],
    [1, 1, 0]
]


def add_column():
    for i in range(len(matrix)):
        if sum(matrix[i]) % 2 == 0:
            matrix[i].append(0)
        else:
            matrix[i].append(1)
    for row in matrix:
        print(row)


add_column()
