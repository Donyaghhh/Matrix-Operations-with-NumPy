import numpy as np 

def addition(matrix1:np.ndarray, matrix2:np.ndarray):
    try:
        result = matrix1 + matrix2
        return result
    except:
        return "Cannot be done"

a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[7,8],[9,10],[11,12]])
print(addition(a, b))

def subtraction(matrix1:np.ndarray, matrix2:np.ndarray):
    try:
        result = matrix1 - matrix2
        return result
    except:
        return "Cannot be done"
    
a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[7,8],[9,10],[11,12]])
print(subtraction(a,b))

def multiply(matrix1:np.ndarray, matrix2:np.ndarray):
    try:
        result = matrix1 @ matrix2
        return result
    except:
        return "Cannot be done"
    
a = np.array([[1,2],[3,4],[5,6]])
b = np.array([[7,8],[9,10],[11,12]])
print(multiply(a,b))

def convolution(matrix:np.ndarray, kernel:np.ndarray):

    m_rows, m_cols = matrix.shape
    k_rows, k_cols = kernel.shape

    if k_rows > m_rows or k_cols > m_cols:
        return "Cannot be done"
    out_rows = m_rows - k_rows + 1
    out_cols = m_cols - k_cols + 1
    output = np.zeros((out_rows, out_cols))

    for i in range(out_rows):
        for j in range(out_cols):
            region = matrix[i:i+k_rows, j:j+k_cols]
            output[i, j] = np.sum(region * kernel)
    return output

matrix = np.array([
    [1, 2, 3, 0],
    [4, 5, 6, 1],
    [7, 8, 9, 2]
])

kernel = np.array([
    [1, 0],
    [0, -1]
])

result = convolution(matrix, kernel)
print("Input matrix:\n", matrix)
print("Kernel:\n", kernel)
print("Convolution result:\n", result)