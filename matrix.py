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

def matmul(mA, mB):
    if isinstance(mA, list) == False or isinstance(mB, list) == False:
        raise ValueError("Must input two matrix")
    if len(mA) == 0 or len(mB) == 0:
        return []
    mBReverse = transpose(mB)
    if len(mA[0]) != len(mBReverse[0]):
        raise ValueError('Matricies must match')
    mC = []
    for row in mA:
        mC.append(buildZipSum(row, mBReverse))
    return mC

def zipsumRows(rowA, columnB):
    return sum([valA*valB for valA, valB in zip(rowA, columnB)])

def buildZipSum(rowA, columns):
    out = []
    for c in columns:
        out.append(zipsumRows(rowA, c))
    return out

if zipsumRows([1, 2, 3], [7, 11, 15]) == 74:
    print('zipSumRows: pass')

if buildZipSum([1,2,3], [[7, 11, 15]]) == [74]:
    print('buildZipSum: pass')

t3 = buildZipSum([1,2,3], [[7, 11, 15], [8,12,16], [9, 13, 17], [10, 14, 18]])
if t3 == [74, 80, 86, 92]:
    print('3: Pass')
else:
    print(t3)