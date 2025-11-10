num = int(input('Введите число: '))
def is_prime():
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

if is_prime():
    print('Число простое ')
else:
    print('число непростое')
