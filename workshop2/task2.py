def k_min(matrix, k):
    n = len(matrix)
    low, high = matrix[0][0], matrix[n-1][n-1]

    while low < high:
        mid = (low + high) // 2 # Берём середину не по индексам, а по значениям
        count = 0 # Количество элементов меньше mid
        i, j = 0, n - 1

        while i < n and j >= 0:
            if matrix[i][j] <= mid: # Сдвиг по строкам
                count += j + 1  
                i += 1
            else: # Сдвиг по столбцам
                j -= 1

        if count < k: # Отсекаем левую часть
            low = mid + 1
        else: # Отсекаем правую часть
            high = mid

    return low

matrix = [
    [1, 5, 9, 13],
    [2, 6, 10, 14], 
    [3, 7, 11, 15], 
    [4, 8, 12, 16]
]
k = 7
print(k_min(matrix, k))

matrix = [
    [1, 5, 9],
    [10, 11, 13],
    [12, 13, 15]
]
k = 8
print(k_min(matrix, k))

