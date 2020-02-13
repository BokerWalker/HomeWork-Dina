import numpy as np

def dotMatrixes(a,kernel):
    li = [[0] * (len(a) - len(kernel) + 1) for i in range(len(a[0]) - len(kernel[0]) + 1)]
    for r in range(len(a) - len(kernel) + 1):
        for c in range(len(a[0]) - len(kernel[0]) + 1):
            fixed = a[r:r + len(kernel),c: c + len(kernel)]
            li[r][c] = scalarProduct(fixed,kernel) 
    return li

def scalarProduct (mat1,mat2): # Both matrixes in same size
    a = 0
    for r in range(len(mat1)):
        for c in range(len(mat1[0])):
            a += mat1[r][c] * mat2 [r][c] 
    return a

def main ():
    x = np.array([[0,0,0,1,1,0,0,0],
                 [0,0,0,1,1,0,0,0],
                 [0,0,0,1,1,0,0,0],
                 [0,0,0,1,1,0,0,0],
                 [0,0,0,1,1,0,0,0],
                 [0,0,0,1,1,0,0,0],
                 [0,0,0,1,1,0,0,0]])
                 [0,0,0,1,1,0,0,0],
    Kernel = np.array([[0,1,0],
                      [0,1,0],
                      [0,1,0]])
    lis = dotMatrixes(x,Kernel)
    print(lis)
    


main()