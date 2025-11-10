
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