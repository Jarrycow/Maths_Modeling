% % % % % % % % % % % % % % % % % % % % % % % % % % % 
% % % % % % % % % % % % % % % % % % % % % % % % % % % 
% %  指派问题
% %  已知
% % % x(inction)为整数
% % % A * X <= b
% % % Aeq * x = beq
% % % lb <= x <= ub
% % 求
% % % min f'x

function [x,y]=Appointlinar(f,A,b)
n=size(f,1);
Aeq=zeros(2*n,n^2);
for i=1:n
    Aeq(i,(i-1)*n+1:n*i)=1;
    Aeq(n+i,i:n:n^2)=1;
end;clear i
f=f(:);
intcon=1:n;
beq=ones(2*n,1);lb=zeros(n*n,1);ub=ones(n*n,1);
[x,y]=intlinprog(f,intcon,A,b,Aeq,beq,lb,ub);
a=[n,n];
x=reshape(x,a);
end