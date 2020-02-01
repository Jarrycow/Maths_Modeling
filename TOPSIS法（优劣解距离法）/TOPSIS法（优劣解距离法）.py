import numpy as np
import scipy.io
#
File_mat = scipy.io.loadmat("E:\Download\BaiduPan\A01所有课件\第1-14讲和番外篇课件和代码\番外篇：基于熵权法对Topsis模型的修正\data_water_quality.mat")
#
X = np.mat(File_mat['X'])
'''判断是否要正向化'''
(n,m)=np.shape(X)
print("共有 "+str(n)+" 个评价对象，"+str(m)+ " 个评价指标")
print('请输入需要处理的这些列的指标类型（0:不需要进行， 1：极小型， 2：中间型， 3：区间型） ')
#Type = input('例如：第2列是极小型，第3列是区间型，第6列是中间型，就输入[1,3,2]：  ')
Type=[0,2,1,3]



def Positivization(X):
    pass
    X = X.transpose()
    X = X.tolist()
    for i in range(len(X)):
        Max = max(X[i])
        if Type[i] == 1:
            for j in range(len(X[i])):
                X[i][j] = Max - X[i][j]
        elif Type[i] == 2:
            Xi = float(input("第"+str(i+1)+"项中间值指标最佳值为"))
            M = []
            for j in range(len(X[i])):
                M.append(abs(X[i][j]-Xi))
            M = max(M)
            for j in range(len(X[i])):
                X[i][j] = 1 - abs(X[i][j] - Xi)/M
        elif Type[i] == 3:
            s=input("请输入第"+str(i+1)+"项最佳区间：")
            s=s.replace('(','');s=s.replace(')','');
            s=s.replace('[','');s=s.replace(']','')
            s=s.replace(' ','');s=s.replace('，',',')
            s=s.replace(':',',');s=s.replace('：',',')
            s=s.replace(';',',');s=s.replace('；',',')
            if s[0] == ',':
                    s=s.split(',')
                    b=float(s[-1])
                    M = max(X[i]) - b
                    for j in range(len(X[i])):
                        if X[i][j] > b:
                            X[i][j] = 1 - abs(X[i][j]-b)/M
                        else:
                            X[i][j] = 1
            elif s[-1] == ',':
                s=s.split(',')
                a=float(s[0])
                M = a - min(X[i])
                for j in range(len(X[i])):
                    if X[i][j] < a:
                        X[i][j] = 1 - abs(X[i][j]-a)/M
                    else:
                        X[i][j] = 1
            else:
                s=s.split(',')
                a=float(s[0])
                b=float(s[-1])
                M=max( a - min(X[i]) , max(X[i]) - b )
                for j in range(len(X[i])):
                    if X[i][j] > a and X[i][j] < b:
                        X[i][j] = 1
                    else:
                        X[i][j] = 1 - abs(X[i][j]-a)/M
    X=np.mat(X).transpose()
    return X


def Standardation(X):
    M = (((np.array(X)**2).sum(axis=0))**0.5)
    for i in range(len(X)):
        for j in range(np.size(X[0])):
            X[i,j] = X[i,j] / M[j]
    return X

def  Distance(X):
    Z_max = np.amax(X,0)
    Z_min = np.amin(X,0)
    
    D_max = (((np.array(Z_max[0,j-1] - X[i-1,j-1])**2).sum(axis=0))**0.5)
    
#X = Positivization(X)
#X = Standardation(X)
