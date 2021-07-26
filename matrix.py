def transpose(matrix):
    # Validate input matrix
    if isinstance(matrix, list) == False:
        raise ValueError("Input must be an list")
    if len(matrix) == 0:
        return matrix
    # Check if the lists have the same length
    lengths = [len(x) for x in matrix]
    if len(set(lengths)) != 1:
        raise ValueError("Matrix row/columns is not uniform")

    outMatrix = []
    for i, _ in enumerate(matrix[0]):
        outMatrix.append([])
        for l in matrix:
            outMatrix[i].append(l[i])
    return outMatrix

def powers(listVals: list[int], first: int, last: int):
    outMatrix = []
    for val in listVals:
        outMatrix.append([val**i for i in range(first, last+1)])
    return outMatrix

def matmul(matrixA, matrixB):
    if isinstance(matrixA, list) == False or isinstance(matrixB, list) == False:
        raise ValueError("Must input two matrix")
    if len(matrixA) == 0 or len(matrixB) == 0:
        return []
    mBReverse = transpose(matrixB)
    if len(matrixA[0]) != len(mBReverse[0]):
        raise ValueError('Matricies must match')

    matrixC = []
    for row in matrixA:
        newRow = [__zipSumRows(row, col) for col in mBReverse]
        matrixC.append(newRow)
        
    return matrixC

def __zipSumRows(rowA, columnB):
    return sum([valA*valB for valA, valB in zip(rowA, columnB)])

def invert(matrix2v2):
    [[a, b],[c, d]] = matrix2v2
    det = a*d - b*c
    return [[d/det, -b/det], [-c/det, a/det]]

def loadtxt(filename):
    with open(filename) as textFile:
        lines = textFile.readlines()
    matrix = []
    for line in lines:
        matrix.append([float(val) for val in line.split()])
    return matrix