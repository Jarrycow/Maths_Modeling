% % 0-1规划
% % x(i) = 0 或 1
% % 解
% % lb[i] = 0
% % ub[i]=1
% % % % % % % % % % 
function [x,y]=Appointlinar(f,A,b,Aeq,beq,lb,ub,i)
f=f';
intcon = size(f,1);
lb(i)=0;
ub(i)=1;
[x,y]=intlinprog(f,intcon,A,b,Aeq,beq,lb,ub);
end