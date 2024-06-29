def get_matrix(n, m, value):

    if n <= 0 or m <= 0:
        return []

    matrix = []

    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)

    return matrix

result1 = get_matrix(3, 5, 24)
result2 = get_matrix(2, 3, 1)
result3 = get_matrix(5, 2, 88)

print('Result 1: ', result1)
print('Result 2: ', result2)
print('Result 3: ', result3)
