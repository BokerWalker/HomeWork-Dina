def checkmatrix (matrix):
    numsinrow = 0
    for r in range(len(matrix)):
        if(numsinrow == 0):
            numsinrow = len(matrix[r])
        else:
            if(numsinrow != len(matrix[r])):
                return False
    return True
            
def matrixmul (fmat,smat):
    if(not checkmatrix(fmat) or not checkmatrix(smat)):
        return
    if(not len(fmat[0]) == len(smat)):
        return
    remat = [[0] * len(smat[0]) for i in range(len(fmat)) ]
    for r in range(len(fmat)): # go through rows
        for c in range(len(smat[0])): # go through columns 
            for n in range (len(smat)): #go through each num in col
                remat[r][c] += fmat[r][n] * smat[n][c]
    return remat
                

def minaddmat (fmat,smat):
    if(not checkmatrix(fmat) or not checkmatrix(smat)):
        return
    rows = min(len(fmat),len(smat))
    columns = min(len(fmat[0]),len(smat[0]))
    remat = [[0 for i in range (columns)] for j in range(rows)]
    for r in range(rows):
        for c in range(columns):
            remat[r][c] = fmat[r][c] + smat[r][c]
    return remat

def maxaddmat (fmat,smat):
    rows = max(len(fmat),len(smat))
    columns = max(len(fmat[0]),len(smat[0]))
    remat = [[0 for i in range (columns)] for j in range(rows)]
    comat = minaddmat(fmat,smat)
    for r in range(rows):
        for c in range(columns):
            try:
                remat[r][c] = comat[r][c]
            except:
                try:
                    remat[r][c] = fmat[r][c]
                except:
                    try:
                        remat[r][c] = smat[r][c]
                    except:
                        remat[r][c] = remat[r][c]
    return remat


one = [[1,2,3,4],[5,6,7,8],[9,1,2,3]]
two = [[1,2],[4,3],[8,8],[7,7]]
mulot = matrixmul(one,two)
print(mulot)
minmat = minaddmat(one,two)
print(minmat)
maxmat = maxaddmat(one,two)
print(maxmat)
            
    

