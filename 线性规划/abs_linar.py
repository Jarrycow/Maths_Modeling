import numpy as np
import scipy.io
import scipy.stats
import matplotlib.pyplot as plt
import linar


def Pre():
    f=[[1,2,3,4]]
    A=[[1,-1,-1,1],[1,-1,1,3],[1,-1,-2,3]]
    b=[[-2,-1,-1/2]]
    Aeq=beq=lb=ub=[]
    flag=0
    #[f,A,b,Aeq,beq,lb,ub]=linar.Pre()
    f=f[0]+f[0]
    a=np.mat(A)*(-1)
    a=a.tolist()
    for i in range(len(A)):
        A[i]=A[i]+a[i]
    f=np.mat(f);b=np.mat(b)
    f=f.transpose().tolist()
    b=b.transpose().tolist()
    A=A+np.eye(np.size(f))
    print(type(f));print(type(A));print(type(b))
    x,y,flag = linar.linar(0,f,A,b,Aeq,beq,lb,ub)
    x=(np.mat(x[0:int(np.size(f)/2)])-np.mat(x[int(np.size(f)/2):])).tolist()
    return x,y

x,y=Pre()
