#Fibonacci Using Matrix Exponentiation
def fibonacci_matrix(n):
    def multiply(mat1, mat2):
        return [[mat1[0][0] * mat2[0][0] + mat1[0][1] * mat2[1][0],
                 mat1[0][0] * mat2[0][1] + mat1[0][1] * mat2[1][1]],
                [mat1[1][0] * mat2[0][0] + mat1[1][1] * mat2[1][0],
                 mat1[1][0] * mat2[0][1] + mat1[1][1] * mat2[1][1]]]

    def power(matrix, n):
        result = [[1, 0], [0, 1]]
        while n:
            if n % 2:
                result = multiply(result, matrix)
            matrix = multiply(matrix, matrix)
            n //= 2
        return result

    if n <= 1:
        return n
    base_matrix = [[1, 1], [1, 0]]
    result_matrix = power(base_matrix, n - 1)
    return result_matrix[0][0]

n = 10
print([fibonacci_matrix(i) for i in range(n)])
