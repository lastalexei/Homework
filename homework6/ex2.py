
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
