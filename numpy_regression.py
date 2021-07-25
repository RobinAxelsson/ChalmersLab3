from sys import argv
from numpy import loadtxt, transpose, matmul, array
from numpy.linalg import inv as invert
from matplotlib import pyplot as plt

def powers(listVals: list[int], first: int, last: int):
    outMatrix = []
    for val in listVals:
        outMatrix.append([val**i for i in range(first, last+1)])
    return array(outMatrix)

def poly(a,x):
    pass

if __name__ == '__main__':
    file = "chirps-modified.txt" if len(argv) == 1 else argv[1]
    n = 1 if len(argv) < 3 else argv[2]
    matrix = loadtxt(file)
    mtrans = transpose(matrix)
    Xs = mtrans[0]
    Ys = mtrans[1]
    Xp = powers(Xs, 0, n)
    Yp = powers(Ys,1,1)
    Xpt = transpose(Xp)
    [[b],[m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))

    predictChirps = lambda temp : b + m * temp
    plt.plot(Xs,Ys, 'ro')
    plt.plot(Xs,[predictChirps(x) for x in Xs])
    plt.show()