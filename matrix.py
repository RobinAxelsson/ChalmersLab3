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
    for i, _ in enumerate(matrix[0]): # same as "for i in range(len(matrix[0])):""
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

if __name__ == '__main__':
    if loadtxt("chirps.txt") == [[12.5, 81.0], [15.27778, 97.0], [17.5, 103.0], [19.72222, 123.0], [22.2222, 150.0], [25.83333, 182.0], [28.3333, 195.0]]:
        print('PASS!')

### EXTRA MIRROR MATRIX ###

def mirrorMatrix(matrix):
    vals = mapMatrix(matrix)
    reverseVals(vals)
    return buildMatrix(vals)
class Value:
    def __init__(self,x,y,val):
        self.x = x
        self.y = y
        self.val = val
        
def searchVal(vals: list[Value], x, y):
    for v in vals:
        if v.x == x and v.y == y:
            return v.val
    else:
        raise IndexError(f"x or y ({x},{y}) value does not exist")

def mapMatrix(matrix):
    vals: list[Value] = []
    for y, row in enumerate(matrix):
        for x, val in enumerate(row):
            vals.append(Value(x,y,val))
    return vals


def reverseVals(values: list[Value]):
    Xs = set([val.x for val in values])
    Ys = set(([val.y for val in values]))
    Xs_rev = [x for x in reversed(list(Xs))]
    Ys_rev = [y for y in reversed(list(Ys))]

    xDict = {}
    for x, x_rev in zip(Xs, Xs_rev):
        xDict[x] = x_rev
    yDict = {}
    for y, y_rev in zip(Ys, Ys_rev):
        yDict[y] = y_rev

    for val in values:
        val.x = xDict[val.x]
        val.y = yDict[val.y]

def buildMatrix(values: list[Value]):
    rows = max([val.x for val in values])+1
    columns = max([val.y for val in values])+1
    matrix = []
    for x in range(rows):
        newRow = []
        for y in range(columns):
            newRow.append(searchVal(values, x, y))
        matrix.append(newRow)
    return matrix
