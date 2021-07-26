from sys import argv
from matrix import loadtxt, transpose, powers, matmul, invert
from matplotlib import pyplot as plt

if __name__ == '__main__':
    file = "chirps.txt" if len(argv) == 1 else argv[1]
    matrix = loadtxt(file)
    mtrans = transpose(matrix)

    if len(mtrans) != 2:
        raise ValueError("A two dimensional matrix can only have two lists when transposed.")
    Xs = mtrans[0]
    Ys = mtrans[1]
    Xp = powers(Xs, 0, 1)
    Yp = powers(Ys,1,1)
    Xpt = transpose(Xp)
    [[b], [m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    
    predictedYs = lambda x : b + m * x
    plt.plot(Xs,Ys, 'ro')
    plt.plot(Xs,[predictedYs(x) for x in Xs])
    plt.show()