
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

