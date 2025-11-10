task = input('Выебрите задание(1-14): ')

if int(task) == 1:
    def binary_search_recursive(arr, left, right, n):
        if left > right:
            return -1
        middle = (left + right) // 2
        if arr[middle] == n:
            return middle
        elif arr[middle] > n:
            return binary_search_recursive(arr, left, middle - 1, n)
        elif arr[middle] < n:
            return binary_search_recursive(arr, middle + 1, right, n)


    sort_list = [1, 2, 3, 4, 5, 6, 7]
    required_number = int(input('Введите искомое значение: '))
    result = binary_search_recursive(sort_list, 0, len(sort_list) - 1, required_number)
    print(f'Индекс числа {required_number} - {result}')

elif int(task) == 2:
    def iterative(n):
        binary = ''
        while n > 0:
            binary += str(n % 2)
            n = n // 2
        return binary[::-1]


    def recursive(n):
        if n == 0:
            return ''
        return recursive(n // 2) + str(n % 2)


    num = int(input('Введите десятчное число: '))
    print(f'Число {num} в двоичной системе(итеративно): {iterative(num)}')
    print(f'Число {num} в двоичной системе(рекурсивно): {recursive(num)}')

elif int(task) == 3:
    def is_prime():
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True


    num = int(input('Введите число: '))
    if is_prime():
        print('Число простое ')
    else:
        print('число непростое')

elif int(task) == 4:
    print('НОД из преидущего дз')

elif int(task) == 5:
    text_cipher = input('Введите строку для шифра Цезаря: ')
    action = input('Шифровать - 1, дешифровать - 2: ')
    alphabet_ru_big = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_ru_small = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_eng_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_eng_small = 'abcdefghijklmnopqrstuvwxyz'
    exceptions = 'ЭЮЯэюяXYZxyz'
    steps = 3
    new_cipher = []


    def cypher_caesar(step):
        for i in text_cipher:
            if i in alphabet_ru_big:
                alphabet = alphabet_ru_big
            elif i in alphabet_ru_small:
                alphabet = alphabet_ru_small
            elif i in alphabet_eng_big:
                alphabet = alphabet_eng_big
            elif i in alphabet_eng_small:
                alphabet = alphabet_eng_small
            else:
                new_cipher.append(i)
                continue

            if i in exceptions:
                new_str = alphabet[alphabet.index(i) + step - len(alphabet)]
                new_cipher.append(new_str)
            else:
                new_str = alphabet[alphabet.index(i) + step]
                new_cipher.append(new_str)
        return ''.join(new_cipher)


    def decypher_caesar(step):
        return cypher_caesar(step)


    if action == '1':
        print(cypher_caesar(steps))
    elif action == '2':
        print(decypher_caesar(-steps))
    else:
        print('action error')

elif int(task) == 6:
    vigenere = input('Введите строку для шифра Виженера: ')
    key = input('Введите ключ: ')
    action = input('Шифровать - 1, дешифровать - 2: ')
    new_key = key * (len(vigenere) // len(key) + 1)
    new_key = new_key[:len(vigenere)]
    print(f'Новый ключ: {new_key}')
    alphabet_ru_big = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    alphabet_ru_small = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    alphabet_eng_big = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet_eng_small = 'abcdefghijklmnopqrstuvwxyz'
    new_vegenere = []


    def cypher_vigenere(cypher):
        for i in range(len(vigenere)):
            char_vigenere = vigenere[i]
            char_key = new_key[i]
            if char_vigenere in alphabet_ru_big:
                alphabet = alphabet_ru_big
            elif char_vigenere in alphabet_ru_small:
                alphabet = alphabet_ru_small
            elif char_vigenere in alphabet_eng_big:
                alphabet = alphabet_eng_big
            elif char_vigenere in alphabet_eng_small:
                alphabet = alphabet_eng_small
            else:
                new_vegenere.append(char_vigenere)
                continue
            idx = ((alphabet.index(char_vigenere) + cypher * alphabet.index(char_key)) % len(alphabet))
            new_vegenere.append(alphabet[idx])
        return ''.join(new_vegenere)


    def decypher_vigenere(cypher):
        return cypher_vigenere(cypher)


    if action == '1':
        print(cypher_vigenere(1))
    elif action == '2':
        print(cypher_vigenere(-1))
    else:
        print('action error')

elif int(task) == 7:
    import random


    def generate_random_matrix(M, N):
        matrix = []
        for i in range(M):
            matrix.append([])
            for j in range(N):
                matrix[i].append(random.randint(0, 100))
            print(matrix[i])


    generate_random_matrix(3, 3)

elif int(task) == 8:
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


    matrix = [[11, 2, 35], [4, 35, 6], [17, 86, 9]]
    min_matrix, max_matrix, min_matrix_pos, max_matrix_pos = min_max_matrix()
    print(f'Минимальный элемент: {min_matrix} с индексом {min_matrix_pos}')
    print(f'Максимальный элемент: {max_matrix} с индексом {max_matrix_pos}')

elif int(task) == 9:
    def sum_matrix():
        num_columns = len(matrix[0])
        summa = 0
        columns_sum = num_columns * [0]
        for row in matrix:
            for j, col in enumerate(row):
                columns_sum[j] += col
                summa += col
        return summa, columns_sum


    matrix = [[11, 2, 35], [4, 35, 6], [17, 86, 9]]
    summa, columns_sum = sum_matrix()

    print(f'Сумма элементов матрицы - {summa}')
    for j, column in enumerate(columns_sum):
        print(f'Процент столбца {j} - {column / summa * 100:.3f} %')

elif int(task) == 10:
    k = 1
    new_matrix = []


    def multiply_columns():
        for i in range(len(matrix)):
            new_rows = []
            for j in range(len(matrix[i])):
                new_rows.append(matrix[i][j] * matrix[i][k])
            new_matrix.append(new_rows)
        return new_matrix


    print(multiply_columns())

elif int(task) == 11:
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
