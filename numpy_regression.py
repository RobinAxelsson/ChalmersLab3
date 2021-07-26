# This program plots x,y values and calculates a general curve used for further prediction of the dataset

from sys import argv
from numpy import loadtxt, transpose, matmul, array, linalg, linspace
from matplotlib import pyplot as plt

def powers(listVals: list[int], first: int, last: int):
    outMatrix = []
    for val in listVals:
        outMatrix.append([val**i for i in range(first, last+1)])
    return array(outMatrix)

if __name__ == '__main__':

    if len(argv)== 3 and argv[2].isnumeric():
        file = argv[1]
        n = int(argv[2])
    else:
        raise ValueError("Input file-path to file containing 'x,y' coordinates as argv[1] and an integer 'n' indicating the polynomal degree as argv[2]")
    matrix = loadtxt(file) # numpy errorhandles the file input
    mtrans = transpose(matrix)
    Xs = mtrans[0]
    Ys = mtrans[1]
    Xp = powers(Xs, 0, n)
    Yp = powers(Ys,1,1)
    Xpt = transpose(Xp)
    a = matmul(linalg.inv(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    As = a[:,0]

    # lambda expression calculating the polynom with n dimensions.
    poly = lambda x, _As : sum([a * x**n for n, a in enumerate(_As)])

    # Creating a greater set of x-values to smoothen the plotted curve
    minX = min(Xs)
    maxX = max(Xs)
    polyXs = linspace(minX,maxX).tolist()

    plt.plot(Xs,Ys, 'ro') # plotting x,y points
    plt.plot(polyXs,[poly(x, As) for x in polyXs]) # plotting predicted curve
    plt.show()