from sys import argv
from matrix import loadtxt, transpose, powers, matmul, invert
from matplotlib import pyplot as plt

if __name__ == '__main__':
    file = "chirps.txt" if len(argv) == 1 else argv[1]
    matrix = loadtxt(file)
    mtrans = transpose(matrix)
    Xs = mtrans[0]
    Ys = mtrans[1]
    Xp = powers(Xs, 0, 1)
    Yp = powers(Ys,1,1)
    Xpt = transpose(Xp)
    [[b], [m]] = matmul(invert(matmul(Xpt,Xp)),matmul(Xpt,Yp))
    
    predictChirps = lambda temp : b + m * temp
    plt.plot(Xs,Ys, 'ro')
    plt.plot(Xs,[predictChirps(x) for x in Xs])
    plt.show()