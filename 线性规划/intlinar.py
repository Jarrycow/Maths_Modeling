import numpy as np
f=[[3, 8, 2, 10, 3], [8, 7, 2, 9, 7], [6, 4, 2, 7, 5], [8, 4, 2, 3, 5], [9, 10, 6, 9, 10]]



A=np.zeros((2*len(f),len(f)**2))
for i in range(len(f)):
    for j in range(len(A)*i,len(A)*i+len(A)):
        A[i,j]=1
    for j in range(i,len(f)**2,len(f)):
        A[5+i,j]=1
while(len(f)>1): #矩阵转化为列向量
    f[0]=f[0]+f.pop(1)
intcon=np.arange(1,np.size(f)+1)
