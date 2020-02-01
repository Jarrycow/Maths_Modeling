#s=input().split()


def JudgeCR(array):
    RI_dict = {1: 0, 2: 0, 3: 0.58, 4: 0.90, 5: 1.12, 6: 1.24, 7: 1.32, 8: 1.41, 9: 1.45}
    row = array.shape[0]  # 计算出阶数
    a_axis_0_sum = array.sum(axis=0)
    # print(a_axis_0_sum)
    b = array / a_axis_0_sum  # 新的矩阵b
    # print(b)
    b_axis_0_sum = b.sum(axis=0)
    b_axis_1_sum = b.sum(axis=1)  # 每一行的特征向量
    w = b_axis_1_sum / row  # 归一化处理(特征向量)
    AW = (w * array).sum(axis=1)
    # print(AW)
    max_max = sum(AW / (row * w))
    # print(max_max)
    CI = (max_max - row) / (row - 1)
    CR = CI / RI_dict[row]
    if CR < 0.1:
        pass
        print("满足一致性")
        return 1
    else:
        print("不满足一致性")
        return 0

def Aver_weight(A): #算术平均法求权重
    '''第一步，矩阵按照列归一化，每一个元素除以其所在列的和'''
    Sum_A = sum(A) #求矩阵每一列的和
    n = len(A) #求矩阵行数列数，np.size(A)求的是元素个数
    SUM_A = np.tile(Sum_A,(n,1)) #相当于MAT中的repmat函数，将矩阵复制n列
    Stand_A = A / SUM_A #每个元素相除
    '''将归一化各列相加，按行求和'''
    Stand_A = np.sum(Stand_A,1) #求矩阵每一行的和
    print("算术平均法求得权重：")
    print(Stand_A/n)
    return Stand_A/n

def GAver_weight(A): #几何平均法求权重
    '''将A的元素按照行相乘得到一个新的列向量'''
    Prduct_A = np.prod(A,1) #prod与sum类似，用于元素相乘
    n = len(A) #求矩阵行数列数，np.size(A)求的是元素个数
    '''第二步：将新的向量的每个分量开n次方'''
    Prduct_n_A = Prduct_A **(1/n)
    '''第三步：对该列向量进行归一化即可得到权重向量
    将这个列向量中的每一个元素除以这一个向量的和即可'''
    print("几何平均法求权重的结果为：")
    print(Prduct_n_A / sum(Prduct_n_A))
    return Prduct_n_A / sum(Prduct_n_A)

def Eig_weight(A):
    row = A.shape[0]  # 计算出阶数
    a_axis_0_sum = A.sum(axis=0)
    # print(a_axis_0_sum)
    b = A / a_axis_0_sum  # 新的矩阵b
    # print(b)
    b_axis_0_sum = b.sum(axis=0)
    b_axis_1_sum = b.sum(axis=1)  # 每一行的特征向量
    # print(b_axis_1_sum)
    w = b_axis_1_sum / row  # 归一化处理(特征向量)
    return w


def main():
    import numpy as np
    print("输入判断矩阵A：")
    A = input()
    A = np.array(A)
    if JudgeCR(A) == 0:
        pass
    else:
        print(Aver_weight(A))
        print(GAver_weight(A))
        print(Eig_weight(A))
    return 1/3*( Aver_weight(A)+(GAver_weight(A)+(Eig_weight(A))))
