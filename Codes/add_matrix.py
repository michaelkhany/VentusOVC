
"""
Get new_matrix
Check its size
Add its values into main_matrix
"""
 
def addmatrix(matrix_a,matrix_b):
    if len(matrix_a) == len(matrix_b):
        for i in range(len(matrix_a.matrix)):
            for j in range(len(matrix_a.matrix[0])):
                matrix_a[i][j] = matrix_a[i][j] + matrix_b[i][j]
    return matrix_a
