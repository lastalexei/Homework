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
