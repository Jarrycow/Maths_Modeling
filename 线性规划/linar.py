import numpy as np
import scipy.io
import scipy.stats
import matplotlib.pyplot as plt

def SE(A):
    if A != []:
        import re
        A=A.replace('[','')
        A=re.split(']',A)
        for i in range(len(A)):
            A[i]=re.split(',',A[i])
            if '' in A[i]:
                A[i].remove('')
            for j in range(len(A[i])):
                if ' 'not in A[i][j]:
                    A[i][j]=float(A[i][j])
    while([] in A):
        A.remove([])
    #A=np.mat(A)
    return A

def Pre():
    s1=input('请输入表达式 \n格式为：min w=ax+by+c\n')
    s2=input('请输入已知式子 \n格式为：A * x ≤ b;\nAeq * x = beq;\nlb  ≤ x ≤ ub\n')
    flag=0
    if 'max' in s1:
        flag=1
        s1=s1.replace('+','!')
        s1=s1.replace('-','@')
        s1=s1.replace('!','-')
        s1=s1.replace('@','+')
        s1=s1.replace('max','min')
        s1=s1.replace(' ','')
        if '=-' not in s1:
            s1=s1.replace('=','=-')
    s1=s1.replace('min','')

    s2=s2.replace('<=','<')
    s2=s2.replace('>=','>')
    s2=s2.split(';')
    i=0;s21="";s22="";s23=""
    while(1):
        s2[i]=s2[i].replace(' ','')
        if '=' in s2[i]:
            s22=s22+s2[i]+'\n'
            #print(s2[i])
        else:
            if '>' in s2[i]:
                s2[i]=s2[i].replace('>','<')
                s2[i]=s2[i].replace('+','!')
                s2[i]=s2[i].replace('-','@')
                s2[i]=s2[i].replace('!','-')
                s2[i]=s2[i].replace('@','+')
                if '<-' not in s2[i]:
                    s2[i]=s2[i].replace('<','<-')
                if s2[i][0] != '-':
                    s2[i]='-'+s2[i]
            count=0;j=0
            for j in range(len(s2[i])):
                if s2[i][j] == '<':
                    count=count+1
                if count == 2:
                    break
            #print(count)
            if count == 1:
                s21=s21+s2[i]+'\n'
                #print(s21)
            if count == 2:
                s23=s23+s2[i]+'\n'
        i=i+1
        if i == len(s2):
            break
    f='';A='';b='';Aeq='';beq='';lb='';ub=''
    print("f:\n"+str(s1));f=input("请输入f:\n")
    print("A * x ≤ b:\n"+str(s21));A=input("请输入A:\n");b=input("请输入b:\n");
    print("Aeq * x = beq:\n"+str(s22));Aeq=input("请输入Aeq:\n");beq=input("请输入beq:\n")
    print("lb  ≤ x ≤ ub:\n"+str(s23));lb==input("请输入lb:\n");ub==input("请输入ub:\n")
    '''f="[[-2,-3,5]]"
    A="[[-2,5,-1],[1,3,1],[-1,0,0],[0,-1,0],[0,0,-1]]"
    b="[[-10],[12],[0],[0],[0]]"
    Aeq="[[1,1,1]]"
    beq="[[7]]"
    lb=''
    ub='''''
    f=SE(f);A=SE(A);b=SE(b);Aeq=SE(Aeq);beq=SE(beq);lb=SE(lb);ub=SE(ub)
    return f,A,b,Aeq,beq,lb,ub,flag


def linar(flag,f,A,b,Aeq=[],beq=[],lb=[],ub=[]):
    f=np.mat(f)
    f=f.transpose()
    f=f.tolist()
    if Aeq==[]:
        print(1)
        l_dict=scipy.optimize.linprog(f,A,b)
    elif lb==[]:
        l_dict=scipy.optimize.linprog(f,A,b,Aeq,beq)
    else:
        l_dict=scipy.optimize.linprog(f,A,b,Aeq,beq,lb,ub)
    if l_dict['success']==True:
        x=l_dict['x']
        y=l_dict['fun']
        if flag==1:
            y=-y
    else:
        x='Flase';y='False'      
    return x,y,l_dict


