import random


def generate_random_matrix(M, N):
    matrix = []
    for i in range(M):
        matrix.append([])
        for j in range(N):
            matrix[i].append(random.randint(0, 100))
        print(matrix[i])


generate_random_matrix(3, 3)
