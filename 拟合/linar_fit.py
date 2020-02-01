import numpy as np
import scipy.io
import matplotlib.pyplot as plt
data1 = scipy.io.loadmat('E:\Download\BaiduPan\A01所有课件\第1-14讲和番外篇课件和代码\第4讲.拟合\代码和例题数据\data1.mat')


x=data1['x']
y=data1['y']
def linar_fit(x,y):
    n=np.size(x)
    k=(n*sum(x*y)-sum(x)*sum(y))/(n*sum(x*x)-sum(x)*sum(x))
    b=(sum(x*x)*sum(y)-sum(x)*sum(x*y))/(n*sum(x*x)-sum(x)*sum(x))
    xx=np.arange(min(x)-0.5,max(x)+0.5,0.01)
    yy=k*xx+b
    plt.xlabel('x');
    plt.ylabel('x');
    plt.grid();
    plt.plot(x,y,'o');
    plt.plot(xx,yy,'b');
    plt.show()

    y_hat = k*x+b; # y的拟合值;
    SSR = sum((y_hat-np.mean(y))**2);  # 回归平方和
    SSE = sum((y_hat-y)**2); # 误差平方和
    SST = sum((y-np.mean(y))**2); # 总体平方和
    flag = SSR/SST
    if flag <= 1:
        flag = 1
    else:
        flag = 0
