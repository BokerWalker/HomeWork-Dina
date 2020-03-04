import numpy as np

def mulmats(a,kernel):
    rows = a.shape[1]- kernel.shape[1] + 1
    culs =  a.shape[0]- kernel.shape[0] + 1
    li = np.zeros((rows,culs))
    for r in range (len(li)):
        for c in range(len(li[0])):
            fixed = a[r:r + len(kernel), c: c + len(kernel[0])]
            mats = fixed * kernel
            li[r][c] = mats.sum()
    return li

def cremat (n):
    ker = np.random.rand(n,n)
    ker *= 5
    return ker


def main():
    mat = cremat()
    kernel = cremat(3)
    temp = mulmats(mat,kernel)
    print(temp, "\n")
    while (True):
        try:
            temp = mulmats(temp,kernel)
            print (temp, "\n")
            kernel = cremat(3)
        except:
           break
        
    









main()