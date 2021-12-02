def transposedMatrix(matrix):
    newMatrix = []
    for i in range(0, len(matrix[0])):
        newVector = []
        for vector in matrix:
            newVector.append(vector[i])
        newMatrix.append(newVector)
    return newMatrix



print(transposedMatrix([[1, 2], [3, 4], [5, 6]]))